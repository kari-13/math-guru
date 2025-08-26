import json 
with open('math.json','r') as file:
    datab = json.load(file)

while True:
    a=input("enter a math theorem to find it's explanation :")

    if a in datab:
        print(datab[a])

    else : print("theorem not found")

    if a.lower() == 'exit':
        break
