#conditional statments
input_id=input("Please enter your ID\n")
input_pw=input("Please enter your pw\n")
real_id,real_pw='bitnoori','1234'

if real_id==input_id and real_pw==input_pw:
    print("Hello!"+real_id.upper()+"")
else:
    print("fail to login")
