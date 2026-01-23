Word  = input("What word would you like to type?")
Character = input("Which letter would you want to find out")
count = 0
i = 0
while(i < len(Word)):
    if Word[i]  == Character:
        count = count + 1
    i = i +1
print("The number of times", Character,"has appeared is", count )