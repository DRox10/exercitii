language1 = "it"
language2 = "eng"
language3 = "ro"
language = ["it" , "ger" , "ro" ]
user = input("select the language: eng, it, ro ")
while  user == "eng":
    print("True")
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
        
while  user == "it":
    print("True")
    x = int(input("Metti il primo numero: "))
    y = int(input("Metti il secondo numero: "))
    result = input("Alegi una operazione(add, sub, mul, div): ")
    if result == "add":
        print(x+y)
    elif result == "sub":
        print(x-y)
    elif result == "mul":
        print(x*y)
    elif result == "div":
        print(x/y)
    else:
        print("L'operazione non e disponibile")
        
        while  user == "ro":
            print("True")
    x = int(input("Introduceti primul numar: "))
    y = int(input("Introduceti al doilea numar: "))
    result = input("alegeti o operazie(add, sub, mul, div): ")
    if result == "add":
        print(x+y)
    elif result == "sub":
        print(x-y)
    elif result == "mul":
        print(x*y)
    elif result == "div":
        print(x/y)
    else:
        print("operatia nu este disponibila")

