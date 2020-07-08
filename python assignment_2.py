age = input("Are you a cigarette addict older than 75 years old? : ")
if age == "yes":
    age = True
else:
    age = False
chronic = input("Do you have a severe chronic disease? : ")
if chronic =="yes":
    chronic = True
else:
    chronic = False
immune = input("Is your immune system too weak? : ")
if immune == "yes":
    immune = True
else:
    immune = False
risk =  (age) and (chronic) and (immune)

if risk == False:
    print("You are not in risky group")
else:
    print("You are in risky group")