"""Stage 1 — A Tiny GPT — Close the Prediction Loop, with operations visible."""

def generate(prompt,forward,steps,choose):
 tokens=list(prompt)
 for _ in range(steps): tokens.append(choose(forward(tokens)))
 return tokens
