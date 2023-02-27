while True:
    word = list(input())
    if word[0] == '0':
        break
    r_word = word[::-1]
    print('yes' if int(''.join(word))==int(''.join(r_word)) else 'no')