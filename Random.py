import random

random_number = random.integer(1,10)

print(random_number)

random_float = random.uniform(0,1)

print(random_float)

cara_ou_coroa = random.randint(0,1)

if(cara_ou_coroa == 0):
    print("cara")

else:
    print("coroa")
