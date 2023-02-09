# # # from  collections import Counter
# # #
# # # sample_string = 'aaaababbbbbccddcccdddcddeeeeeeccee'
# # # my_counter = Counter(sample_string)  # возвращает словарь
# # # print(my_counter.most_common())
# # #
# # # print(type(my_counter))
# #
# # #print(my_counter['d'])
# #
# # # from collections import namedtuple #именной кортедж
# # # point = namedtuple('Point','x,y')
# # #
# # # pt=point(-1,2)
# # # print(pt)
# # # print(pt.x)
# # # print(pt.y)
# #
# # from collections import OrderedDict
# #
# # oder_dict=OrderedDict()
# # oder_dict['name']='Jack'
# # oder_dict['Surname']='Smith'
# #
# # print(oder_dict)
# #
# # from collections import defaultdict
# # my_def = defaultdict(int) #тип данных который будет хранить
# # my_def['a'] = 1
# # my_def['b'] = 2
# # print(my_def['c'])
#
# from collections import deque
# d = deque()
# d.append(1)
# d.append(2)
# d.appendleft(5) #добавить слева
# d.popleft() #удаляет слева
# x=d.popleft() #удаляет слева
# d.extend([7,8,9]) # добавление спсика
# d.extendleft([0,1,2]) # добавление слева спсика
# print(d)
# d.rotate() #разворот списка. Можно ставить номер
# d.rotate(3) #разворот списка. Можно ставить номер
# print(d)
