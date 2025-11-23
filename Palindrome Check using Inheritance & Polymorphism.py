# Base Class
class PalindromeChecker:
    def __init__(self, value):
        self.value = value

    def is_palindrome(self):
        # Will be overridden by child classes
        pass


# Derived Class for String
class StringPalindrome(PalindromeChecker):
    def is_palindrome(self):
        text = self.value.replace(" ", "").lower()
        return text == text[::-1]


# Derived Class for Integer
class IntegerPalindrome(PalindromeChecker):
    def is_palindrome(self):
        num_str = str(self.value)
        return num_str == num_str[::-1]


# ---- Main Program ----
user_input = input("Enter a value (string or integer): ")

# Check whether input is integer or string
if user_input.isdigit():
    obj = IntegerPalindrome(int(user_input))
else:
    obj = StringPalindrome(user_input)

# Polymorphic call
if obj.is_palindrome():
    print("It is a Palindrome")
else:
    print("It is NOT a Palindrome")
