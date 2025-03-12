#2) შექმენით ცვლადები და შეინახეთ სხვადასხვა მონაცემთა ტიპის მნიშვნელობები. შემდეგ შეამოწმეთ თითოეული ცვლადის მონაცემთა ტიპი.

name = "avto"
age = 25
my_salary = 1150.50
married = True
print(type(name), type(age), type(my_salary), type(married))  



#3) მომხარებელს შემოატანინეთ რიცხვი და შეამოწმეთ მისი ტიპი, ისე რომ დაგიბრუნდეთ integer
num = int(input("Enter a number: "))
print(type(num))

#4) გააკეთეთ 5-5 მაგალთი შედარების ოპერატორებზე
num1 = 5
num2 = 5
print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)


#5) დაბეჭდეთ ყველა შესაძლო ვარიანტი and და or ოპერატორებზე
num1 = 5
num2 = 24
result = num2 == num1 and num2 >= num1
print(result)

x = 14
y = 54
result = x == y or x < y

# 6)მომხარებელს შემოატანინეთ მისი ასაკი, როგორც სტრინგი და დაბეჭდეთ მისი ტიპი. 
# შემდეგ შეუცვალეთ მას მონაცემთა ტიპი ჯერ integer-ად, შემდეგ float-ად (ყოველ გარდაქმნაზე დაბეჭდეთ შედეგი)

age = input("Enter your age: ")
print(type(age))
print(int(age))
print(float(age))
print(bool(age))

#7) მომხარებელს შემოატანინეთ მისი საყვარელი რიცხვი და გაიგეთ არის თუ არა ის ლუწი

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")    
#8) მომხარებელს შემოატანინეთ მისი ასაკი და სახელი, შემდეგ შეამოწმეთ არის თუ არა ის სრულწლოვანი და უდრის 
# თუ არა მისი სახელი თქვენს სახელს.
age = int(input("Enter your age: "))
name = input("Enter your name: ")
if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")
if name == "Avto":
    print("Ouer name is same")
else:
    print("Your name is different")