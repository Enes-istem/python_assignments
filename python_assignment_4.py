while True :
    enter = int(input("bir sayı giriniz : "))
    if (enter == 2) or (enter == 1):
        print("asal sayı. ")
        
    elif  (enter %2 ==0) or (enter %3 == 0) or (enter %5 == 0) or (enter %7 ==0):
        print("asal sayı değil.")
        
    else:
        print("asal sayı")
        break
    