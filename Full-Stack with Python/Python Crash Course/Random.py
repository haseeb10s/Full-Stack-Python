import random
for i in range(3):
    print(random.random())
    print(random.randint(10, 20))


members = ['John', 'Roman', 'CM', 'Seth']    
leader = random.choice(members)
print(leader)