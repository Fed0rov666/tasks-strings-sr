max_length = int(input())
N = int(input())
headlines = []
for _ in range(N):
    headline = input()
    if len(headline) > max_length:
        headline = headline[:max_length-3] + '...'
    headlines.append(headline)

for headline in headlines:
    print(headline)
