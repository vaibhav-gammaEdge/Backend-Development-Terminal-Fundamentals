cache={}

data={
    "id1":{
        "name":"vaibhav",
        "age":"22"
    }
    ,
     "id2":{
        "name":"ujjwal",
        "age":"23"
    }
}

def store(userid):
    if(cache.get(userid)):
        return cache[userid]


    cache[userid]=data[userid]  


print(store("id1"))
print(cache)