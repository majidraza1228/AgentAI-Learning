from typing import Any, Dict, List, Union

Scalar = Union[str, int, float, bool, None]

def _needs_quotes(s: str) -> bool:
    if s == "" or s.strip() != s:
        return True
    specials = [":", "|"]
    return any(ch in s for ch in specials)

def _fmt_scalar(v: Scalar) -> str:
    if isinstance(v, str):
        return f"\"{v}\"" if _needs_quotes(v) else v
    if v is None:
        return "null"
    return str(v).lower() if isinstance(v, bool) else str(v)

def _is_homogeneous_obj_array(arr: List[Any]) -> bool:
    if not arr or not all(isinstance(x, dict) for x in arr):
        return False
    # same keys across all objects
    keys = list(arr[0].keys())
    return all(list(d.keys()) == keys for d in arr)

def _indent(s: str, n: int) -> str:
    pad = "  " * n
    return "\n".join(pad + line if line else pad for line in s.split("\n"))

def json_to_toon(data: Any, level: int = 0) -> str:
    # dict
    if isinstance(data, dict):
        lines = []
        for k, v in data.items():
            if isinstance(v, (dict, list)):
                lines.append(f"{k}:")
                lines.append(_indent(json_to_toon(v, level + 1), 1))
            else:
                lines.append(f"{k}: {_fmt_scalar(v)}")
        return "\n".join(lines)
    # list
    if isinstance(data, list):
        if _is_homogeneous_obj_array(data) and data and data[0]:
            cols = list(data[0].keys())
            lines = [f"columns: {', '.join(cols)}", "rows:"]
            for obj in data:
                row_vals = []
                for c in cols:
                    val = obj.get(c)
                    if isinstance(val, (dict, list)):
                        row_vals.append("[complex]")
                    else:
                        row_vals.append(_fmt_scalar(val))
                lines.append("- " + "  ".join(row_vals))
            return "\n".join(lines)
        else:
            lines = []
            for item in data:
                if isinstance(item, (dict, list)):
                    lines.append("-")
                    lines.append(_indent(json_to_toon(item, level + 1), 1))
                else:
                    lines.append(f"- {_fmt_scalar(item)}")
            return "\n".join(lines)
    # scalar or multiline string
    if isinstance(data, str) and "\n" in data:
        body = "\n".join("  " + ln for ln in data.split("\n"))
        return "|\n" + body
    return _fmt_scalar(data)

# A permissive TOON -> JSON parser placeholder.
# For production, switch to a formal parser or a grammar-based approach.
def toon_to_json(toon: str) -> Any:
    # Minimal bridge: treat TOON as YAML superset via PyYAML if allowed.
    # Fallback: very simple heuristic-decoder for the demo.
    try:
        import yaml  # type: ignore
        return yaml.safe_load(toon)
    except Exception:
        # Extremely naive fallback: not robust.
        raise ValueError("TOON parsing requires PyYAML. pip install pyyaml")