User_Name=input("Enter a Name")
User_Name=list(User_Name)
if(len(User_Name)>3):
	print("Hello","".join(User_Name),"How are you")
else:
	print("Nmae Length is more than 3 alphabets")