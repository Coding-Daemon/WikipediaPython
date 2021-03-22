#Code by Mr.Coder , Subscribe to Mr.Coder , and like all videos

# import the module
import wikipedia

# taking input of what I want to search
User_query = input("What do you want to get on wikipedia: ")

#getting result
result = wikipedia.summary(f"{User_query}", sentences = 2)

#printing result
print (result)

