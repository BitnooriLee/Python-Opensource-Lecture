'''conditional statments
bitnoori
2018 07 18'''

in_id=input("Please enter your ID\n")
members=['bitnoori','andrew']
# real_bitnoori='bitnoori'
# real_andrew='andrew'
for member in members:
    if member==in_id:
        print("Hello!"+member+"")
        import sys
        sys.exit()
print('Who are you?')
# if real_bitnoori==in_str:
#     print("Hello!, Bitnoori")
# elif real_andrew==in_str:
#     print("Hello!, Andew")
# else:
#     print("Who are you?")
