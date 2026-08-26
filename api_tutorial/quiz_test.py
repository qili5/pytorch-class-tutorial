import requests
import random
import html

API_URL = "https://opentdb.com/api.php"

params = {
    "amount": 1,
    "type": "multiple"
}

response = requests.get(API_URL, params=params)
data = response.json()

question_data = data["results"][0]

question = html.unescape(question_data["question"])
correct_answer = html.unescape(question_data["correct_answer"])

wrong_answers = [
    html.unescape(answer)
    for answer in question_data["incorrect_answers"]
]

answers = wrong_answers + [correct_answer]
random.shuffle(answers)

print("\nQuestion:")
print(question)

print("\nChoices:")
for i, answer in enumerate(answers, start=1):
    print(f"{i}. {answer}")

user_answer = int(input("\nEnter your answer number: "))

selected_answer = answers[user_answer - 1]

if selected_answer == correct_answer:
    print("Correct!")
else:
    print("Wrong!")
    print("Correct answer:", correct_answer)