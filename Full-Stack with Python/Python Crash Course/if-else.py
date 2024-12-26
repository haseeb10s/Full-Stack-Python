temp = 35
if temp > 30:
    print("It's a hot day ")
    print('Drink plenty of water ')
elif temp > 20: # 20, 30 
    print("It's a nice day ")    
elif temp > 10: # 20, 30 
    print("It's a bit cold ")   
else:
    print("It's cold")     
print('Done')    

# ex:1
weight = int(input("Enter your weigh: "))
unit = input("(K)g or (L)bs")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kg: " + str(converted))    