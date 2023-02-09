import csv
with open('2019.csv','r',encoding='UTF8') as file:
    happiness_data=list(csv.reader(file))
    # next(happiness_data)
    # happiness_data=list(happiness_data)
analysis_data=[]
for line in happiness_data:
    analysis_data.append([line[3],line[1]]) #'сортирует по первую ключу'
#print(analysis_data)
analysis_data.sort(reverse=True)
#print(analysis_data)

result=[]

for line in analysis_data:
     if analysis_data.index(line)>9:
         break
     result.append(line)

print(result)







