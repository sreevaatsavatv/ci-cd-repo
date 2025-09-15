import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero not allowed")
        return a / b

    def factorial(self, n):
        return math.factorial(n)

    def power(self, base, exp):
        return pow(base, exp)


class TextProcessor:
    def word_count(self, text):
        return len(text.split())

    def char_count(self, text):
        return len(text)

    def reverse_text(self, text):
        return text[::-1]

    def is_palindrome(self, text):
        cleaned = text.lower().replace(" ", "")
        return cleaned == cleaned[::-1]
