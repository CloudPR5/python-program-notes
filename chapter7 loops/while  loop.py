'''This program uses a while loop to print numbers from 1 to 10.'''

# number = int(input("enter a number"))
number = 1
while number <= 10:
    print(number)
    # print(f"the sum of number {number}")
    number+=1


'''This program sums numbers from 1 to a user-given number.'''

n=int(input("enter a number:"))
sum=0
i=1
while i<=n:
    sum+=n
    i+=1
    # print(f"the sum of number from 1 to {n} is {sum}")
    print ( f"{sum }")


'''This program prints even numbers between 1 and 20.'''

# number=2
# while number<=20:
#     print(number)
#     number+=2

number=int(input("enter a number"))
while number<=20:
    print(f"sum of number{number}")
    number+=2