import json
import os
import re
from typing import Any, Dict, List, Optional

import pyodbc
from dotenv import load_dotenv

from mcp.server.fastmcp import FastMCP, Context

load_dotenv()

app = FastMCP("mssql-mcp")

def get_conn():
    driver = os.getenv("MSSQL_DRIVER", "ODBC Driver 18 for SQL Server")
    server = os.getenv("MSSQL_SERVER", "localhost")
    database = os.getenv("MSSQL_DATABASE", "")
    user = os.getenv("MSSQL_USER", "")
    password = os.getenv("MSSQL_PASSWORD", "")
    encrypt = os.getenv("MSSQL_ENCRYPT", "yes")
    tsc = os.getenv("MSSQL_TRUSTSERVERCERTIFICATE", "yes")

    conn_str = (
        f"DRIVER={driver};SERVER={server};DATABASE={database};"
        f"UID={user};PWD={password};Encrypt={encrypt};TrustServerCertificate={tsc}"
    )
    return pyodbc.connect(conn_str, autocommit=True)

SAFE_SELECT = re.compile(r"^\s*SELECT\b", re.IGNORECASE)

@app.tool()
def list_tables(context: Context) -> Dict[str, Any]:
    """
    List table names in the current database.
    Returns: { "tables": ["dbo.Users", ...] }
    """
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT TABLE_SCHEMA, TABLE_NAME
            FROM INFORMATION_SCHEMA.TABLES
            WHERE TABLE_TYPE='BASE TABLE'
            ORDER BY TABLE_SCHEMA, TABLE_NAME
        """)
        rows = cur.fetchall()
        tables = [f"{r.TABLE_SCHEMA}.{r.TABLE_NAME}" for r in rows]
        return {"tables": tables}

@app.tool()
def describe_table(context: Context, table: str) -> Dict[str, Any]:
    """
    Describe a table's columns.
    Params:
      - table: schema-qualified or plain table name (e.g., 'dbo.Users' or 'Users')
    Returns: { "columns": [{"name": "...", "type": "...", "nullable": true/false, "default": "..."}] }
    """
    schema = "dbo"
    name = table
    if "." in table:
        schema, name = table.split(".", 1)

    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT c.COLUMN_NAME, c.DATA_TYPE, c.IS_NULLABLE, c.COLUMN_DEFAULT
            FROM INFORMATION_SCHEMA.COLUMNS c
            WHERE c.TABLE_SCHEMA = ? AND c.TABLE_NAME = ?
            ORDER BY c.ORDINAL_POSITION
        """, (schema, name))
        cols = []
        for col, dtype, nullable, default in cur.fetchall():
            cols.append({
                "name": col,
                "type": dtype,
                "nullable": True if str(nullable).upper() == "YES" else False,
                "default": default
            })
        return {"columns": cols}

@app.tool()
def run_query(context: Context, sql: str, params: Optional[List[Any]] = None, limit: int = 1000) -> Dict[str, Any]:
    """
    Run a read-only query. Only SELECT is allowed.
    Params:
      - sql: SQL text (must start with SELECT)
      - params: optional positional parameters for parameterized queries
      - limit: max rows to return (default 1000)
    Returns: { "columns": [...], "rows": [[...], ...] }
    """
    if not SAFE_SELECT.match(sql or ""):
        return {"error": "Only SELECT statements are allowed by this server."}

    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute(sql, params or [])
        columns = [d[0] for d in cur.description] if cur.description else []
        rows = []
        count = 0
        for r in cur:
            rows.append([_py_to_json(v) for v in r])
            count += 1
            if count >= max(1, int(limit)):
                break
        return {"columns": columns, "rows": rows}

def _py_to_json(v):
    # Basic conversion for JSON-safe output
    if isinstance(v, (bytes, bytearray)):
        return v.decode("utf-8", errors="replace")
    return v

if __name__ == "__main__":
    # Runs an MCP server over stdio
    app.run()