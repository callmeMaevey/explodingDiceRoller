import statistics 
from collections import namedtuple
from random import randint as roll

def ExplosiveSix(quant: int, numOfSides: int) -> [int]:
    accum: [int] = []
    for iteration in range (0, quant):
        accum.append(roll(1,numOfSides))
        if accum[-1] == 6: 
            for explosion in ExplosiveSix(1,numOfSides):
                accum.append(explosion)
    return accum

def higherthanFactory(value: int):
    def higherthan(pool: [int]) -> int:
        accum: int = 0
        for die in pool:
            if die > value: accum += 1 
        return accum
    return higherthan

def getStats(rolls: [int]) -> tuple:
    nums: [int] = rolls.copy()
    nums.sort()
    stats = namedtuple("stats",["min", "max", "mean", "medi", "mode"])
    return stats(
        lambda: "minimum: " + str(nums[0]),
        lambda: "maximum: " + str(nums[len(nums) - 1]),
        lambda: "mean: "    + str(statistics.mean(nums)),
        lambda: "median: "  + str(statistics.median(nums)),
        lambda: "mode: "    + str(statistics.multimode(nums))
    )

