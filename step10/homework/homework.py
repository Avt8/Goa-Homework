#2) მომხარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ, რამდენჯერ შედის შემოტანილი რიცხვი 100-ში.
#  გააკეთეთ ყველაზე მოკლე გზით(ამისათვის გამოიყენეთ გაყოფის სწორი ტიპი)

num = int(input("Enter a number: "))
if 100 / num:
  num = 100 // num
  print(int(num))

#3)while ციკლის გამოყენებით გამოიტანეთ 1-დან 20-მდე ყველა კენტი
#  რიცხვის ჯამი

sum_odd = 0
num = 1

while num <= 20:
    if num % 2 != 0:
        sum_odd = sum_odd + num
    num = num + 1
print(sum_odd)


#4) მომხარებელს შემოატანინეთ ორი რიცხვი და დაბეჭდეთ ის, 
# რომელიც არის მეტი. თუ ორივე რიცხვი ტოლია დაბეჭდეთ 
# "Both numbers are equal"

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
if num1 > num2:
 print(num1)
elif num1 < num2:
 print(num2)
else:
 print("both number are equal")

#5)მომხარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ შემოტანილი რიცხვის
#  ფაქტორიალი
# (დასერჩეთ რა არის ფაქტორიალი)
import math
num = int(input("Enter a number: "))
print(f"{num}-n! is: {math.factorial(num)}")


#6)მომხარებელს შემოატანინეთ რიცხვი და შეინახეთ ის ცვლადში. 
# შემდეგ დაბეჭდეთ შემოტანილი რიცხვის ჩათვლით ყველა რიცხვის კვადრატის ჯამი

num = int(input("Enter your number: "))
num = num * num
print(num)


#7)თამაში "რიცხვის გამოცნობა". შექმენით ცვლადი და შეინახეთ რომელიმე რიცხვი 1-დან 20-ის 
# ჩათვლით(ეს იქნება ჩაფიქრებული რიცხვი). გამოიყენეთ while loop-ი და მომხარებელს
#  შემოატანინეთ რიცხვი იქამდე სანამ არ გამოიცნობს მას. თუ მომხარებლის მიერ შემოტანილი
#  რიცხვი მეტია ჩაფიქრებულზე, დაპრინტეთ To high, თუ ნაკლებია Too low, 
#ხოლო იმ შემთხვევაში თუ მომხარებელი გამოიცნობს რიცხვს დაპრინტეთ "You win"

num = 8
while True:
 user_num = int(input("Guess a number: "))
 if user_num > num:
        print("To high")
 elif user_num < num:
        print("To low")
 elif user_num == num:
        print("You WIN! right number is " + str(num))
        break

