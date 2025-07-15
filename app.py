import json

data = {
    "name" : "komeyl",
    "age" : 9
}

with open("user.json" , "w") as f :
    json.dump(data, f)
    
with open("user.json" , "r") as f:
    user = json.load(f)
    
    
print(user)