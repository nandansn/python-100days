def greetings(func):
    def wish():
        func()
        print('today quote: all is well')

    return wish


@greetings
def good_morning():
    print('good morning')


good_morning()


## with params

def salary_incr(func):
    
    def incr():
        print('incr')
        ##salary = salary + ((salary * kwargs["per"]) / 100)
        func()
    return incr


@salary_incr
def increase_Salary():
    print('hello')

increase_Salary()

print(__name__)