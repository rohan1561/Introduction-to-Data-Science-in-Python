import pandas as pd
import numpy as np

#pd.set_option('display.max_rows', 300)
#pd.set_option('display.max_colwidth', 100)
print(pd.__version__)
directory = r'/home/rohan/Downloads/ML/PythonProjectsSolutions/IntroToDataScienceInPython(Course1)/course1_downloads/'


energy = pd.read_excel(directory + r'Energy Indicators.xls', skiprows=17)

# Drop the first two columns and the unwanted footers
energy.drop([u'Unnamed: 1', u'Unnamed: 0'], axis=1, inplace=True)
energy = energy[:227]

# Change column names
energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable\'s']

# Convert Energy Supply from petajoules to gigajoules
energy['Energy Supply'] = energy['Energy Supply']*10**6

# Replace missing data with np.nan
energy['Energy Supply'].replace(r'\.+', np.nan, inplace=True, regex=True)
energy['Energy Supply per Capita'].replace(r'\.+', np.nan, inplace=True, regex=True)

# Replace numbers in country names with null characters
energy['Country'].replace(r'\d+', '', inplace=True, regex=True)

# Replace the countries names
energy['Country'].replace({'Republic of Korea': 'South Korea', 'United States of America': 'United States', 'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom', 'China, Hong Kong Special Administrative Region': 'Hong Kong'}, inplace=True)
energy['Country'].replace(r'\(.*\)', '', inplace=True, regex=True)
energy['Country'] = energy['Country'].str.strip(' ')
#print(energy.head())
#print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

# Load the GDP data from world_bank.csv
GDP = pd.read_csv(directory + r'world_bank.csv', skiprows=4)
GDP['Country Name'].replace({'Korea, Rep.': 'South Korea', 'Iran, Islamic Rep.': 'Iran', 'Hong Kong SAR, China': 'Hong Kong'}, inplace=True)
GDP = GDP[['Country Name', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]

GDP.columns = ['Country', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
#print(GDP.head())

# Load the Sciamgo Journal dataset
ScimEn = pd.read_excel(directory + r'scimagojr-3.xlsx')
#print(ScimEn.head(16))

# Join the three datasets
#ScimEn_J = ScimEn[:15]
#df = pd.merge(ScimEn_J, energy, how='inner', left_on='Country', right_on='Country')
#df = pd.merge(df, GDP, how='inner', left_on='Country', right_on='Country')


def answer_one():
    energy = pd.read_excel(directory + r'Energy Indicators.xls', skiprows=17)

    # Drop the first two columns and the unwanted footers
    energy.drop([u'Unnamed: 1', u'Unnamed: 0'], axis=1, inplace=True)
    energy = energy[:227]

    # Change column names
    energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']

    # Convert Energy Supply from petajoules to gigajoules
    energy['Energy Supply'] = energy['Energy Supply']*10**6

    # Replace missing data with np.nan
    energy['Energy Supply'].replace(r'\.+', np.nan, inplace=True, regex=True)
    energy['Energy Supply per Capita'].replace(r'\.+', np.nan, inplace=True, regex=True)

    # Replace numbers in country names with null characters
    energy['Country'].replace(r'\d+', '', inplace=True, regex=True)

    # Replace the countries names
    energy['Country'].replace({'Republic of Korea': 'South Korea', 'United States of America': 'United States', 'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom', 'China, Hong Kong Special Administrative Region': 'Hong Kong'}, inplace=True)
    energy['Country'].replace(r'\(.*\)', '', inplace=True, regex=True)
    energy['Country'] = energy['Country'].str.strip(' ')
    #print(energy.head())
    #print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

    # Load the GDP data from world_bank.csv
    GDP = pd.read_csv(directory + r'world_bank.csv', skiprows=4)
    GDP['Country Name'].replace({'Korea, Rep.': 'South Korea', 'Iran, Islamic Rep.': 'Iran', 'Hong Kong SAR, China': 'Hong Kong'}, inplace=True)
    GDP = GDP[['Country Name', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
]
    GDP.columns = ['Country', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    #print(GDP.head())
    #print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

    # Load the Sciamgo Journal dataset
    ScimEn = pd.read_excel(directory + r'scimagojr-3.xlsx')
    #print(ScimEn.head(16))

    # Join the three datasets
    ScimEn_J = ScimEn[:15]
    df = pd.merge(ScimEn_J, energy, how='inner', left_on='Country', right_on='Country')
    df = pd.merge(df, GDP, how='inner', left_on='Country', right_on='Country')
    df.set_index('Country', inplace=True)

    return df
print('ANSWER ONE:\n{}'.format(answer_one()))
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')


def answer_two():
    return 156
print('ANSWER TWO:\n{}'.format(answer_two()))
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')


def answer_three():
    answer = answer_one()[['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']].mean(axis=1)
    answer = answer.sort_values(ascending=False).rename('avgGDP')
    return answer
print('ANSWER THREE:\n{}'.format(answer_three()))
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')


def answer_four():
    Top15 = answer_one()
    country = answer_three().index[5]
    answer = answer_one().loc[country]
    answer = answer['2015'] - answer['2006']
    return answer
print('ANSWER FOUR:\n{}'.format(answer_four()))
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')


def answer_five():
    Top15 = answer_one()
    answer = Top15['Energy Supply per Capita'].mean()
    return answer
print('ANSWER FIVE:\n{}'.format(answer_five()))
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')


def answer_six():
    Top15 = answer_one()
    answer = Top15.sort_values('% Renewable', ascending=False)
    answer= (answer.index[0], answer['% Renewable'][0])
    return(answer)
print('ANSWER SIX:\n{}'.format(answer_six()))
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')


def answer_seven():
    Top15 = answer_one()
    Top15['Cit_Ratio'] = Top15['Self-citations']/Top15['Citations']
    answer = Top15.sort_values('Cit_Ratio', ascending=False).iloc[0]
    answer = (answer.name, answer['Cit_Ratio'])
    return answer
print('ANSWER SEVEN:\n{}'.format(answer_seven()))
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')


def answer_eight():
    Top15 = answer_one()
    Top15['Population'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    answer = Top15['Population'].sort_values(ascending=False).index[0]
    return answer
print('ANSWER EIGHT:\n{}'.format(answer_eight()))
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')


def answer_nine():
    Top15 = answer_one()
    Top15['Population'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    Top15['CitePerPerson'] = Top15['Citable documents']/Top15['Population']
    answer = Top15[['Energy Supply per Capita', 'CitePerPerson']].corr().ix['Energy Supply per Capita', 'CitePerPerson']
    return answer
print('ANSWER NINE:\n{}'.format(answer_nine()))
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')


def answer_ten():
    Top15 = answer_one()
    median = Top15['% Renewable'].median()
    Top15['MedianMarker'] = Top15['% Renewable'] >= median
    Top15['MedianMarker'] = Top15['MedianMarker'].apply(lambda x: 1 if x else 0)
    return Top15['MedianMarker'] 
print('ANSWER TEN:\n{}'.format(answer_ten()))
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')


def answer_eleven():
    Top15 = answer_one()
    ContinentDict = {'China': 'Asia',
                     'United States': 'North America',
                     'Japan': 'Asia',
                     'United Kingdom': 'Europe',
                     'Russian Federation': 'Europe',
                     'Canada': 'North America',
                     'Germany': 'Europe',
                     'India': 'Asia',
                     'France': 'Europe',
                     'South Korea': 'Asia',
                     'Italy': 'Europe',
                     'Spain': 'Europe',
                     'Iran': 'Asia',
                     'Australia': 'Australia',
                     'Brazil': 'South America'}
    Top15['Population'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    answer = Top15.groupby(ContinentDict).Population.agg(['count', 'sum', 'mean', 'std'])
    return answer
print('ANSWER ELEVEN:\n{}'.format(answer_eleven()))
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')


def answer_twelve():
    Top15 = answer_one()
    ContinentDict = {'China': 'Asia',
                     'United States': 'North America',
                     'Japan': 'Asia',
                     'United Kingdom': 'Europe',
                     'Russian Federation': 'Europe',
                     'Canada': 'North America',
                     'Germany': 'Europe',
                     'India': 'Asia',
                     'France': 'Europe',
                     'South Korea': 'Asia',
                     'Italy': 'Europe',
                     'Spain': 'Europe',
                     'Iran': 'Asia',
                     'Australia': 'Australia',
                     'Brazil': 'South America'}
    Top15.reset_index(inplace=True)
    Top15['Continent'] = [ContinentDict[Country] for Country in Top15['Country']]
    Top15['bins'] = pd.cut(Top15['% Renewable'], 5)
    return Top15.groupby(['Continent', 'bins']).size()
print('ANSWER TWELVE:\n{}'.format(answer_twelve()))


def answer_thirteen():
    Top15 = answer_one()
    Top15['PopEst'] = (Top15['Energy Supply']/Top15['Energy Supply per Capita']).astype(float)
    answer = Top15['PopEst'].apply(lambda x: '{:,}'.format(x))
    return answer
print('ANSWER THIRTEEN:\n{}'.format(answer_thirteen()))
