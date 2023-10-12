password = 'cheesy chips'
digit_found = False
for c in password:
    print(c)
    if c in '0123456789':
        digit_found = True
print(digit_found)

while True:
    answer = input('do you want chips with that? (y/n)')
    if answer == 'y' or answer =='n':
        break
if answer == 'y':
    print('chips again, bad for your health')
print("I'll get coocking then")