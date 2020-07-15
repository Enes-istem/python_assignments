list_one =[]
count = 0
sonuc = 0
for i in range(-1,9):
    if i <=1:
        count = count +abs(i)
        list_one.append(count)
    elif i >=2:
        count = count + list_one[i-1]
        list_one.append(count)
    
    
print(list_one)        