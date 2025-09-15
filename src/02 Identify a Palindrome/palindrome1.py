import re

def is_palindrome(phrase):
  phrase = ''.join(re.findall(r'[a-z]+', phrase.lower()))  
  phrase1 = phrase[::-1]

  return phrase1 == phrase

if __name__ == '__main__':
    print(is_palindrome('hello world'))  # false
    print(is_palindrome("abc cba"))
    print(is_palindrome("Go hang a salami, I'm a lasagna hog."))  # true
