from app.textprocessor import TextProcessor

tp = TextProcessor()

def test_word_count():
    assert tp.word_count("hello world") == 2

def test_char_count():
    assert tp.char_count("hello") == 5

def test_reverse_text():
    assert tp.reverse_text("hello") == "olleh"

def test_is_palindrome_true():
    assert tp.is_palindrome("madam")

def test_is_palindrome_false():
    assert not tp.is_palindrome("hello")

def test_is_palindrome_with_spaces():
    assert tp.is_palindrome("nurses run")
