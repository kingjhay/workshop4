# ex 1
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.pop("model")
print(thisdict)

# ex 2
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.popitem()
print(thisdict)

# ex 3
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
del thisdict["model"]
print(thisdict)

# ex 4
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.clear()
print(thisdict)