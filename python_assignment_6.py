empty_list = []
empty_list2 = []
for i in range(100):
    if (i==2) or (i ==3) or (i ==5) or (i == 7):
        empty_list.append(i)
    elif (i %2 ==0) or (i %3 ==0) or (i % 5 ==0) or (i % 7 == 0) or (i==1):
        empty_list2.append(i)
      
       
    else :
        empty_list.append(i)
print(empty_list)    