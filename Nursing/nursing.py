import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

data = pd.read_csv('data/Thankyou.csv')

no_note_data = data[data['Group']== 'No note']
note_data = data[data['Group']== 'Thank you note']

def check_normality(data):
    test_stat_normality, p_value_normality=stats.shapiro(data)
    print("p value:%.4f" % p_value_normality)
    if p_value_normality <0.05:
        print("Reject null hypothesis >> The data is not normally distributed")
    else:
        print("Fail to reject null hypothesis >> The data is normally distributed")

no_note_totals = no_note_data['total'].to_numpy()
note_totals = note_data['total'].to_numpy()

#remove nan values
note_totals = note_totals[~np.isnan(note_totals)]
no_note_totals = no_note_totals[~np.isnan(no_note_totals)]

# check normality
check_normality(no_note_totals)
check_normality(note_totals)

# plot to confirm normailty check
plt.hist(no_note_totals)
plt.title('Hist for Total Score with No Note given')
plt.xlabel('Total Score')
plt.ylabel('Counts of Score')

plt.hist(note_totals)
plt.title('Hist for Total Score with Note given')
plt.xlabel('Total Score')
plt.ylabel('Counts of Score')

# Test given non normal distribution
stat, pvalue = stats.mannwhitneyu(no_note_totals, note_totals)
print(pvalue)
if pvalue > .05:
    print('Fail to reject null hypothesis that means are different')
else:
    print('Reject null hypothesis that means are different')