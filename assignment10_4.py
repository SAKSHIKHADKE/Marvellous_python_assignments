from functools import reduce

checkeven=lambda x:x%2==0
   
square=lambda x: x**2
    
sum=lambda x,y:x+y
   

data=[5,2,3,4,3,4,1,2,8,10]
print("input data :",data)

fdata=list(filter(checkeven,data))
print("filter output :",fdata)

mdata=list(map(square,data))
print("map output :",mdata)

rdata=reduce(sum,data)
print("reduce output :",rdata)