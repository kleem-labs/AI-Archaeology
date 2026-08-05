"""Learn the minimum of a one-parameter loss with gradient descent."""
def loss(w): return (w-3.0)**2
def gradient(w): return 2.0*(w-3.0)
if __name__ == "__main__":
    w=0.0; rate=0.1
    for step in range(12):
        print(f"step={step:02d} w={w:.4f} loss={loss(w):.4f} grad={gradient(w):.4f}")
        w-=rate*gradient(w)
