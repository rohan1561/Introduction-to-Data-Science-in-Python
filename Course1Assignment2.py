# -*- coding: utf-8 -*-

import pandas as pd

# PART ONE
directory = r'/home/rohan/Downloads/ML/PythonProjectsSolutions/IntroToDataScienceInPython(Course1)/course1_downloads/'
df = pd.read_csv(directory + 'olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2] == '01':
        df.rename(columns={col: 'Gold' + col[4:]}, inplace=True)
    if col[:2] == '02':
        df.rename(columns={col: 'Silver' + col[4:]}, inplace=True)
    if col[:2] == '03':
        df.rename(columns={col: 'Bronze' + col[4:]}, inplace=True)
    if col[:1] == '№':
        df.rename(columns={col: '#' + col[1:]}, inplace=True)

name_ids = df.index.str.replace(u'\xc2\xa0', u' ')
print(name_ids)
name_ids = name_ids.str.split('\s\(')
df.index = name_ids.str[0]
df['ID'] = name_ids.str[1].str[:3]
df = df.drop('Totals')
print(df.head(10))
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')


def answer_zero():
    return df.iloc[0]


print('ANSWER ZERO: \n{}'.format(answer_zero()))
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')


def answer_one():
    answer = df.sort_values(['Gold'], ascending=False).iloc[0].name
    return answer


print('ANSWER ONE: \n{}'.format(answer_one()))
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')


def answer_two():
    df['difference'] = df['Gold'] - df['Gold.1']
    answer = df.sort_values(['difference'], ascending=False).iloc[0].name
    return answer


print('ANSWER TWO: \n{}'.format(answer_two()))
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

pd.set_option('display.max_rows', 1000)


def answer_three():
    df_new = df[(df['Gold'] > 0) & (df['Gold.1'] > 0)]
    value = (abs(df_new['Gold'] - df_new['Gold.1']) / df_new['Gold.2'])  # Returns a pd.Series object
    return value.idxmax()


print('ANSWER THREE: \n{}'.format(answer_three()))
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')


def answer_four():
    df['Points'] = 3 * df['Gold.2'] + 2 * df['Silver.2'] + df['Bronze.2']
    return df['Points']


print('ANSWER FOUR: \n{}'.format(answer_four()))
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

# PART TWO
census_df = pd.read_csv(
    r'/home/rohan/Downloads/ML/PythonProjectsSolutions/IntroToDataScienceInPython(Course1)/course1_downloads/census.csv')
print(census_df.head(10))
print(census_df.columns)


def answer_five():
    df_counties = census_df[census_df['SUMLEV'] == 50]
    answer = df_counties.groupby('STNAME').count()['SUMLEV'].idxmax()
    return answer


print('ANSWER FIVE: \n{}'.format(answer_five()))
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')


def answer_six():
    counties = census_df[census_df['SUMLEV'] == 50][['STNAME', 'CTYNAME', 'CENSUS2010POP']]
    counties = counties.sort_values(['STNAME', 'CENSUS2010POP'], ascending=False)
    counties = counties.groupby('STNAME').head(3).groupby('STNAME').sum()
    answer = counties.sort_values('CENSUS2010POP', ascending=False).head(3).index.tolist()
    return answer


print('ANSWER SIX: \n{}'.format(answer_six()))
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')


def answer_seven():
    counties = census_df[census_df['SUMLEV'] == 50]
    counties['change'] = abs(counties['POPESTIMATE2015'] - counties['POPESTIMATE2014']) + abs(
        counties['POPESTIMATE2014'] - counties['POPESTIMATE2013']) + abs(
        counties['POPESTIMATE2013'] - counties['POPESTIMATE2012']) + abs(
        counties['POPESTIMATE2012'] - counties['POPESTIMATE2011']) + abs(
        counties['POPESTIMATE2011'] - counties['POPESTIMATE2010'])
    answer = counties.sort_values('change', ascending=False).iloc[0]['CTYNAME']
    return answer


print('ANSWER SEVEN: \n{}'.format(answer_seven()))
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')


def answer_eight():
    counties = census_df[census_df['SUMLEV'] == 50]
    answer = counties[
        ((counties['REGION'] == 1) | (counties['REGION'] == 2)) & (counties['CTYNAME'].str.startswith('Washington')) & (
        counties['POPESTIMATE2015'] > counties['POPESTIMATE2014'])][['STNAME', 'CTYNAME']]
    return answer


print('ANSWER EIGHT: \n{}'.format(answer_eight()))
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print('XXXXXXXXXXXXXXXXXXXXXXXX--END OF ASSIGNMENT--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
