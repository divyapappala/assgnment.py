card_digits=input("enter your card number")
card_digits=[int(digit)for digit in card_digits]

x = card_digits.pop()

card_digits.reverse()

for i in range(0,len(card_digits)+1,2):
    card_digits[i]=card_digits[i]*2

for i in range(len(card_digits)):
    if card_digits[i] > 9:
        card_digits[i]=card_digits[i]-9

total=sum(card_digits)+x

if total%10==0:
    print("valid")
else:
    print('Invalid')