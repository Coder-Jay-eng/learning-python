from Question import Question

question_prompts = [
    "What is the capital city of Kenya? \n(a) Nairobi\n(b) Kisumu\n(c) Mombasa\n\n",
    "What is the capital city of Uganda? \n(a) Jinja\n(b) Kampala\n(c) Mbale\n\n",
    "What is the color of bananas? \n(a) Magenta\n(b) Red\n(c) Yellow\n\n",
]


questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct")


run_test(questions)
