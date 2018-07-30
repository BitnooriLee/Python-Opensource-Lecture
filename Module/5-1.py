import auth

in_id=input("Please enter your ID\n")

if auth.login(in_id):
    print("Hello!"+in_id+"")
else:
    print('Who are you?')
