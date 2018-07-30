
def login(re_id):
    members=['bitnoori','andrew']
    for member in members:
        if member==re_id:
            return True
        else:
            return False

in_id=input("Please enter your ID\n")
login(in_id)

if login(in_id):
    print("Hello!"+in_id+"")
else:
    print('Who are you?')
