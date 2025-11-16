import json
from pathlib import Path
from typing import Any, List

from tiktoken import get_encoding
from pydantic import ValidationError

from toon import json_to_toon, toon_to_json
from schemas import RagChunk

ENC = get_encoding("cl100k_base")  # close to GPT-4-class models

def count_tokens(s: str) -> int:
    return len(ENC.encode(s))

def load_chunks(path: str) -> List[Any]:
    return json.loads(Path(path).read_text())

def compare_semantics(a: Any, b: Any) -> bool:
    # order-insensitive for dict keys; lists must match order
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        if set(a.keys()) != set(b.keys()):
            return False
        return all(compare_semantics(a[k], b[k]) for k in a.keys())
    if isinstance(a, list):
        if len(a) != len(b):
            return False
        return all(compare_semantics(x, y) for x, y in zip(a, b))
    return a == b

def main():
    chunks = load_chunks("chunks.json")
    for ch in chunks:
        json_str = json.dumps(ch, ensure_ascii=False)
        toon_str = json_to_toon(ch)

        json_tokens = count_tokens(json_str)
        toon_tokens = count_tokens(toon_str)
        delta = json_tokens - toon_tokens

        print("=" * 72)
        print(f"id={ch.get('id')}")
        print(f"tokens json={json_tokens} toon={toon_tokens} Δ={delta}")
        print("\nTOON:\n" + toon_str)

        # Round-trip and validate shape (best-effort)
        try:
            rt = toon_to_json(toon_str)
            # Validate if it looks like a RagChunk
            RagChunk.model_validate(rt)
            ok = compare_semantics(ch, rt)  # may be False if key ordering differs
            print(f"round_trip_validated={ok}")
        except ImportError:
            print("Install pyyaml for TOON -> JSON parsing: pip install pyyaml")
        except ValidationError as ve:
            print("Schema validation failed:", ve)
        except Exception as e:
            print("Round-trip failed:", e)

if __name__ == "__main__":
    main()