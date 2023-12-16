size = int(input("Введите размер доски: "))

for i in range(size, 0, -1):
    for j in range(65, 65 + size):
        print(chr(j) + str(i), end=" ")
    print()
