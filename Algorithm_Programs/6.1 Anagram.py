
firstWord=str(input("enter a 1st word : "))
secondWord=str(input("enter a 2nd Word : "))
firstWord=list(firstWord)
firstWord.sort()
secondWord=list(secondWord)
secondWord.sort()
if(firstWord==secondWord):
    print("".join(firstWord),"is Anagram of","".join(secondWord))
else:
    print("".join(firstWord),"is not Anagram of","".join(secondWord))
