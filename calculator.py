print(''' 
. + Addition
. - Substraction
.* Multiplication
.  /Division
.  %Modulus       
''')


num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

opr = input("Enter the opr...(+,-,/,*,%):")
if opr == "+":
    print(num1 + num2)

elif opr =="-":
    print(num1 - num2)

elif opr =="*":
    print(num1 * num2)

elif opr =="%":
    print(num1%num2)  
      
elif opr =="/":
    if num2 !=0:
      print(num1/num2)
    else:

        print("invalid divisible:")
else:
    print("invalid opr: please enter valid opr:")