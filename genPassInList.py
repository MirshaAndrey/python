import random

numberpassword = 1000
lenpass = 100

for c in range (numberpassword):
    pas = ''
    for x in range(lenpass): #Количество символов (16)
        pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    pas=pas + '\n'
    file = open("pass.txt", "a")
    file.write(pas)
    file.close()



