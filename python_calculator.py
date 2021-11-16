n1 = float(input("Enter your first number:"))
o = input("Enter an operator:")
n2 = float(input("Enter your second number:"))
c = input("Credits? y/n:")

if c == "y":
   print("https://www.youtube.com/channel/UCoIgEBRn2TeOnIAg46Y6log")
elif o == "+":
   print(n1 + n2)
elif o == "-":
   print(n1 - n2)
elif o == "/":
   print(n1 / n2)
elif o == "*":
   print(n1 * n2)
else:
    print("Invalid Operator. Try again...")