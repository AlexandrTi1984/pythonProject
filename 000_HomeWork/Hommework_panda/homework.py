'''
Домашнее задание:
Для опроса на Stack Overflow (https://insights.stackoverflow.com/survey)
Написать программу, которая по выбору пользователя делает следующее:
1. Выводит данные о том сколько программистов является профессионалами и сколько хобби программистами. (столбец 'Hobbyist')
2. Выводит средний, максимальный и минимальный возраст (столбец 'Age') программистов
3. Выводит таблицу со странами (столбец 'Country'). Группирует, считает кол-во и выводит в порядке убывания.
4. Выводит таблицу с валютами (столбец 'CurrencyDesc'). Группирует и выводит в порядке убывания
'''

# https://tproger.ru/digest/data-science-python/#1

import pandas as pd

pd.set_option('display.max_rows',200) # количество отображаеміх строк
pd.set_option('display.max_columns',1) # количество отображаеміх столбцов
df=pd.read_csv('survey_results_public.csv')

#==========1====================
pd.set_option('display.max_rows',1)
df01=df.loc[df['Hobbyist'] == 'Yes']
df02=df01.loc[df01['MainBranch'] == 'I am a developer by profession']
print(df02.count())

#==============2=================
pd.set_option('display.max_columns',4) # количество отображаеміх столбцов
df10=df.loc[df['Age'] != 'NA']
df09=df10.loc[df10['MainBranch'] == 'I am a developer by profession']

print(df09.groupby('MainBranch').min())
print(df09.groupby('MainBranch').max())
print(df09.groupby('MainBranch').mean())


#========= 3 ===============
pd.set_option('display.max_rows',200)
pd.set_option('display.max_columns',6)
print(df['Country'].value_counts(ascending=False)) #количесвто стран
#========= 4 ===============
print(df['CurrencyDesc'].value_counts(ascending=False)) #количесвто валют