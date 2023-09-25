import pandas as pd
import numpy as np

raw_mapping = {
    'PF': ['Q2A', 'Q2B'],
    'RP': ['Q3A', 'Q3B'],
    'BP': ['Q5'],
    'GH': ['Q1'],
    'VT': ['Q6B'],
    'SF': ['Q7'],
    'RE': ['Q4A', 'Q4B'],
    'MH': ['Q6A', 'Q6C']
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

COLUMNS = ['Q1', 'Q2A', 'Q2B', 'Q3A', 'Q3B', 'Q4A', 'Q4B', 'Q5', 'Q6A', 'Q6B', 'Q6C', 'Q7']

def q1_mapping(value):

    question1_codes = {
        1:5.0
        ,2:4.4
        ,3:3.4
        ,4:2.0
        ,5:1.0
    }

    return question1_codes[value]

def rev_mapping(value):

    reverse_codes = {
        1:5
        ,2:4
        ,3:3
        ,4:2
        ,5:1
        }

    return reverse_codes[value]


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
        data['orginal' + column] = data[column]

    data['Q5'] = data['Q5'].apply(rev_mapping)
    data['Q6A'] = data['Q6A'].apply(rev_mapping)
    data['Q6B'] = data['Q6B'].apply(rev_mapping)
    data['Q1'] = data['Q1'].apply(q1_mapping)

    return data


def raw(input_df: pd.DataFrame) -> pd.DataFrame:

    data = input_df.copy()

    for value in raw_mapping:
        data['Raw_' + str(value)] = 0
        for column in raw_mapping[value]:
            data['Raw_' + str(value)] = data['Raw_' + str(value)] + data[column]
    
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
    raw_data = pd.read_csv('data/SF12_A.csv')
    data1 = recalibrate(raw_data).copy()
    data2 = raw(data1).copy()
    data3 = transformed(data2).copy()
    data4 = standardized(data3).copy()
    data5 = norm_based(data4).copy()
    data6 = agg_pcs(data5).copy()
    data7 = agg_mcs(data6).copy()
    final_data = pcs_mcs(data7).copy()
    final_data = final_data.drop(columns=COLUMNS).copy()
    final_data.columns = [col.replace('orginal', '') for col in final_data.columns]
    final_data = final_data.round(2).copy()
    final_data.to_csv('data/SF12_A_OUTPUT.csv')