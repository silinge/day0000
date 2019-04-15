from sys import argv

script, user_names = argv

prompt = "> "
print(f"Hi {user_names}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_names}?")

likes = input(prompt*4)
print(f"Where are you from {user_names}?")
lives = input(prompt*5)

print("What kind of computer do you have?")
computer = input(prompt*4)

print(f"""
Alright then, so you said {likes} abouts liking me.
You are from {lives}. Not sure where that is.
And you have a {computer}, Nice one.
""")