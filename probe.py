

RMB_f = 10 * 60 + 25/4 * 170 - 5 * 19 - 161
print("femeie", RMB_f)
kg = 60

'''
PAL = {
  "1": "Sedentar",
  "2": "Activ Moderat",
  "3": "Activ viguros",
  "4": "Extrem de activ"
}
'''

user_pal = int(input("Va rugam sa alegeti nivelul dvs de activitate fizica:\n 1: Sedentar, \n 2: Activ Moderat, \n 3: Activ viguros, \n 4: Extrem de activ \n"))

if user_pal == 1:
    total = int(RMB_f*(155/100))
    print("totalul de kcal este: ", total)
    prot = (13/10) * kg
    print("Proteine necesare: ", prot)
    carbs = (45/100) * total
    print("Carbohidratii necesari: ", carbs)
    fats = (20/100) * total
    print("Grasimi necesare: ", fats)
        
elif user_pal == 2:
    print(int(RMB_f*(185/100)))
    
elif user_pal == 3:
    print(int(RMB_f*(22/10)))
    
elif user_pal == 4:
    print(int(RMB_f*(24/10)))
    
else:
    print("don't mess with me")