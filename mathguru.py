import json 
import os
json_path='Math.json'
with open(json_path,'r') as file:
    datab = json.load(file)

while True:
mac
    a=input("enter a math theorem to find it's explantion :")

    if a in datab:
        print(datab[a])

    else : print("theorem not found")
=======
    a=input("enter a math theorem to find it's explanation :")
    keys = a.strip().split()
    result = datab
    try:
        for keys in keys:
            result=result[keys]
        print(result)
    except Exception:print("theorem not found")
    
  main

    if a.lower() == 'exit':
        print("thank you for using my app :) \n  @kari_13")
        break
