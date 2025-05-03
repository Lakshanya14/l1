print("😊Hello I am an AI chatbot,what is your name?")
name=input()
print(f"Nice to meet you {name}!")
print("How are you feeling (good/bad)")
mood=input().lower()
if mood==("good","awesome","great"):
    print("I am glad to hear!")
elif mood==("bad","I dont know"):
    print("I am sorry to hear that!")
else :
    print("I know sometimes it is difficult to tell feelings")

print("It was nice to talk with you{name},Goodbye!")        