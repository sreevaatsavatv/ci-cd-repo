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
