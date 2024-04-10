import sys
import numpy as np


def main(args):
    # Left = cool, middle = warm, right = overheat
    v = [(0, 0, 0)] # initial state, everything is 0

    # Probabilities
    coolToCoolFast = 0.5
    coolToWarmFast = 0.5
    coolToOverheatFast = 0

    warmToCoolFast = 0
    warmToWarmFast = 0
    warmToOverheatFast = 1

    overheatToCoolFast = 0
    overheatToWarmFast = 0
    overheatToOverheatFast = 0

    coolToCoolSlow = 1
    coolToWarmSlow = 0
    coolToOverheatSlow = 0

    warmToCoolSlow = 0.5
    warmToWarmSlow = 0.5
    warmToOverheatSlow = 0

    overheatToCoolSlow = 0
    overheatToWarmSlow = 0
    overheatToOverheatSlow = 0


    # Rewards
    slowToCoolReward = 1
    fastToCoolReward = 2

    slowToWarmReward = 1
    fastToWarmReward = 2

    slowToOverheatedReward = -10
    fastToOverheatedReward = -10

    


if __name__ == "__main__":
    main(sys.argv)
