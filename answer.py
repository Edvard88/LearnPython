#question=input('Введите answer: ')
import time

def get_answer(question):
	
	answer={'привет':'И тебе привет',
			'как дела':'Лучше всех',
			'пока':'Увидимся'
			}

	return answer.get(question.lower())

#print(get_answer('привет'))
#print(get_answer('ПриВеТ'))
#print(get_answer('как дела'))
#print(get_answer('пока'))

while(True) :
	question=input('Введите answer: ')
	time.sleep(2)
	print('Ответ: ',get_answer(question), '\n')

	


