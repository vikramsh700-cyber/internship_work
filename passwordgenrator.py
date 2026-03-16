
import random

Letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbol = ['!','#','$','%','&','(',')','*','+']

print("welcome to password genrator!")

n_Letters = int(input("How many letters you want in your password?\n"))
n_symbol = int(input("How many letters you want in your password?\n"))
n_numbers = int(input("How many letters you want in your password?\n"))


password = " "

for i in range(1,n_Letters +1):
    char = random.choice(Letters)  
    password = password + char

for i in range(1, n_symbol +1):
    char = random.choice(symbol)
    password = password + char    

for i in range(1, n_numbers +1):
    char = random.choice(numbers)
    password = password + char
print(password)
