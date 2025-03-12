#1) მოხარებელს შეეკითხეთ მისი სახელი,გვარი ასაკი და იმეილი, შემდეგ კი შემოტანილი მნიშვნელობები დაბეჭდეთ ტერმინალში.
#  გამოიყენეთ ეტიკეტი, რომ მიანიშნოთ მომხარებელს თუ რა უნდა შემოიტანოს კონკრეტულ შესაყვან ველში.
name = input("Enter your name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
email = input("Enter your email: ")

#2) მომხარებელს შემოატანინეთ ორი რიცხვი და გამოიყენეთ ყველა არითმეტიკული ოპერაცია ამ ორ რიცხვს შორის.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 + num2, num1 - num2, num1 * num2, num1 / num2
print(result)

#3) კომენტარებით ახსენით თუ რა არის input-ი და output-ი, ასევე რისთვის გამოიყენება ისინი
#ინპუტი არის ფუნქცია რომლის საშუალებით შეგვყავს მონაცემი, აუთპუთ გვიბრუნებს შეყვანილ მონაცემს.

#4) შექმენით კალკულატორის პროგრამა სადაც მომხარებელი შემოიტანს ორ რიცხვს და 4 არითმეტიკული ოპერაციიდან ერთერთს. 
# შეასრულეთ ამ ორ რიცხვს შორის არჩეული არითმეტიკული ოპერაცია და დაბეჭდეთ შედეგი.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation: ")
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)