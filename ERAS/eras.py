import pandas as pd
import numpy as np

academic_cols = ['Q11', 'Q12', 'Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20']
recreational_cols = ['Q1', 'Q2', 'Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10']

def academic_score(row, cols, row_lab):
    row['academic'+row_lab] = sum([row[col] for col in cols])
    return row

def recreational_score(row, cols, row_lab):
    row['recreational'+row_lab] = sum([row[col] for col in cols])
    return row

def total_score(row):
    row['total'] = sum([row['academic'], row['recreational']])
    return row




eras_tab = pd.read_excel('data/ERAS data(1).xlsx', sheet_name='ERAS')
test_retest_tab = pd.read_excel('data/ERAS data(1).xlsx', sheet_name='Test Re-test')
alt_forms_tab = pd.read_excel('data/ERAS data(1).xlsx', sheet_name='Alternate Forms')

eras_tab = academic_score(eras_tab, academic_cols, "")
eras_tab = recreational_score(eras_tab, recreational_cols, "")
eras_tab = total_score(eras_tab)

test_retest_tab = academic_score(test_retest_tab)
test_retest_tab = recreational_score(test_retest_tab)
test_retest_tab = total_score(test_retest_tab)

alt_forms_tab = academic_score(alt_forms_tab)
alt_forms_tab = recreational_score(alt_forms_tab)
alt_forms_tab = total_score(alt_forms_tab)

# Getting correlation between the two tries
test_retest_tab = test_retest_tab[test_retest_tab['Grade'] == 1].copy()
try1 = test_retest_tab[:40].copy()
try2 = test_retest_tab[40:].copy()
all_tries = try1.merge(try2, how='inner', on='Number')
academic_pearson = np.corrcoef(all_tries['academic_x', all_tries['academic_y']])
recreational_pearson = np.corrcoef(all_tries['recreational_x', all_tries['recreational_y']])
total_pearson = np.corrcoef(all_tries['total_x', all_tries['total_y']])

# Getting correlation between two forms
form1 = alt_forms_tab[alt_forms_tab['Time'] == 1][['Number', 'academic', 'recreational', 'total']]
form2 = alt_forms_tab[alt_forms_tab['Time'] == 2][['Number', 'academic', 'recreational', 'total']]
all_forms = form1.merge(form2, how='inner', on='Number')
all_acad_pearson = np.corrcoef(all_forms['academic_x'], all_forms['academic_y'])
all_rec_pearson = np.corrcoef(all_forms['recreational_x'], all_forms['recreational_y'])
all_tot_pearson = np.corrcoef(all_forms['total_x'], all_forms['total_y'])


academic_a = ['Q11', 'Q12', 'Q13','Q14','Q15']
academic_b = ['Q16','Q17','Q18','Q19','Q20']
rec_a = ['Q1', 'Q2', 'Q3','Q4','Q5']
rec_b = ['Q6','Q7','Q8','Q9','Q10']

eras_tab = academic_score(eras_tab, academic_a, 'a')
eras_tab = academic_score(eras_tab, academic_b, 'b')
eras_tab = recreational_score(eras_tab, rec_a, 'a')
eras_tab = recreational_score(eras_tab, rec_b, 'b')

inner_acad_perason = np.corrcoef(eras_tab['academica'], eras_tab['academicb'])
inner_rec_perason = np.corrcoef(eras_tab['recreationala'], eras_tab['recreationalb'])


all_cols = academic_cols + recreational_cols