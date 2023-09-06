import Roller

def printStats (rolls: list):
    stats: function = Roller.getStats(rolls)
    print(stats("min"))
    print(stats("max"))
    print(stats("mean"))
    print(stats("medi"))
    print(stats("mode"))

if __name__ == "__main__":
    iterations = [int] * 1000
    dice = lambda: Roller.AddDice(3,6)
    for i in range(0, len(iterations)):
        iterations[i] = dice()
    
    printStats(iterations)
