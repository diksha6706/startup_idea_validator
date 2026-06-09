from file_handling import *
from idea_validator import StartupIdeaValidator


print("1. Validate New Idea")
print("2. View Previous Reports")

choice = input("Enter Choice: ")
if(choice == "2"):
    view_reports()
    exit()

idea_name = input("Enter Name of Idea: ")
problem_solved = input("Problem solved: ")
target_audience = input("Target Audience: ")
try:
    budget = int(input("Estimated Budget: "))

except ValueError:
    print("Invalid Budegt1 Please enter numbers only.")
    exit()


revenue_model = input("Revenue Model: ")

idea = {"name" : idea_name, "problem" : problem_solved, "audience" : target_audience,
        "budget" : budget, "revenue_model" : revenue_model }

validator = StartupIdeaValidator(idea)
# print(validator.idea)


score = validator.calculate_score()
print("\nIdea Score:", score)

rating = validator.get_rating(score)
print("Idea Rating: ", rating )

strengths, weaknesses = validator.analyze_idea()

print("\nStrengths:")
for item in strengths:
    print("-", item)

print("\nWeaknesses:")
for item in weaknesses:
    print("-", item)

strength_text = ""
for item in strengths:
    strength_text += item + "\n"

weakness_text = ""
for item in weaknesses:
    weakness_text += item + "\n"

save_report(idea_name, score, rating, strength_text, weakness_text)

