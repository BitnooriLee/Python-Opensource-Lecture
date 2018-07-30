'''conditional statments
bitnoori
2018 07 18'''

def login(re_id):
    members=['bitnoori','andrew']
    for member in members:
        if member==re_id:
            print("Hello!"+member+"")
            import sys
            sys.exit()
    print('Who are you?')

in_id=input("Please enter your ID\n")
login(in_id)
