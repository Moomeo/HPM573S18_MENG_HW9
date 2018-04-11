import ParameterClasses as P
import MarkovModelClasses as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

# create a cohort
cohort = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.MONO)

# simulate the cohort
simOutputs = cohort.simulate()

#question 3
# get the mean survival time and 95% CI
SupportMarkov.print_outcomes(simOutputs, 'Mono therapy:')

#question 4
#get the transition prob matrix after anticoagulation
para = P.ParametersFixed(P.Therapies.COMBO)
print("the transition prob matrix after anticoagulation is:", para.get_transition_prob_whole())

#question 5
# create a cohort
cohort2  = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.COMBO)

# simulate the cohort
simOutputs2 = cohort2.simulate()

#get the mean survival time and 95% CI under anticoagulation
SupportMarkov.print_outcomes(simOutputs2, 'Combo therapy:')

# question 6
# graph survival curve under no treatment
PathCls.graph_sample_path(
    sample_path=simOutputs.get_survival_curve(),
    title='Survival curve under no treatment',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

# graph survival curve receiving anticoagulation
PathCls.graph_sample_path(
    sample_path=simOutputs2.get_survival_curve(),
    title='Survival curve receiving anticoagulation',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

# question 7
#histogram of number of stroke times no treatment
Figs.graph_histogram(
    data=simOutputs.get_cohort_stroke(),
    title='Times of stroke of patients',
    x_label='Number of stroke during life time with no treatment',
    y_label='Counts',
    bin_width=1
)

#histogram of number of stroke times receiving anticoagulation
Figs.graph_histogram(
    data=simOutputs2.get_cohort_stroke(),
    title='Times of stroke of patients',
    x_label='Number of stroke during life time receiving anticoagulation',
    y_label='Counts',
    bin_width=1
)