# MCP in VS Code

Model Context Protocol (MCP) lets VS Code communicate with local and remote tools (models, data sources, code actions) through a standard protocol. This guide helps you enable MCP in VS Code, learn best practices, and see how it helps day‑to‑day development.

---

## 1) Prerequisites
- VS Code latest stable
- Node.js 18+ (for most MCP servers)
- Git installed and on PATH
- Provider account if required by a given MCP server (OpenAI, Anthropic, etc.)

Windows notes:
- Use PowerShell in VS Code terminal
- Config path: %APPDATA%/mcp/config.json
- If scripts do not run: Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
- Consider CRLF vs LF line endings and long path support

---

## 2) Enable MCP in VS Code

1. Install an MCP-enabled VS Code extension or AI/agent extension with MCP support.
2. Open Command Palette → “MCP: Open Config”.
3. Create or update your MCP config file at:
   - macOS/Linux: ~/.config/mcp/config.json
   - Windows: %APPDATA%/mcp/config.json
4. Add one or more servers. Example minimal config:
