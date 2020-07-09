number1 = int(input("Lütfen bir sayı giriniz : "))
number1_list =list(str(number1))
i = 0
toplam = 0




while i < len(number1_list) and (number1 > 0):
    toplam += int(number1_list[int(i)])**(int(len(number1_list)))
    i = i + 1
if (number1 > 0) and (number1 == toplam):
    print("{} sayısı Armstrong bir sayıdır.".format(number1))
elif (number1 == 0) or (number1 <0):
    print("{} sayısı 0 veya negatif sayı olduğundan Armstrong bir sayı değildir.".format(number1))
else:
    print("{} sayısı Armstrong bir sayı değldir.".format(number1))
