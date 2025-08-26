import json 
import os
json_path=os.path.join(os.path.dirname(__file__),'math.json')
with open('json_path','r') as file:
    datab = json.load(file)

while True:
    a=input("enter a math theorem to find it's explanation :")

    if a in datab:
        print(datab[a])

    else : print("theorem not found")

    if a.lower() == 'exit':
        break
