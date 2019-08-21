'''
    რას დაბეჭდავს პროგრამა გაშვების შემდეგ?
'''

def php_programming():
    print("I am still popular")

def python_programming():
    return "I am easy but powerfull"

def golang_programming():
    return "I am super fast"


def question():
    php = php_programming()
    python = python_programming()
    go = golang_programming()

    return php, python, go


answer = question()

print(f"PHP: {answer[0]}\nPython: {answer[1]}\nGo: {answer[2]}")
