textData = "The quick brown fox"

for letter in textData:
    if letter in "xX":
        print("X found!")
        break
else:
    print("No X found...") 
