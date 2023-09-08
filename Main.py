import Roller

def printStats (rolls: [int]):
    stats: tuple = Roller.getStats(rolls)
    print(stats.min())
    print(stats.max())
    print(stats.mean())
    print(stats.medi())
    print(stats.mode())

if __name__ == "__main__":
    dice = lambda: Roller.ExplosiveSix(3,6)
    counter = Roller.higherthanFactory(3)

    iterations = [int] * 5
    for i in range(0, len(iterations)): 
        val: [int] = dice()
        print(val,counter(val),sum(val))
        printStats(val)
        iterations[i] = val
    
