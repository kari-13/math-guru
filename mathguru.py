import json 
import os
json_path='Math.json'
with open(json_path,'r') as file:
    datab = json.load(file)

while True:
    a=input("enter a math theorem to find it's explanation :")
    keys = a.strip().split()
    result = datab
    try:
        for keys in keys:
            result=result[keys]
        print(result)
    except Exception:print("theorem not found")
    
   

    if a.lower() == 'exit':
        print("thank you for using my app :) \n  @kari_13")
        break
