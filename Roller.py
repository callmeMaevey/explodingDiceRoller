import random, statistics

def AddDice (quant: int, numOfSides: int) -> int:
    accum: int = 0
    for iteration in range (0, quant):
        value: int = random.randint(1,numOfSides)
        accum += value
        if value == 6:
            accum += AddDice(1,numOfSides)
    return accum

def getStats(rolls: list):
    nums: list = rolls.copy()
    nums.sort()
    def get( stat: str ):
        match stat:
            case "min":  return "minimum: " + str(nums[0]) 
            case "max":  return "maximum: " + str(nums[len(nums) - 1])
            case "mean": return "mean: "    + str(statistics.mean(nums))
            case "med":  return "median: "  + str(statistics.median(nums))
            case "mode": return "mode: "    + str(statistics.mode(nums))
            case _: return "n/a"
    return get

def printStats (rolls: list):
    stats = getStats(rolls)
    print(stats("min"))
    print(stats("max"))
    print(stats("mean"))
    print(stats("med"))
    print(stats("mode"))



