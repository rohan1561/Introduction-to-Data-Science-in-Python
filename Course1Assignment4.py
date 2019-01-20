# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import re
import scipy.stats as st

directory = r'/home/rohan/Downloads/ML/PythonProjectsSolutions/IntroToDataScienceInPython(Course1)/course1_downloads/'
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

def get_list_of_university_towns():
    File = open(directory + r'university_towns.txt', 'r')
    states = [] 
    current_line = File.readline()
    while(current_line):
        if '[edit]' in current_line:
            current_line = re.sub(r'\[.*', '', current_line)
            state = current_line.strip()
        elif '[edit]' not in current_line:
            current_line = re.sub(r'\(.*', '', current_line).strip()
            states.append([state, current_line])
        current_line = File.readline()
    df = pd.DataFrame(states, columns=['State', 'RegionName'])
    return df
print('ANSWER ONE:\n{}'.format(get_list_of_university_towns()))
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')


def get_recession_start():
    df = pd.read_excel(directory + r'gdplev.xls', skiprows=219)
    df.drop('Unnamed: 3', axis=1, inplace=True)
    df.drop('Unnamed: 7', axis=1, inplace=True)
    df.columns = ['Year', 'GDP Ann', 'GDP(chained 2009) Ann', 'Quarter','GDP Quar', 'GDP(chained 2009) Quar']
    length = len(df['Quarter'])
    recession = False
    for i in range(length - 4):
        if recession:
            break
        if (df.iloc[i+1]['GDP Quar'] < df.iloc[i]['GDP Quar']) and (df.iloc[i+2]['GDP Quar'] < df.iloc[i+1]['GDP Quar']):
            rec_start = df.iloc[i].Quarter
            for j in range(i + 2, length - 2):
                if (df.iloc[j]['GDP Quar'] < df.iloc[j+1]['GDP Quar']) and (df.iloc[j+1]['GDP Quar'] < df.iloc[j+2]['GDP Quar']):
                    rec_end = df.iloc[j+2].Quarter
                    recession = True
                    break
    return rec_start
print('ANSWER TWO:\n{}'.format(get_recession_start()))
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')


def get_recession_end():
    df = pd.read_excel(directory + r'gdplev.xls', skiprows=219)
    df.drop('Unnamed: 3', axis=1, inplace=True)
    df.drop('Unnamed: 7', axis=1, inplace=True)
    df.columns = ['Year', 'GDP Ann', 'GDP(chained 2009) Ann', 'Quarter','GDP Quar', 'GDP(chained 2009) Quar']
    length = len(df['Quarter'])
    recession = False
    for i in range(length - 4):
        if recession:
            break
        if (df.iloc[i+1]['GDP Quar'] < df.iloc[i]['GDP Quar']) and (df.iloc[i+2]['GDP Quar'] < df.iloc[i+1]['GDP Quar']):
            rec_start = df.iloc[i].Quarter
            for j in range(i + 2, length - 2):
                if (df.iloc[j]['GDP Quar'] < df.iloc[j+1]['GDP Quar']) and (df.iloc[j+1]['GDP Quar'] < df.iloc[j+2]['GDP Quar']):
                    rec_end = df.iloc[j+2].Quarter
                    recession = True
                    break
    return rec_end
print('ANSWER THREE:\n{}'.format(get_recession_end()))
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')


def get_recession_bottom():
    df = pd.read_excel(directory + r'gdplev.xls', skiprows=219)
    df.drop('Unnamed: 3', axis=1, inplace=True)
    df.drop('Unnamed: 7', axis=1, inplace=True)
    df.columns = ['Year', 'GDP Ann', 'GDP(chained 2009) Ann', 'Quarter','GDP Quar', 'GDP(chained 2009) Quar']
    df = df.loc[:, ['Quarter', 'GDP Quar']]
    rec_start = df.index[df.Quarter == get_recession_start()][0]
    rec_end = df.index[df.Quarter == get_recession_end()][0]
    df = df.iloc[rec_start : rec_end, :] 
    answer =  df.loc[df['GDP Quar'].idxmin()].Quarter
    return answer
print('ANSWER FOUR:\n{}'.format(get_recession_bottom()))
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')


def convert_housing_data_to_quarters():
    df = pd.read_csv(directory + r'City_Zhvi_AllHomes.csv')
    df1 = df[['RegionName', 'State']]
    df1['State'] = df1['State'].map(states)
    df = df.loc[:, '2000-01':]
    columns = df.columns.tolist()
    columns = [columns[x:x+3] for x in range(0, len(columns), 3)]
    for column in columns:
        if column[0].split('-')[1] == '01':
            q = 'q1'
        elif column[0].split('-')[1] == '04':
            q = 'q2'
        elif column[0].split('-')[1] == '07':
            q = 'q3'
        elif column[0].split('-')[1] == '10':
            q = 'q4'
        quarter = column[0].split('-')[0] + q
        df[quarter] = df.loc[:, column].mean(axis=1)
    df = df.loc[:, '2000q1':]
    df = pd.concat([df1, df], axis=1)
    df.set_index(['State', 'RegionName'], inplace=True)

    return df
print('ANSWER FIVE:\n{}'.format(convert_housing_data_to_quarters().head(10))) 
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

def run_ttest():
    df = convert_housing_data_to_quarters()
    quar_b4_rec = get_recession_start()
    recession_bottom = get_recession_bottom()
    df = df.loc[:, quar_b4_rec:recession_bottom]
    df.reset_index(inplace=True)
    df['PriceRatio'] = (df['2008q3'] - df['2009q2'])/df['2008q3']
    uni = get_list_of_university_towns()['RegionName']
    df_uni = df[df['RegionName'].isin(uni)]
    df_non_uni = df[~df['RegionName'].isin(uni)]
    
    better = ['university town' if df_uni['PriceRatio'].mean() < df_non_uni['PriceRatio'].mean() else 'non-university town'][0]
    pval = st.ttest_ind(df_uni['PriceRatio'].dropna(), df_non_uni['PriceRatio'].dropna())
    return(True, list(pval)[1], better) 


print(run_ttest())

