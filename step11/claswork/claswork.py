#პაროლის ვალიდაციის პროგრამა:
#შექმენით ცვლადი სადაც შეინახავთ პაროლს(მაგალითად: goa1234)
#სანამ მომხარებელი არ შემოიყვანს სწორ პაროლს მანამდე შემოატანინეთ ხელახლა.
# მომხარებელს ექნება 3 ცდა. თუ შემოიყვანა სწორი პაროლი დაუპრინტეთ 
# "წვდომა მიღებულია", სხვა შემთხვევაში "სცადეთ ხელახლა", 
# დაპრინტეთ რამდენი მცდელობა დარჩა და გამოაკელით ცდას ერთი. 
#როდესაც მცდელობები ამოიწურება გათიშეთ while loop-ი
 
correct_password = "goa1234"
user_pass = ''
tries = 3
while tries > 0 and user_pass != correct_password:
    user_pass = input("enter your password (you have " +  str(tries) + " tries left): ")
    tries = tries - 1

    if user_pass == correct_password:
     print("accsess granted!")
    elif tries == 0:
       print("You've reached the maximum number of tries.Access denied!")
    else:
       print("access denied! Try again.")
    
    


