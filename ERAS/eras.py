import pandas as pd

academic_cols = ['Q11', 'Q12', 'Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20']
recreational_cols = ['Q1', 'Q2', 'Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10']

def academic_score(row):
    row['academic'] = sum([row[col] for col in academic_cols])
    return row

def recreational_score(row):
    row['recreational'] = sum([row[col] for col in recreational_cols])
    return row

def total_score(row):
    row['total'] = sum([row['academic'], row['recreational']])
    return row








sheet1 = pd.read_excel('data/ERAS data(1).xlsx', sheet_name='ERAS')

sheet1 = academic_score(sheet1)
sheet1 = recreational_score(sheet1)
sheet1 = total_score(sheet1)