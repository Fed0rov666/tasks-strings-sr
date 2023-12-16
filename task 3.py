word1 = input()
word2 = input()

bulls = sum(1 for i in range(len(word1)) if word1[i] == word2[i])
cows = len(set(word1) & set(word2)) - bulls

print(bulls, cows)
