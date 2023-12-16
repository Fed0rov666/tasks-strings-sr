N = int(input())
advices = []
for _ in range(N):
    advice = input()
    if advice[:3].lower() == 'не ':
        advice = advice[3:]
    advices.append(advice)

for advice in advices:
    print(advice)
