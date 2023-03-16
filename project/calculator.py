# display calc logo
# get the first number
# display the operaions
# get the next number
# do the calculation
# display the result
# check to continue for next calculation


logo = '''

           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                              

'''

def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b


operation_map = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}

def display_logo():
    print(logo)
display_logo()

def display_operations(): 
    for key in operation_map:
        print(key)


def calc():
    f_number = float(input("enter first  number: "))
    display_operations()
    operation = input("choose operation: ")
    s_number = float(input("enter second number: "))
    
    ops = operation_map.get(operation)
    result = ops(f_number,s_number)
    print("{} {} {} = {}".format(f_number,operation,s_number,result))

yes_or_no = {
    "cond": "YES"
}

while yes_or_no.get("cond").upper() == "YES":
  calc()
  value = input("Want to continue? yes or no: ")
  yes_or_no["cond"] = value