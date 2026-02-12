" Store Correct Credentials"

correct_username = "admin"
correct_password = 1234

username = input("Enter Username: ")
password = int(input("Enter password: "))

if username == correct_username and password == correct_password:
    print("Login Successfull")

else:
    print("Invalid Login Credentials")