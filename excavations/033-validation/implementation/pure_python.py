"""Stage 1 — Validation — Testing Without Peeking at the Final Exam, with operations visible."""

def split(items,train=.6,validation=.2):
 a=int(len(items)*train); b=a+int(len(items)*validation); return items[:a],items[a:b],items[b:]
