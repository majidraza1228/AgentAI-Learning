def prompt_rules() -> str:
    return """Return data in TOON.
Rules:
- Indentation defines nesting
- Arrays: use "- item"; for homogeneous objects, prefer compact rows with aligned columns
- Use block strings with "|" for multi-line text
- Only quote strings when necessary to preserve exact characters
"""