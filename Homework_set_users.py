#1.1

st1 = {1,2,3,4}
st2 = {2,4,6,8}
st3 = st1.union(st2)
print(f"Miavorumy havasar e: {st3}")

#1.2

st4 = {}
st = set(st4)
for i in st1:
    for j in st2:
        if i == j:
            st.add(i)
print(f"Hatumy havasar e: {st}")

#1.3 

sim_dif = st3 - st
print(sim_dif)

#2

all_users = []
user_info = {}

while True:
    
    Name = input("Enter your name: ")
    Surname = input("Enter your surname: ")
    ID = input("Enter your ID number: ")
    Email = input("Enter your email: ")
    Password = input("Enter your password: ")
    Phone_number = input("Enter your phone number: ")
    
    user_info = {'Name' : Name,
                 'Surname' : Surname,
                 'ID' : ID,
                 'Email' : Email,
                 'Passord' : Password,
                 'Phone_number' : Phone_number
                }

    all_users.append(user_info)


    more_users = input("Do you want to enter another user ?. (Yes / NO )")
    if more_users != 'Yes':
        break

print(all_users)

name_for_search = input("Enter user name: ")
user_found = None

for user in all_users:
    if user['Name'] == name_for_search:
        user_found = user
        break

if user_found:
    print(user_found)
else:
    print("User not found")

