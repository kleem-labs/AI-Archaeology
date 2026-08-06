"""Use one weight to see slow progress, useful progress, and overshoot."""

def loss(weight):
    return (weight - 3.0) ** 2

def gradient(weight):
    return 2.0 * (weight - 3.0)

def train(start, rate, steps):
    weight = start
    history = []
    for _ in range(steps):
        history.append((weight, loss(weight), gradient(weight)))
        weight -= rate * gradient(weight)
    history.append((weight, loss(weight), gradient(weight)))
    return history

def run():
    for rate in (.01, .1, 1.0):
        history = train(8.0, rate, 5)
        print("rate", rate, "losses", [round(row[1], 4) for row in history])
    assert train(8.0, .1, 1)[-1][1] < loss(8.0)
    assert train(8.0, 1.0, 1)[-1][1] == loss(8.0)

if __name__ == "__main__":
    run()

