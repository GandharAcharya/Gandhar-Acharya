#Dictionary is Nothing But Key Value Pairs
#D1={}
#print(type(D1))
D2={"Rishav":"Chicken" , "Gandhar":"Beef" , "Aansh":{"B":"Bread Butter And Coffee" , "L":"Burger & Pizza" , "D":"Chicken"}}
print(D2)
D2["Ankit"] = "Crispy Fried Chicken"
del D2["Ankit"]
D3=D2.copy()
del D3["Rishav"]
D2.update({"Gulshan":"Tofee"})
print(D2.keys())
print(D2.items())
