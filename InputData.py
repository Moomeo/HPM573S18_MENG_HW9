# simulation settings
# problem 3 simulate 2,000 patients over 50 years
POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50    # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 1       # years

# transition matrix
TRANS_MATRIX = [
    [0.75,  0.15,    0,     0.1],   # Well
    [0,     0.25,    0.55,  0.2],   # Post-stroke
    [0,     0,       1.0,     0],   # stroke
    [0,     0,       0,     1.0],   # Dead
    ]

# stroke costs
STROKE_COST = 5000

# treatment relative risk
TREATMENT_RR = 0.65
TREATMENT_RR_DEAD = 1.05
