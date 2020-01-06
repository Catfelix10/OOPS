import account
deposit = 0
withdraw = 0
namelist = []
passwordlist = []
balancelist = []
if input("Would you like to add an account? (y or n)") == 'y':
    addname = input("What do you want your account name to be. ")
    namelist.append(addname)
    addpassword = input("What do you want your password to be. ")
    passwordlist.append(addpassword)
    addbalance = input("What is your balance in "+ (addname)+ "'s account. ")
else:
    name = input("Enter your user name. ")
if name == namelist:
           name = account.Account('me', 0)
           password = input("Enter your password. ")
elif password == passwordlist:
           print(acct.balance)
else:
           print("Your account Name or Password was denied. ")



import account

acct1 = account.Account('Jose',100)
acct2 = account.Account('Zelda',500)

acct1.deposit(200)
acct1.withdrawl(700)
acct2.deposit(200)
acct2.withdrawl(700)

print(acct1.owner, acct1.balance)
print(acct2.owner, acct2.balance)
acct1.deposit(20.23*1.22)
print(acct1._str_())
print(acct2._str_())
