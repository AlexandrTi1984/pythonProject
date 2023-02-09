# answer_question() - function to take one question as an argument
# returns user picked answer
import json


def answer_question(question):
    while True:
        print(f'1.{question}[0] 2.{question}[1],)\n'
              f'3.{question}[2] 4.{question}[3],)\n')
        user_choice=input('Введите ответ')
        if user_choice.lower()=='exit':
            print('Godbay')
            quit()
        if user_choice in '1234':
            return question[int(user_choice)-1] # возвращаем индекс
        else:
            print('не верній вібор, попробуй еще. Или нажми exit')


# check_answer() - function that takes right answer and user answer
# Compares them and returns True or False
def check_answer(answer, user_answer):
    if user_answer==answer:
        return True
    return False


# start_quiz() - function starr and quiz
def start_quiz(topic, data):
    quiz = data[topic]
    score = 0
    for question in quiz.values():
        print(question.get('question'))
        user_answer = answer_question(question.get('options'))
#       to complete
        print(user_answer)
        if check_answer(question.get('answer'),user_answer):
            score+=1
    print(f'You answer {score}')


# main() - function to control quiz process
def main(data):
    print('Hello. Welcome to our quiz.')
    print(f'You can choose from {len(data.keys())} topics')


    for topic in data.keys():
        print('*', topic)
    while True:
        quiz_topic = input('Type topic name to continue or "exit" to quit. ->')
        if quiz_topic.lower() == 'exit':
            print('Good bye')
            quit()
        if quiz_topic.lower() in data.keys():
            start_quiz(quiz_topic.lower(), data)
             # if input('Еще раз').lower()=='y':
             #     main(data)
            break
        else:
            print(f'There`s no {quiz_topic}.')

with open('quiz.json', 'r', encoding='utf8') as file:
    quiz_data = json.load(file).get('quiz')

main(quiz_data)
