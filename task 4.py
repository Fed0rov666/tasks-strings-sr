words = []
while True:
    word = input()
    if word == 'стоп':
        break
    words.append(word)

shortest_word = min(words, key=len)
longest_word = max(words, key=len)

if all(letter in longest_word for letter in shortest_word):
    print('ДА')
else:
    print('НЕТ')
