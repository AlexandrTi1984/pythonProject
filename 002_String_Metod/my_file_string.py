string_sample1='Hello world world'
               #0123456789  -2 -1
string_sample2='first letteR is LowErcase'
string_sample3=' *   *   * extra  *   *   * whitespaces  *     *   *'
german_sample='der Fluß'

#[Start:End:Step] последний индекс не включен. то есть можно добавит 1. Если нет финишного - то будет от начала до конца
print(string_sample1[-1])
print(string_sample1[6:11])
print(string_sample1[6:11])
print(string_sample1[::-1]) # в обратном направлении
print(len(string_sample1)) #всего 17, но длина 16.т.к начинается с 0
print(string_sample1.upper()) # приводит к верхнему регистру
#string_sample1=string_sample1.upper()
print(german_sample.lower())
print(german_sample.casefold()) #попробует конвертировать в читаемый
print(string_sample1.isupper()) # проверка все ли верхний регистр
print(string_sample1.islower())# проверка все ли нижний регистр
print(string_sample2.capitalize()) #типа делает первую букву большой
print(string_sample2.title()) #типа делает первую букву каждого слова большой остальніе маленькие
print(string_sample3.strip()) # удаляет лишние прбелі с начала и с конца строки
print(string_sample3.strip('* ')) # удаляет лишние прбелі с начала и с конца строки
#print(string_sample3.rstrip('* ')) # удаляет лишние прбелі с права
#print(string_sample3.lstrip('* ')) # удаляет лишние прбелі с слева
print(string_sample1.replace('world','planet',1).replace('planet','круг')) # ищет world На планет и меняет слово count раз
print(string_sample1.split()) # разделение слов по принципу пробел \ слеш\кавычка
# a,b,c =string_sample1.split()
# print(a)
# print(b)
# print(c)
print(string_sample1.count("l")) #количество слов в тексте
print(string_sample1.find("Hello")) #позиция слова в тексте первое совпадение
print('world' in string_sample1) # есть ли совпадение в строке