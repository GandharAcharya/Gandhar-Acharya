
Numbers=[1,2,3,4,5,6,7,8,9,0]
print(Numbers[::3])
print(len(Numbers))
print(max(Numbers))
print(min(Numbers))

Numbers.insert(2,1)
Numbers.remove(3)
Numbers.pop()
Numbers[1]=98

#Mutable-Can Change (This is a Simple Line, Not A Code)
#Immutable-Cannot Change (This is a Simple Line, Not A Code)
tp=(1,2,3)
print(tp)
print(Numbers)

#This Is a Traditional Meathod Of Swapping Two Numbers Down Below (This is a Simple Line, Not A Code)
a=1
b=2
temp=a
a=b
b=temp

#This is a Mordern Meathod Of Swapping Two Numbers Down Below (This is a Simple Line, Not A Code)
a=1
b=2
a,b=b,a
print(a,b)
