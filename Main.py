import Roller

def printStats (rolls: list):
    stats: function = Roller.getStats(rolls)
    print(stats("min"))
    print(stats("max"))
    print(stats("mean"))
    print(stats("med"))
    print(stats("mode"))


if __name__ == "__main__":
    iterations = [int] * 1000
    dice = lambda: Roller.AddDice(4,6) + Roller.AddDice(2,12)
    for i in range(0, len(iterations)):
        iterations[i] = dice()

    printStats(iterations)

