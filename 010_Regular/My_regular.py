import re
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa Haa HaHaa HaHA
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
809-555-1234
809-555-1234
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
Ms Santa-Fe
Ms R123
abc_
www.ex.com
mall wall bball tall hall khall
xall fall sallo
'''
#
sentence = 'Start a sentence and then bring it to an end'
# #pattern=re.compile(r'[af\-t]')
# pattern=re.compile(r'M(r|s|rs)\.? [A-Za-z-]*\b')
# #pattern=re.compile(r'\d{3,4}') # берет максимум - т.е 4 цифрыpattern=re.compile(r'\d{3}.\d{3}.\d{4}') #в скобках кол-во цифр
# #pattern=re.compile(r'8[0]00.\d\d\d.\d\d\d') #ищется конкретный символ точка
# # print(pattern)
# # print(type(pattern))
#
# matches = pattern.finditer(text_to_search)
# # print(matches)
# # print(type(matches))
#
# for match in matches:
#     print(match)
#     # print(match.start()) # nachalo
#     # print(match.end()) #konec
#     # print(match.group()) #stroka
#
#
#    # print(type(match))
# #print(text_to_search[264:267])
pattern=re.compile(r'\d\d\d')
mathes=pattern.findall(text_to_search) #в список
print(mathes)

print(re.findall(r'\d\d\d',text_to_search)) #в принт віводим
#mathes=pattern.fullmatch(r'\nabc')
#mathes=pattern.match(r'\nabc')

pattern=re.compile(r' ')
mathes = pattern.split(sentence)
print(mathes)

pattern=re.compile(r'\d\d\d')
mathes = pattern.search(text_to_search,2,367) # только первое совпадение
print(mathes)

mathes = pattern.subn('*',text_to_search,3)
print(mathes)

pattern=re.compile(r'^a',re.MULTILINE) # используют флаги
mathes = pattern.finditer(text_to_search)
for match in mathes:
    print(match)