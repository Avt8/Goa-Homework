# while ციკლის საშვალებით გამოიტანეთ რიცხვები 1-იდან 10-მდე
'''
num = 0
while num < 9:
   num = num + 1
   print(num)

#2) while ციკლის საშვალებით გამოტანეთ რიცხვები 20 დან 0 მდე.
num = 21
while num > 1:
   num = num - 1
   print(num)

'''

#3) while ციკლის საშუალებით გგამოიტანეთ  1-დან 20-მდე მხოლოდ ლუწი რიცხვები.
num = 0
while num < 20:
   print(num)
   num = num + 2



#4) while ციკლის საშუალებით გამოიტანეთ 1-დან 100-მდე ყველა 5-ის ჯერადი რიცხვი.
num = 0
while num < 95:
   num = num + 5
   print(num)

#5) while ციკლისა და input-ის საშუალებით შემოატანინეთ მომხარებელს პაროლი "goa123" ტოლი.
password = input("Enter your password: ")
while password != "goa123":
   password = input("Enter your password again: ")
if password == "goa123":
      print("Correct password")