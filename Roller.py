import statistics, enum
from collections import namedtuple
from random import randint as roll

def ExplosiveSix(quant: int, numOfSides: int) -> [int]:
    accum: [int] = []
    for iteration in range (0, quant):
        accum.append(roll(1,numOfSides))
        if accum[-1] == 6: accum.append(iter(ExplosiveSix(1,numOfSides)))
    return accum


def higherthanFactory(value: int):
    def higherthan(pool: [int]) -> int:
        accum: int = 0
        for die in pool:
            if die > value: accum += 1 
        return accum
    return higherthan

def getStats(rolls: list):
    nums: list = rolls.copy()
    nums.sort()
    def get( stat: str ):
        match stat:
            case "min":  return "minimum: " + str(nums[0]) 
            case "max":  return "maximum: " + str(nums[len(nums) - 1])
            case "mean": return "mean: "    + str(statistics.mean(nums))
            case "medi": return "median: "  + str(statistics.median(nums))
            case "mode": return "mode: "    + str(statistics.multimode(nums))
            case _: return "n/a"
    return get



