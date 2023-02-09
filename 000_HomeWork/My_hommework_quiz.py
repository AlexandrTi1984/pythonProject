import json

def answer_qustion (question): # принимает ответ
    pass

def chek_answer(answer, user_answer): #сравниваем ответ пользователя с нашим
    pass

def start_quiz(topic,data): # запуск 5 вопросов
    quiz=data[topic]
    score=0

    for question in quiz.values():
        print(question.get('question'))
        user_answer=answer_qustion(question.get('options'))
        print(user_answer)


def main (data):
    print('Hello')
  #  print(f'Вібирите из {len(data.keys())} topics')

    for topic in data.keys():
        print('*',topic)
    while True:
        quize_topic=input('выбирите тему или выход')
        if quize_topic.lower()=='exit':
            print('Гудбай')
            quit()
        if quize_topic.lower() in data.keys():
            start_quiz()
            pass





with open('quiz.json','r',encoding='UTF8') as file:
    quize_data=json.load(file).get('quize')
main(quize_data)