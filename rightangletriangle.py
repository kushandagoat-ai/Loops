print("right triangle of stars *")
n = int(input("How many rows of stars do you want?"))
for i in range(n):
    for j in range (i + 1):
        print("*", end ="")
    print("")