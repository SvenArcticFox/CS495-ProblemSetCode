import sys

# Iterations
iterations = 100

# Discount
discount = 1

# Probabilities
coolToCoolFastProb = 0.5
coolToWarmFastProb = 0.5
coolToOverheatFastProb = 0

warmToCoolFastProb = 0
warmToWarmFastProb = 0
warmToOverheatFastProb = 1

overheatToCoolFastProb = 0
overheatToWarmFastProb = 0
overheatToOverheatFastProb = 0

coolToCoolSlowProb = 1
coolToWarmSlowProb = 0
coolToOverheatSlowProb = 0

warmToCoolSlowProb = 0.5
warmToWarmSlowProb = 0.5
warmToOverheatSlowProb = 0

overheatToCoolSlowProb = 0
overheatToWarmSlowProb = 0
overheatToOverheatSlowProb = 0

# Rewards
slowToCoolReward = 1
fastToCoolReward = 2

slowToWarmReward = 1
fastToWarmReward = 2

slowToOverheatedReward = -10
fastToOverheatedReward = -10


def main(args):
    # Left = cool, middle = warm, right = overheat
    v = [(0, 0, 0)] # initial state, everything is 0
    i = 1

    print("Cool, Warm, Overheat")
    print(v[0])

    while i <= iterations:
        coolIter = iterateCool(v[i - 1])
        warmIter = iterateWarm(v[i - 1])
        overheatIter = iterateOverheat(v[i - 1])

        v.insert(i, (coolIter, warmIter, overheatIter))
        print(v[i])

        i += 1


def iterateCool(prevIter):
    fast = 0
    fast += coolToCoolFastProb * (fastToCoolReward + (discount * prevIter[0]))
    fast += coolToWarmFastProb * (fastToWarmReward + (discount * prevIter[1]))
    fast += coolToOverheatFastProb * (fastToOverheatedReward + (discount * prevIter[2]))

    slow = 0
    slow += coolToCoolSlowProb * (slowToCoolReward + (discount * prevIter[0]))
    slow += coolToWarmSlowProb * (slowToWarmReward + (discount * prevIter[1]))
    slow += coolToOverheatSlowProb * (slowToOverheatedReward + (discount * prevIter[2]))

    return max(fast, slow)


def iterateWarm(prevIter):
    fast = 0
    fast += warmToCoolFastProb * (fastToCoolReward + (discount * prevIter[0]))
    fast += warmToWarmFastProb * (fastToWarmReward + (discount * prevIter[1]))
    fast += warmToOverheatFastProb * (fastToOverheatedReward + (discount * prevIter[2]))

    slow = 0
    slow += warmToCoolSlowProb * (slowToCoolReward + (discount * prevIter[0]))
    slow += warmToWarmSlowProb * (slowToWarmReward + (discount * prevIter[1]))
    slow += warmToOverheatSlowProb * (slowToOverheatedReward + (discount * prevIter[2]))

    return max(fast, slow)

def iterateOverheat(prevIter):
    fast = 0
    fast += overheatToCoolFastProb * (fastToCoolReward + (discount * prevIter[0]))
    fast += overheatToWarmFastProb * (fastToWarmReward + (discount * prevIter[1]))
    fast += overheatToOverheatFastProb * (fastToOverheatedReward + (discount * prevIter[2]))

    slow = 0
    slow += overheatToCoolSlowProb * (slowToCoolReward + (discount * prevIter[0]))
    slow += overheatToWarmSlowProb * (slowToWarmReward + (discount * prevIter[1]))
    slow += overheatToOverheatSlowProb * (slowToOverheatedReward + (discount * prevIter[2]))

    return max(fast, slow)



if __name__ == "__main__":
    main(sys.argv)
