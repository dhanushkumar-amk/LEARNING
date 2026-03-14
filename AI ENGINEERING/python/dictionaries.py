deatils = {
    "name" : "dhanushkumar",
    "age" : 21,
    "address" : {
        "city" : "coimbatore",
        "state" : "Tamil nadu"
    }
}

#  accessing element
print(deatils["name"])
print(deatils["address"]["city"])

#  adding element
deatils["age"] = 22
print(deatils)

#  removing element
deatils.pop("age")
print(deatils)

# length of the dictionary
print(len(deatils))

# get keys
print(deatils.keys())


