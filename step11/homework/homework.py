#1) გააიაზრეთ ეს კოდი, დაკომენტარეთ თითოეული კოდი

secret_pass = "luka1234" # შეიქმნა ცვლადი სადაც შევინახეთ პაროლი
user_pass = ''           # მომხარებლის მიერ შემოტანილი პაროლი

tries = 3                # მცდელობა

while tries > 0 and user_pass != secret_pass: # შედარების ოპერატორებით ვადარებთ მცდელობას, მომხარებლის პაროლს და ჩვენს მიერ შექმნილ პაროლს
    user_pass = input("Enter your password (you have " + str(tries) + " tries left): ") # მომხარებელს შემოაქვს პაროლი
    tries = tries - 1     # მცდელობების ოდენობა


    if user_pass == secret_pass: # მომხარებლის პაროლი თუ არის ტოლი ჩაფიქრებული პაროლის
        print("Access granted!")
    elif tries == 0:
        print("You've reached the maximum number of tries. Access denied!")
    else:
        print("Access denied! Try again.")

#2) დაითვალეთ რამდენი ლუწი რიცხვია 1-დან 50-ის ჩათვლით(გამოიყენეთ for loop-ი)
sum = 0
for i in range(1,51):
    if i % 2 == 0:
        sum = sum + 1
        print(sum)


#3) დაბეჭდეთ 1-დან 100-მდე ყველა ლუწი რიცხვის საშუალო არითმეტიკული. გამოიყენეთ while loop-ი.
# (დაგჭირდებათ ორი ცვლადის შექმნა, ერთში შეინახავთ ჯამს, მეორეში რაოდენობას)
sum_even = 0  
count = 0  
num = 2  

while num <= 100:
    sum_even = sum_even + num 
    count = count + 1 
    num = num + 2  
average = sum_even / count  
print(average)

    
#4) დაბეჭდეთ ყველა რიცხვი 1-დან 30-მდე, რომელიც იყოფა 3-ზე(გამოიყენეთ while loop-ი)
num = 0
while num < 30:
  if num % 3 == 0:
     num = num + 3
     print(num)
    


#5) მომხარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ მიღებული რიცხვის ყველა გამყოფი(გამოიყენეთ for loop-ი)

num = int(input("Enter a number: "))  # მომხმარებლისგან რიცხვის მიღება
print(num,"გამყოფი არის: ")
for i in range(1, num + 1): 
    if num % i == 0: 
        print(i)


#6) დაწერეთ პროგრამა, რომელიც მომხარებელს შემოატანინებს რიცხვს და დაბეჭდავს ეს რიცხვი დადებითია, უარყოფითია თუ 0-ია
num = float(input("შეიყვანეთ რიცხვი: "))  # მომხმარებლისგან რიცხვის მიღება

if num > 0:
    print("რიცხვი დადებითი არის.")
elif num < 0:
    print("რიცხვი უარყოფითი არის.")
else:
    print("რიცხვი არის 0.")

#7) დაწერეთ პროგრამა, რომელიც მომხარებელს შემოატანინებს წელს და გაიგებს არის თუ არა ის ნაკიანი(წელი როდესაც 
# თებერვალში 29 დღე გვაქვს).
#  ნაკიანი არის წელი თუ ის იყოფა 4-ზე და არ იყოფა 100-ზე ან იყოფა 400-ზე.(გამოიყენეთ and და or ოპერატორები)
year = int(input("შეიყვანეთ წელი: "))  # მომხმარებლისგან წლის მიღება

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} არის ნაკიანი წელი.")
else:
    print(f"{year} არ არის ნაკიანი წელი.")

#8) მომხმარებელს შემოატანინეთ რიცხვი 1-დან 100-ის ჩათვლით(ეს იქნება მისი ქულა). თუ მაგალითად 90-დან 100-ის ჩათვლით ექნება ქულა გამოუტანეთ "Your grade is A", 
# თუ 80-დან 90-მდე, გამოუტანეთ "Your grade is B", თუ 70-დან 80-მდე გამოუტანეთ "Your grade is C", სხვა შემთხვევაში გამოუტანეთ "Your grade is D".
score = int(input("შეიყვანეთ თქვენი ქულა (1-დან 100-ის ჩათვლით): "))  # მომხმარებლისგან ქულის მიღება

if 90 <= score <= 100:
    print("Your grade is A")
elif 80 <= score < 90:
    print("Your grade is B")
elif 70 <= score < 80:
    print("Your grade is C")
else:
    print("Your grade is D")
