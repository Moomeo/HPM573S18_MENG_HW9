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


class Therapies(Enum):
    """ mono vs. combination therapy """
    MONO = 0
    COMBO = 1


class ParametersFixed():
    def __init__(self, therapy):

        # selected therapy
        self._therapy = therapy

        # simulation time step
        self._delta_t = Data.DELTA_T

        # initial health state
        self._initialHealthState = HealthStats.Well

        # annual treatment cost
        self._annualTreatmentCost = Data.STROKE_COST

        # transition probability matrix of the selected therapy
        self._prob_matrix = []

        # treatment relative risk for post_stroke and death
        self._treatmentRR = Data.TREATMENT_RR
        self._treatmentRRdead = Data.TREATMENT_RR_DEAD

        # calculate transition probabilities between stroke states
        self._prob_matrix = calculate_prob_matrix()

        # update the transition probability matrix if therapy is being used
        if self._therapy == Therapies.COMBO:
            # calculate transition probability matrix for the combination therapy
            self._prob_matrix = calculate_prob_matrix_combo(
                matrix_mono=self._prob_matrix, combo_rr=Data.TREATMENT_RR, combo_rr_dead=Data.TREATMENT_RR_DEAD)

    def get_initial_health_state(self):
        return self._initialHealthState

    def get_delta_t(self):
        return self._delta_t

    def get_transition_prob(self, state):
        return self._prob_matrix[state.value]

    def get_transition_prob_whole(self):
        return self. _prob_matrix


def calculate_prob_matrix():
    """ :returns transition probability matrix for hiv states under mono therapy"""

    # create an empty matrix populated with zeroes
    prob_matrix = []
    for s in HealthStats:
        prob_matrix.append([0] * len(HealthStats))

    prob_matrix = Data.TRANS_MATRIX

    return prob_matrix


def calculate_prob_matrix_combo(matrix_mono, combo_rr,combo_rr_dead):
    """
    :param matrix_mono: (list of lists) transition probability matrix under mono therapy
    :param combo_rr: relative risk of the combination treatment
    :param combo_rr: relative risk of the combination treatment to increase death
    :returns (list of lists) transition probability matrix under combination therapy """

    # create an empty list of lists
    matrix_combo = []
    for l in matrix_mono:
        matrix_combo.append([0] * len(l))

    # populate the combo matrix
    # first non-diagonal elements
    matrix_combo = matrix_mono
    s=1
    matrix_combo[1][1] = combo_rr* matrix_mono[1][1]
    matrix_combo[1][3]=combo_rr_dead*combo_rr*matrix_mono[1][3]
    matrix_combo[1][2]= 1-matrix_combo[1][1]- matrix_combo[1][3]

    return matrix_combo