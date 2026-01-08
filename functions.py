def add_numbers(a,b):
    sum = a+b
    return sum

result = add_numbers(10,20)
print(result)

def string_reverse(string):
    return string[::-1]

input = input("Enter a String : ")
result = string_reverse(input)
print(f"Original String : {input}")
print(f"Reversed String : {result}")

#area of rectangle
def area_of_rectangle(length, breadth):
    return length * breadth

length_input = int(input("Enter length of rectangle : "))
breadth_input = int(input("Enter breadth of rectangle : "))
area = area_of_rectangle(length_input,breadth_input)
print(area)

#greet a user
def greeting(name = "Guest"):
    return f"Hello, {name}!"
user_name = input("Enter your name : ")
if user_name :
    message = greeting(user_name)
else:
    message = greeting()
print(message)

#Write a Python program to count the number of occurrences of each word in a given sentence.
class StringManipulator:
    def __init__(self, string=""):
        self.string = string

    def reverse_string(self):
        return self.string[::-1]

    def is_palindrome(self):
        reversed_string = self.reverse_string()
        return self.string == reversed_string

# Example usage
string_input = input("Enter manipulator =  ")
print(f"Reversed String: {StringManipulator.reverse_string()}")
print(f"Is Palindrome: {StringManipulator.is_palindrome()}")
