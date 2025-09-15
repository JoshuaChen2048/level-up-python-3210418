def sort_words(phrase):
  words = phrase.split()
  words.sort(key=str.casefold)
  return ' '.join(words)

# Better version. `sorted()` vs. `list.sort()`!!
def sort_words1(phrase):
  return ' '.join(sorted(phrase.split(), str.casefold))

if __name__ == '__main__':
  print(sort_words('banana ORANGE apple'))  # apple banana ORANGE
