from typing import List, Optional, Any
from pydantic import BaseModel, Field

class TraceEvent(BaseModel):
    ts: str
    tool: str
    ok: bool
    ms: Optional[int] = None
    url: Optional[str] = None
    error: Optional[str] = None

class RagChunk(BaseModel):
    id: str
    source: str
    title: str
    score: float
    page: Optional[int] = None
    tags: Optional[List[str]] = None
    content: Optional[str] = None
    events: Optional[List[TraceEvent]] = None
    sections: Optional[List[dict]] = None
    meta: Optional[dict] = None
    mime: Optional[str] = None
    notes: Optional[str] = None
    