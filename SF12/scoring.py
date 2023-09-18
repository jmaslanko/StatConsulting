import pandas as pd


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


def raw(raw_data: pd.DataFrame):

    data = raw_data

    for value in raw_mapping:
        data['raw' + str(value)] = 0
        for column in raw_mapping[value]:
            data['raw' + str(value)] = data['raw' + str(value)] + data[column]
    
    return data


def transformed():
    return


def standardized():
    return


def norm_based():
    return


def norm_based():
    return


def norm_based():
    return


def agg():
    return


def pcs_mcs():
    return


if __name__ == "__main__":
    raw_data = pd.read_csv('data/SF12_A.csv')
