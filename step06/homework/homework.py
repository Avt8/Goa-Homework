#2)კომენტარებით ახსენით რა არის კონკადინაცია და მოიყვანეთ მაგალითები
# კონკადინაცია არის კოდში სტრინგების და ცვლადების ერთმანეთში გაერთიანება.
# მაგალითად:
name = "avto "
age = 29
print(name + str(age))
#3)მომხარებელს შემოატანინეთ რიცხვი ერთიდან შვიდამდე, შემოტანილი რიცხვის მიხედვით დაპრინტეთ კვირის დღე.
# (მაგალითად მომხარებელმა შემოიტანა 4 >>> "Thursday")
day = int(input("Enter a number from 1 to 7: "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")    
elif day == 3:
    print("Wednesday")    
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")    
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
    
#4)მომხარებელს შემოატანინეთ ორი რიცხვი, შეინახეთ ორივე ცვლადში. მოახდინეთ მათ შორის შედარება და შედეგი(True or False) 
# გამოიტანეთ ტერმინალში
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 == num2
print(result)

#5)მომხარებელს შემოატანინეთ თავისი ასაკი, თუ ის არის 18 წლის ან ზემოთ დაპრინტეთ "You are adult", 
# სხვა შემთხვევაში დაპრინტეთ "You are kid"
user_age = int(input("Enter your age: "))
if user_age >= 18:
    print("you are adult")
else:
    print("You are kid")


#6)მომხარებელს შემოატანინეთ 4 რიცხვი. შეინახეთ ისინი ცვლადებში და დაბეჭდეთ მათი საშუალო არითმეტიკული
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 =int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
result = (num1 + num2 + num3 + num4) / 4
print(result)


#7)გააკეთეთ 3-3 მაგალითი int() და str() ფუნქციებზე
# მაგალითი 1
num1 = 43
num2 = 45
result = num1 + num2
print(result)
# მაგალითი 2
num1 = 232
num2 = 451
result = str(num1) + str(num2)
print(result)
# მაგალითი 3
num1 = "13"
num2 = "55"
result = int(num1) + int(num2)
print(result)


