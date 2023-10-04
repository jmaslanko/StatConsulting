import pandas as pd
import numpy as np

raw_mapping = {
    'PF': ['workingQ3a', 'workingQ3b', 'workingQ3c', 'workingQ3d', 'workingQ3e', 'workingQ3f', 'workingQ3g', 'workingQ3h', 'workingQ3i', 'workingQ3j'],
    'RP': ['workingQ4a', 'workingQ4b', 'workingQ4c', 'workingQ4d'],
    'BP': ['workingQ7', 'workingQ8'],
    'GH': ['workingQ1', 'workingQ11a', 'workingQ11b', 'workingQ11c', 'workingQ11d'],
    'VT': ['workingQ9a', 'workingQ9e', 'workingQ9g', 'workingQ9i'],
    'SF': ['workingQ6', 'workingQ10'],
    'RE': ['workingQ5a', 'workingQ5b', 'workingQ5c'],
    'MH': ['workingQ9b', 'workingQ9c', 'workingQ9d', 'workingQ9f', 'workingQ9h']
}

low_high_mapping = {
    'PF': {'MAX': 6, 'MIN': 2, 'RANGE': 4},
    'RP': {'MAX': 10, 'MIN': 2, 'RANGE': 8},
    'BP': {'MAX': 5, 'MIN': 1, 'RANGE': 4},
    'GH': {'MAX': 5, 'MIN': 1, 'RANGE': 4},
    'VT': {'MAX': 5, 'MIN': 1, 'RANGE': 4},
    'SF': {'MAX': 5, 'MIN': 1, 'RANGE': 4},
    'RE': {'MAX': 10, 'MIN': 2, 'RANGE': 8},
    'MH': {'MAX': 10, 'MIN': 2, 'RANGE': 8}
}

std_mapping = {
    'PF': {'Mean': 81.18122, 'SD': 29.10558},
    'RP': {'Mean': 80.52856, 'SD': 27.13526},
    'BP': {'Mean': 81.74015, 'SD': 24.53019},
    'GH': {'Mean': 72.19795, 'SD': 23.19041},
    'VT': {'Mean': 55.59090, 'SD': 24.84380},
    'SF': {'Mean': 83.73973, 'SD': 24.75775},
    'RE': {'Mean': 86.41051, 'SD': 22.35543},
    'MH': {'Mean': 70.18217, 'SD': 20.50597}
}

VALID_VALUES_DICT = {
    'FIVE': {'values': [1., 2., 3., 4., 5.]}
    ,'THREE': {'values': [1., 2., 3.], 'cols': ['Q3a', 'Q3b', 'Q3c', 'Q3d', 'Q3e', 'Q3f', 'Q3g', 'Q3h','Q3i', 'Q3j']}
    ,'SIX': {'values':[1., 2., 3., 4., 5., 6.], 'cols': ['Q7']}
    }

COLUMNS = ['Q1', 'Q2', 'Q3a', 'Q3b', 'Q3c', 'Q3d', 'Q3e', 'Q3f',
       'Q3g', 'Q3h', 'Q3i', 'Q3j', 'Q4a', 'Q4b', 'Q4c', 'Q4d', 'Q5a', 'Q5b',
       'Q5c', 'Q6', 'Q7', 'Q8', 'Q9a', 'Q9b', 'Q9c', 'Q9d', 'Q9e', 'Q9f',
       'Q9g', 'Q9h', 'Q9i', 'Q10', 'Q11a', 'Q11b', 'Q11c', 'Q11d']

def q1_mapping(value):

    question1_codes = {
        1:5.0
        ,2:4.4
        ,3:3.4
        ,4:2.0
        ,5:1.0
    }
    if np.isnan(value):
        return np.nan
    else:
        return question1_codes[value]

def rev_mapping(value):

    reverse_codes = {
        1:5
        ,2:4
        ,3:3
        ,4:2
        ,5:1
        }
    if np.isnan(value):
        return np.nan
    else:
        return reverse_codes[value]


def out_of_range_value_three(value: float):


    if value in VALID_VALUES_DICT['THREE']['values']:
        output = value
    else:
        output = np.nan
    
    return output

def out_of_range_value_five(value: float):


    if value in VALID_VALUES_DICT['FIVE']['values']:
        output = value
    else:
        output = np.nan
    
    return output

def out_of_range_value_six(value: float):


    if value in VALID_VALUES_DICT['SIX']['values']:
        output = value
    else:
        output = np.nan
    
    return output

def prep_df(df: pd.DataFrame):
    
    data = df.copy()

    for column in COLUMNS:
        data['working' + column] = data[column]

    for col in data.columns:
        if col in VALID_VALUES_DICT['THREE']['cols']:
            data[col] = data[col].apply(out_of_range_value_three)
        elif col in VALID_VALUES_DICT['SIX']['cols']:
            data[col] = data[col].apply(out_of_range_value_six)
        elif col == 'Identifier':
            pass
        else:
            data[col] = data[col].apply(out_of_range_value_five)


    return data

def recalibrate(input_df: pd.DataFrame) -> pd.DataFrame:
    '''
    Recalibrate and reverse score the questions.  
    Additionally, copies of the original columns will be made.

    input: raw_data as a pandas df
    output: processed data as a pandas df
    '''
    data = input_df.copy()
    # cols = ['Q1', 'Q2A', 'Q2B', 'Q3A', 'Q3B', 'Q4A', 'Q4B', 'Q5', 'Q6A', 'Q6B', 'Q6C', 'Q7']
    for column in COLUMNS:
        data['working' + column] = data[column]

    data['workingQ5'] = data['workingQ5'].apply(rev_mapping)
    data['workingQ6A'] = data['workingQ6A'].apply(rev_mapping)
    data['workingQ6B'] = data['workingQ6B'].apply(rev_mapping)
    data['workingQ1'] = data['workingQ1'].apply(q1_mapping)

    return data


def mean_impute(row):
    if row.isnull().any():
        valid_nums = row.dropna()
        num_missing = len(row) - len(valid_nums)
        if len(valid_nums) >= len(row) / 2:
            row_mean = valid_nums.mean()
            row_sum = valid_nums.sum()
            total = (row_mean*num_missing) + row_sum
        else:
            total = np.nan
        return total
    else:
        return row.sum()

def raw(input_df: pd.DataFrame) -> pd.DataFrame:

    data = input_df.copy()

    for value in raw_mapping:
        data['Raw_' + str(value)] = data[raw_mapping[value]].apply(mean_impute, axis=1)
    
    return data


def transformed(data: pd.DataFrame) -> pd.DataFrame:
    
    df = data.copy()

    for value in low_high_mapping:
        df['Transformed_'+value] = ((df['Raw_' + str(value)] - low_high_mapping[value]['MIN'])/low_high_mapping[value]['RANGE'])*100
    
    return df


def standardized(data: pd.DataFrame) -> pd.DataFrame:

    df = data.copy()
    for value in std_mapping:
        df['Standardized_'+value] = (df['Transformed_'+str(value)] - std_mapping[value]['Mean'])/ std_mapping[value]['SD']
    
    return df


def norm_based(data: pd.DataFrame) -> pd.DataFrame:
    
    df = data.copy()
    for value in std_mapping:
        df['NormBased_'+str(value)] = (df['Standardized_'+value]*10)+50
    
    return df


def agg_pcs(data: pd.DataFrame) -> pd.DataFrame:

    df = data.copy()

    cols = [col for col in df.columns if 'Standardized' in col]
    sub_df = df[cols].to_numpy()
    values = np.array([.42402,.35119, .31754, .24954, .02877, -.00753, -.19206, -.22069])
    
    df['AGG_PCS'] = np.dot(sub_df, values)
    
    
    return df


def agg_mcs(data: pd.DataFrame) -> pd.DataFrame:

    df = data.copy()

    cols = [col for col in df.columns if 'Standardized' in col]
    sub_df = df[cols].to_numpy()
    values = np.array([-.22999, -.12329, -.09731, -.01571, .23534, .26876, .43407, .48581])
    
    df['AGG_MCS'] = np.dot(sub_df, values)
    return df

def pcs_mcs(data: pd.DataFrame) -> pd.DataFrame:

    df = data.copy()
    df['PCS'] = (df['AGG_PCS']*10)+50
    df['MCS'] = (df['AGG_MCS']*10)+50

    return df


if __name__ == "__main__":
    raw_data = pd.read_csv('data/Practice SF-36 data1.csv')
    preped_data = prep_df(raw_data)
    data1 = recalibrate(preped_data).copy()
    data2 = raw(data1).copy()
    data3 = transformed(data2).copy()
    data4 = standardized(data3).copy()
    data5 = norm_based(data4).copy()
    data6 = agg_pcs(data5).copy()
    data7 = agg_mcs(data6).copy()
    final_data = pcs_mcs(data7).copy()
    final_data = final_data.drop(columns=[col for col in final_data.columns if "working" in col])
    final_data = final_data.round(2).copy()
    final_data.to_csv('data/SF12_B_OUTPUT.csv')