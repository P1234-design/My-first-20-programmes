import random
pwd = input("Check your password strength:")

length_ok = len(pwd) >= 8
upper_ok = any(c.isupper() for c in pwd)
lower_ok = any(c.islower() for c in pwd)
num_ok = any(c.isdigit() for c in pwd)
sym_ok = any(c in"!@#$%^&*" for c in pwd)

score = sum([length_ok,upper_ok,lower_ok,num_ok,sym_ok])

if score == 5:
    print("Strength: Very Strong!")
elif score >= 3:
    print('Strength: Moderate')
else:
    print('Strength: Weak! MAY BE HACK.')
    
if 