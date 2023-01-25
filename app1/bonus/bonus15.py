import json
import os

filepath = os.path.join("bonus", "questions.json")

with open(filepath) as file:
    content = file.read()


data = json.loads(content)


for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(f"{index + 1} - {alternative}")
    question["user_choice"] = input("Enter your answer: ")

score = 0
for index, question in enumerate(data):
    result = "Wrong"
    if question["user_choice"] == question["correct_answer"]:
        score += 1
        result = "Correct"
    message = (
        f"{index+1} - {result} - Your answer: {question['user_choice']}, "
        f"Correct Answer: {question['correct_answer']} "
    )
    print(message)


print(f"Score: {score}/{len(data)}")
