import Roller

if __name__ == "__main__":
    iterations = [int] * 1000
    dice = lambda: Roller.AddDice(4,6) + Roller.AddDice(2,12)
    for i in range(0, len(iterations)):
        iterations[i] = dice()

    Roller.printStats(iterations)

