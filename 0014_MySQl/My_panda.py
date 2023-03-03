import pandas as pd
import mysql.connector
# #df=pd.read_csv('2019.csv',skiprows=1) # пропуск рядов при чтении
# df=pd.read_csv('2019.csv',header=0) # пропуск рядов при чтении
# print(df)

# df=pd.read_csv('test.csv',header=None,names=['Name','DoB','City']) # Добавить название полей
# print(df)

# df=pd.read_csv('test.csv',header=None,names=['Name','DoB','City'],nrows=2) # Добавить название полей
# df.to_csv('my.csv',index=False,header=False,columns=['Name','City'])
# print(df)
# print(df.columns)

# pd.set_option('display.max_rows',160) # количество отображаеміх строк
# pd.set_option('display.max_columns',9) # количество отображаеміх столбцов

#df=pd.read_csv('2019.csv')

# people={
#     'name':['Bob','Sara'],
#     'Lastname':['Smith','Wik'],
#     'email':['1@gmail.com','2@mail.ru']
# }
# df=pd.DataFrame(people)
# #print(df['name'][0])
# print(df[['name','email']]) #два столбца как список подаем

#print(df.iloc[[2,10,8]])  #Если перечисление еще ставим []

# print(df.iloc[0:5,[1,3,6]]) #Если перечисление еще ставим [] Работает с индексами строк и столбцов
# print(df.loc[0:5,'Country or region':'Freedom to make life choices']) #Включительно последнее значение
#
# print(df.loc[0,'Country or region']) #Это строка,строка 0 столбец Кантри

# print(df.shape) # инфо 156 рядов и 9 столбцов- Кортеж
# print(df.shape[0]) # инфо 156 рядов и 9 столбцов- Кортеж
# print(df.shape[1]) # инфо 156 рядов и 9 столбцов- Кортеж

#print(df['Country or region'].value_counts()) #количесвто стран


# print(df.head(3)) # первіе 5 строчек Дата Фрейм
# print(df.tail(5)) # последние 5 строчек  Дата Фрейм

# my_connection=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='@Evp12345',
#     database='sakila'
# )
#
# df=pd.read_sql_query('Select * From actor',my_connection)
#
# print(df)

df=pd.read_csv('2019.csv')

# df['Total']=df['GDP per capita']*1000 #Добавили новой столбец, ГДП умножили на 1000
# #print(df)
#
#
#
# df.insert(loc=0,column='My_col',value=(df['GDP per capita']*6000))
# df=df.drop(columns=['Total','My_col']) #удалить столбці
# print(df)

#print(df.loc[df['Country or region'].str.contains('ong|E')]) #регулярное віражение. Поиск

print(df.groupby('Country or region').count())

a=df.nlargest(5,'Overall rank')
b=df.nsmallest(5,'Overall rank')
df2=pd.read_csv('test.csv')

# print(a)
# print(b)

print(pd.concat([a,b,df2])) #обьединение разніх ДатаФрейм






#print(df.loc[df['Country or region'] == 'Estonia']) #поиск по полю страна или по ячейки

#print(df.describe()) # статистика
#print(df.memory_usage(deep=True)) #сколько памяти занимает в байтах

#print(df.sort_values(['Social support','GDP per capita'],ascending=[True,False])['Country or region']) # сортировка, одни по возратсанию и по убіванию Country or region - критерий вівода
#print(df.dtypes)



# for index, row in df.iterrows():
#     print(index)
#     print(row)
#     print(row['Country or region'])