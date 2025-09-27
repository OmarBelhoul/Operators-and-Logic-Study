#exercise 1
number1=int(input("typer the first number "))
number2=int(input("typer the second number "))
operator=input("choose an operator '+'or'*'or'%'or '**' ")

if operator =="+":
    print(number1+number2)
elif operator =="*":
    print(number1*number2)
elif operator == "%":
    print(number1%number2)
elif operator =="**":
    print(number1**number2)
else :
    print("error")

#exercise 2
number_1=int(input("choose a number"))
number_2=int(input("choose another number"))

if number_1>number_2 :
    print("number 1 is bigger")
elif number_1==number_2 :
    print("equal")
elif number_2<= number_1 :
    print("number 2 is smaller or equal")

#exercise 3
user_age=int(input("how old are you? "))
user_grade=int(input("what's your grade? "))

if 12 <= user_age <= 17 and user_grade >= 50:
    print("congrats teenager")
elif user_grade >= 50:
    print("congrats")
else :
    print("you failed")

    