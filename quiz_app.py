# quiz_app.py

# Step 1: Store questions in a dictionary
quiz = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Bengaluru", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. HTML", "C. C++", "D. Java"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. func"],
        "answer": "C"
    },
    {
        "question": "Which data structure uses key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Set", "D. Dictionary"],
        "answer": "D"
    }
]

# Step 2: Function to run the quiz
def run_quiz():
    score = 0
    print("🎯 Welcome to the Python Quiz!\n")

    for idx, q in enumerate(quiz, start=1):
        print(f"Q{idx}: {q['question']}")
        for opt in q['options']:
            print(opt)
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        if user_answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer is {q['answer']}\n")

    print(f"🎉 Your final score is {score}/{len(quiz)}")

# Step 3: Run the quiz
if __name__ == "__main__":
    run_quiz()
