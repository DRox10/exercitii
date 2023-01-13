#EXERCITIUL CU CALCULATORUL
#PART I
'''
x = int(input("Enter first operand: "))
y = int(input("Enter second operand: "))
'''
#add = (x+y)
#sub = int(x-y)
#mul = (x*y)
#div = (x/y)
'''

result = input("Choose operation(add, sub, mul, div): ")
if result == "add":
    print(x+y)
elif result == "sub":
    print(x-y)
elif result == "mul":
    print(x*y)
elif result == "div":
    print(x/y)
else:
    print("operation not available")
'''

#PART II

language1 = "eng"
language2 = "it"
language3 = "ro"
language = ["it" , "ger" , "ro" ]
user = input("select the language: ")
#eng
while  user == "eng":
    print("ok")
    if user != "eng":
        continue
    x = int(input("Enter first operand: "))
    y = int(input("Enter second operand: "))
    result = input("Choose operation(add, sub, mul, div): ")
    if result == "add":
        print(x+y)
    elif result == "sub":
        print(x-y)
    elif result == "mul":
        print(x*y)
    elif result == "div":
        print(x/y)
    else:
        print("operation not available")

#it
while  user == "it":
    print("ok")
    if user != "it":
        continue
    x = int(input("Metti il primo numero: "))
    y = int(input("Metti il secondo numero: "))
    result = input("Scegli l'operazione(add, sub, mul, div): ")
    if result == "add":
        print(x+y)
    elif result == "sub":
        print(x-y)
    elif result == "mul":
        print(x*y)
    elif result == "div":
        print(x/y)
    else:
        print("L\'operatione incorecta")

#ro
while  user == "ro":
    print("ok")
    if user != "ro":
        continue
    x = int(input("Introduceti primul numar: "))
    y = int(input("introduceti al doilea numar: "))
    result = input("alegeti operatia(add, sub, mul, div): ")
    if result == "add":
        print(x+y)
    elif result == "sub":
        print(x-y)
    elif result == "mul":
        print(x*y)
    elif result == "div":
        print(x/y)
    else:
        print("Operatia nu este disponibila")
    

    
