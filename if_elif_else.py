a = int(input("Enter your age:"))

# If elif else ladder

if(a >= 18):
    print("You are able to vote:")

elif(a < 0):
    print("You are entering negative age which is invalid")

elif(a == 0):
    print("You are entering 0")
    
else:
    print("You are not able to vote")    