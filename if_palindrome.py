def if_palindrom(word: str):
    reversed_word = word[::-1]
    if reversed_word == word:
        return print('the word is a palindrome')
    else:
        return print('the word is not a palindrome')


print('input any word, we will see the word is a palindrome')
try:
    input_word = str(input('Word: '))
except:
    print('Error')

if_palindrom(input_word)
