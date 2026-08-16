"""Excavation 183: dependency-free evidence for this chapter.
"""

import re
def redact(text):
    text=re.sub(r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b","[EMAIL]",text)
    return re.sub(r"\b\d{3}-\d{4}\b","[PHONE]",text)
def demo():
    out=redact("Call Maya at 555-0142 or maya@example.org about the tiger"); assert "555" not in out and "example.org" not in out
    return {"redacted":out}

if __name__ == "__main__":
    print(demo())
