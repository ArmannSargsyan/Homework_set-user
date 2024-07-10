reserved_names = ["admin","root"]


username = input("enter your username: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")
password = input("Enter your password: ")
password_repeat = input("Please repeat your password: ")

user = {"Username" : username,
        "Email" : email,
        "Phone" : phone,
        "Password" : password,
        "Password_repeat" : password_repeat
        }

print(user)

for i in username:
    if not i.isalnum():
        print("Enter only alphanumeric characters!")

if username in reserved_names:
    print("Username can't be reserved names")


if len(username) < 5:
    print("Too short username")
elif 20 < len(username):
    print("Too long username")
else:
    5 <= len(username) <= 20
        




for i in email:
    if '@' not in email and '.' not in email:
        print("Not valid email!")
    


if phone[0:4] == '+374' and len(phone) == 12 and phone[4:].isdigit():
    print("Success phone validation")

elif phone[0:4] != '+374' and len(phone) == 8 and (i.isdigit for i in phone):   
    print("Success phone number validation")

else:
    print("Not valid phone number")

if len(password) < 8:
    print("Too short password")

elif not any(i in " !@#$%^&*" for i in password):
    print("Must contain one special character(!@#$%^&*)")

elif not any(i.isupper for i in password):
    print("Must contain one uppercase letter")

elif not any(i.islower for i in password):
    print("Must contain at least one lowercase letter")

elif not any(i.isdigit for i in password):
    print("Must contain digit")

elif password != password_repeat:
    print("Passwords are not identical!")

else:
    print("Success user validation")

