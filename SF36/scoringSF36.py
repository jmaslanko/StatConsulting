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
    'PF': {'MAX': 30, 'MIN': 10, 'RANGE': 20},
    'RP': {'MAX': 20, 'MIN': 4, 'RANGE': 16},
    'BP': {'MAX': 12, 'MIN': 2, 'RANGE': 10},
    'GH': {'MAX': 25, 'MIN': 5, 'RANGE': 20},
    'VT': {'MAX': 20, 'MIN': 4, 'RANGE': 16},
    'SF': {'MAX': 10, 'MIN': 2, 'RANGE': 8},
    'RE': {'MAX': 15, 'MIN': 3, 'RANGE': 12},
    'MH': {'MAX': 25, 'MIN': 5, 'RANGE': 20}
}

std_mapping = {
    'PF': {'Mean': 83.29094, 'SD': 23.75883},
    'RP': {'Mean': 82.50964, 'SD': 25.52028},
    'BP': {'Mean': 71.32527, 'SD': 23.66224},
    'GH': {'Mean': 70.84570, 'SD': 20.97821},
    'VT': {'Mean': 58.31411, 'SD': 20.01923},
    'SF': {'Mean': 84.30250, 'SD': 22.91921},
    'RE': {'Mean': 87.39733, 'SD': 21.43778},
    'MH': {'Mean': 74.98685, 'SD': 17.75604}
}

VALID_VALUES_DICT = {
    'FIVE': {'values': [1., 2., 3., 4., 5.]}
    ,'THREE': {'values': [1., 2., 3.], 'cols': ['workingQ3a', 'workingQ3b', 'workingQ3c', 'workingQ3d', 'workingQ3e', 'workingQ3f', 'workingQ3g', 'workingQ3h','workingQ3i', 'workingQ3j']}
    ,'SIX': {'values':[1., 2., 3., 4., 5., 6.], 'cols': ['workingQ7']}
    }

COLUMNS = ['Q1', 'Q2', 'Q3a', 'Q3b', 'Q3c', 'Q3d', 'Q3e', 'Q3f',
       'Q3g', 'Q3h', 'Q3i', 'Q3j', 'Q4a', 'Q4b', 'Q4c', 'Q4d', 'Q5a', 'Q5b',
       'Q5c', 'Q6', 'Q7', 'Q8', 'Q9a', 'Q9b', 'Q9c', 'Q9d', 'Q9e', 'Q9f',
       'Q9g', 'Q9h', 'Q9i', 'Q10', 'Q11a', 'Q11b', 'Q11c', 'Q11d']

WORKING_COLS = ['workingQ1','workingQ2','workingQ3a',
'workingQ3b','workingQ3c','workingQ3d','workingQ3e',
 'workingQ3f','workingQ3g','workingQ3h','workingQ3i',
 'workingQ3j','workingQ4a','workingQ4b','workingQ4c',
 'workingQ4d','workingQ5a','workingQ5b','workingQ5c',
 'workingQ6','workingQ7','workingQ8','workingQ9a',
 'workingQ9b','workingQ9c','workingQ9d','workingQ9e',
 'workingQ9f','workingQ9g','workingQ9h','workingQ9i',
 'workingQ10','workingQ11a','workingQ11b','workingQ11c','workingQ11d']

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
        if 'working' in col:
            if col in VALID_VALUES_DICT['THREE']['cols']:
                data[col] = data[col].apply(out_of_range_value_three)
            elif col in VALID_VALUES_DICT['SIX']['cols']:
                data[col] = data[col].apply(out_of_range_value_six)
            else:
                data[col] = data[col].apply(out_of_range_value_five)
        else:
            pass

    return data

def recalibrate(input_df: pd.DataFrame) -> pd.DataFrame:
    '''
    Recalibrate and reverse score the questions.  
    Additionally, copies of the original columns will be made.

    input: raw_data as a pandas df
    output: processed data as a pandas df
    '''
    data = input_df.copy()

    data['workingQ11b'] = data['workingQ11b'].apply(rev_mapping)
    data['workingQ11d'] = data['workingQ11d'].apply(rev_mapping)
    data['workingQ9a'] = data['workingQ9a'].apply(rev_mapping)
    data['workingQ9e'] = data['workingQ9e'].apply(rev_mapping)
    data['workingQ6'] = data['workingQ6'].apply(rev_mapping)
    data['workingQ9d'] = data['workingQ9d'].apply(rev_mapping)
    data['workingQ9h'] = data['workingQ9h'].apply(rev_mapping)
    data['workingQ1'] = data['workingQ1'].apply(q1_mapping)

    return data


null7_only_dict = {
    1.:6.
    ,2.:4.75
    ,3.:3.5
    ,4.:2.25
    ,5:1.
}

q7_dict = {
    1.:6.,
    2.:5.4,
    3.:4.2,
    4.:3.1,
    5.:2.2,
    6.:1.
}

both_7_8_dict = {
    1.:{
        1.:6.,
        2.:5.,
        3.:5.,
        4.:5.,
        5.:5.,
        6.:5.
    },
    2.:{
        1.:4.,
        2.:4.,
        3.:4.,
        4.:4.,
        5.:4.,
        6.:4.
    },
    3.:{
        1.:3.,
        2.:3.,
        3.:3.,
        4.:3.,
        5.:3.,
        6.:3.
    },
    4.:{
        1.:2.,
        2.:2.,
        3.:2.,
        4.:2.,
        5.:2.,
        6.:2.,
    },
    5.:{
        1.:1.,
        2.:1.,
        3.:1.,
        4.:1.,
        5.:1.,
        6.:1.
    },
}

def q7_8_recalibrate(row):

    if row.isna().all():
        row['workingQ8'] = np.nan
        row['workingQ7'] = np.nan
    elif pd.isna(row['workingQ7']) and pd.notna(row['workingQ8']):
        row['workingQ8'] = null7_only_dict[row['workingQ8']]
        row['workingQ7'] = row['workingQ7']
    elif pd.notna(row['workingQ7']) and pd.isna(row['workingQ8']):
        row['workingQ8'] = row['workingQ8']
        row['workingQ7'] = q7_dict[row['workingQ7']]
    elif row.notna().all():
        row['workingQ8'] = both_7_8_dict[row['workingQ8']][row['workingQ7']]
        row['workingQ7'] = q7_dict[row['workingQ7']]

    return row


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
    data1[['workingQ7', 'workingQ8']] = data1[['workingQ7', 'workingQ8']].apply(q7_8_recalibrate, axis=1)
    data2 = raw(data1).copy()
    data3 = transformed(data2).copy()
    data4 = standardized(data3).copy()
    data5 = norm_based(data4).copy()
    data6 = agg_pcs(data5).copy()
    data7 = agg_mcs(data6).copy()
    final_data = pcs_mcs(data7).copy()
    final_data = final_data.drop(columns=[col for col in final_data.columns if "working" in col])
    final_data = final_data.round(2).copy()
    final_data.to_csv('data/SF36_data1_OUTPUT.csv')