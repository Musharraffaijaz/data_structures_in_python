str = "Hello World!"
print(str)          # Prints complete string
print(str[0])       # Prints first character of the string
print(str[0:5])     # Prints characters starting from 0 to 4
print(str[0:])      # Prints string starting from 0
print(str[:-1])     # Prints string starting from 0 to last character
print(str[-1])      # Prints the last character
print(str[::-1])    # Prints the string in reverse order 
print(str[0::2])    # Prints the string with a step of 2
print(str * 2)      # Prints string two times
print(str + "TEST") # Prints concatenated string

#METHODS ON STRIGS
print(str.upper())  # Converts all lowercase letters in a string to uppercase
print(str.lower())  # Converts all uppercase letters in a string to lowercase
print(str.capitalize()) # Converts the first character of a string to uppercase

newStr = "  Hello World!  "
print(newStr)
print(newStr.strip())  # Removes any whitespace from the beginning or the end

print(str.replace("Hello", "Bye")) # Replaces a string with another string
print(str.find("World!")) # Searches the string for a specified value and returns the position of where it was found

beverage = "tea"
quantity = 2
price = 3.5
order = "I ordered {} cups of {} each for ${}, hence a total of ${}"

print(order.format(quantity, beverage, price, quantity*price)) # Formats specified values in a string

#LISTS TO STRINGS
newList = ["apple", "banana", "cherry"]
print("".join(newList)) # Joins the elements of an iterable to the end of the string
print(", ".join(newList)) # Joins the elements of an iterable to the end of the string with a comma and a space
print("-".join(newList)) # Joins the elements of an iterable to the end of the string with a hyphen