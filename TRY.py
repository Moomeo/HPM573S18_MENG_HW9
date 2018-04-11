from enum import Enum
import numpy as np
import scipy.stats as stat
import math as math
import InputData as Data
import scr.MarkovClasses as MarkovCls
import scr.RandomVariantGenerators as Random
import scr.ProbDistParEst as Est


class HealthStats(Enum):
    """ health states of patients"""
    Well = 0
    POST_STROKE = 1
    STROKE = 2
    DEATH = 3

print(len(HealthStats))
