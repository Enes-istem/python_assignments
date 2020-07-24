num = int(input("Lütfen bir sayı giriniz : "))

def leap_year(num):
    return (" {} is a leap year.").format(num) if num % 400 == 0 else  (" {} is not a leap year.").format(num) 
print(leap_year(num))