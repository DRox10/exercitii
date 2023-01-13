#CEL MAI MIC NUMAR
'''l = [3, 44, -7, 11, 1084, 32321, 78, 99]

m = min(l)
M = max(l)
print("minim: ", m, "maxim", M )
'''

#VERIFICA DACA EXISTA NR INTREGI IN LISTA
'''x = 13
lst = [4, 5, 10, 8, 9]

def check_if_x_exist(x, lst):
    return x in lst
print(x)


alta varianta:
if x in lst and x%2==0:
        return True
    else:
        return False

print(check_if_x_exist(x, lst))'''

#EXERCITIUL CU PALINDROM/ANAGRAM
'''s1 = "caiac"
s2 = "caiac"

def are_palindrom(s1,s2):
    return s1 == s2[::-1]

def are_anagram(s1, s2):
    return set(s1) == set(s2)'''

#EXERCITIUL CU DESENUL
'''
def render(x, y):
    print("#"*x)
    for i in range(y-2):
        print("#"+" "*(x-2)+"#")
    print("#"*x)
render(10, 10)
'''

#FUNCTIA RECURSIVA
'''def f(x):
    print(x)
    if x > -3:
        f(x-1)

f(10)
'''

#EXERCITIU CU FUNCTIA RECURSIVA
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1
print(factorial(8))








