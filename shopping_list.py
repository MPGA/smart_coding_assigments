ica_prices = {
    'apple' :0.60,
    'banana':0.70,
    'eggs':0.40,
    'lentils':30,
    'white bread':20,
    'milk':15
}

things_i_need = {
    'apple':5,
    'banana':4,
    'eggs':12,
    'lentils':2,
    'white bread':1,
    'milk':1
}
my_bill=0

for key,value in things_i_need.items():
        for key1,value1 in ica_prices.items():
           if key == key1:
              print(key+ ' ' +str(value)+" "+'x'+" "+str(value1))

my_bill = value * value1 + my_bill
  

#print("total:"+str(my_bill))

total = sum(ica_prices[items]* things_i_need[items]
for items in things_i_need)

print ("total is: " +str (total)+" krones")





    
              
        


