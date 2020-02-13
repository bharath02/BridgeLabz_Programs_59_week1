firstWord=str(input("enter a 1st word : "))
secondWord=str(input("enter a 2nd Word : "))
if(sorted(firstWord)==sorted(secondWord)):
   print(firstWord," Anagram of ", secondWord)
else:
    print(firstWord,"Not Anagram of ", secondWord)
