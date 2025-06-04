# Mad Libs Story Generator with Conditional Statements

print("🎉 Welcome to the Mad Libs Zoo Adventure! 🎉")
print("Let's build your silly story. Please answer the following prompts:\n")

# Collecting user inputs
weather = input("How's the weather today? (e.g., sunny, rainy): ").lower()
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
adjective3 = input("Enter a third adjective: ")
adjective4 = input("Enter one more adjective: ")
animal1 = input("Name a funny animal: ")
animal2 = input("Name a majestic animal: ")

# Conditional twist
if weather == "rainy":
    activity = "slipping in the mud"
    surprise = "a penguin with an umbrella"
else:
    activity = "swinging from the trees"
    surprise = "a giraffe wearing sunglasses"

# Constructing the story
print("\n📝 Here's your Mad Libs Zoo Story:\n")

story = f"""
On a beautiful {adjective1} day, I went to the zoo. 
I saw a funny {adjective2} {animal1} {activity}. 
Then, I spotted a majestic {adjective3} {animal2} lounging in the sun. 
Suddenly, I noticed {surprise} walking by! 
What a wild and {adjective4} experience!
"""

print(story)
print("🎊 Thanks for playing Mad Libs! Come back for another silly adventure! 🎊")
