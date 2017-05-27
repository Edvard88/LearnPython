user_info={
    'first_name':input("Введите свое имя: "),
    'second_name':input("Введите свою фамилию: ")
    }

#first_name=input("Введите свое имя: ")
#second_name=input("Введите свою фамилию: ")

#user_info['first_name']=first_name
#user_info['second_name']=second_name

print(user_info)
print("Имя пользователя {}".format(user_info.get('first_name')))
print("Фамилия пользователя {}".format(user_info.get('second_name')))



