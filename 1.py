'''
    რას დაბეჭდავს პროგრამა გაშვების შემდეგ?
'''

def hi():
    print("Hi, from function")


class Hi_1:
    print("Hi, from Hi_1 class")


class Hi_2:
    def __init__(self):
        print("Hi, from Hi_2 class")


hi()
Hi_1()
Hi_2()