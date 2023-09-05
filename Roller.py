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
    def get( stat: str ) -> str:
        pass


    print("minimum: "+ str(nums[0]))
    print("maximum: "+ str(nums[len(nums) - 1]))
    print("mean: "+ str(statistics.mean(nums)))
    print("median high: "+ str(statistics.median_high(nums)))
    print("median: "+ str(statistics.median(nums)))
    print("median low: "+ str(statistics.median_low(nums)))
    print("mode: "+ str(statistics.mode(nums)))


