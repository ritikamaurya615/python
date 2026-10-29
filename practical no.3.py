# safe Division Calculator
# try:
#     a= int(input("enter your number:"))
#     b= int (input("Enter you number2:"))
#     print(a/b)
# except ValueError:
#     print("invalid input")
# except ZeroDivisionError:
#     print("cannot divide by 0")        


# Positive number validator 

# try:
#     num=int(input("enter your number :"))
#     if num < 0:
#         raise ValueError("Number cannot be negative")
# except ValueError:
#     print("give a valid number")

# else:
#     print("number accepted:",num)

    


#   List Index Handling

numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index(0-4) : "))
    print("numbers(index)")

except IndexError:
    print("Invalid index")

except ValueError:
    print("Please enter an integer")