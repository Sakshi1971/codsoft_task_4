import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_welcome_message(self):
        print("Easy Pisy Quiz Game!!!")
        print("You will be asked General Knowledge Questions.")
        print("\n")
        print("Let's get started!\n")

    def present_quiz_questions(self):
        random.shuffle(self.questions)
        for idx, question in enumerate(self.questions, start=1):
            print(f"Question {idx}: {question['question']}")
            if 'choices' in question:
                for choice_num, choice in enumerate(question['choices'], start=1):
                    print(f"{choice_num}. {choice}")
            user_answer = input("Your answer: ").strip().lower()
            self.evaluate_user_answer(question, user_answer)

    def evaluate_user_answer(self, question, user_answer):
        correct_answer = question['answer'].lower()
        if user_answer == correct_answer:
            print("Correct!\n")
            self.score += 1
        else:
            print("Incorrect.")
            print(f"The correct answer is: {correct_answer}\n")

    def display_final_results(self):
        print("Quiz Completed!")
        print(f"Your final score is: {self.score}/{len(self.questions)}")
        if self.score == len(self.questions):
            print("Congratulations! You got all the questions right.")
        elif self.score >= len(self.questions) / 2:
            print("Good job! You did well.")
        else:
            print("Keep practicing to improve.")

    def play_again(self):
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        return play_again == "yes"

def main():
    questions = [
        {
            'question': "which is the national bird of India?",
            'answer': "Peacock"
        },
        {
            'question': "How many letters are there in the English alphabet?",
            'answer': "26"
        },
         {
            'question': "What do you call a house made of ice??",
            'answer': "Igloo"
        },
         {
            'question': "Which is the largest animal in the world??",
            'answer': "Blue whale"
        },
         {
            'question': "Which festival is known as the festival of colors?",
            'answer': "Holi"
        },
         {
            'question': "What type of bird lays the largest eggs?",
            'answer': "Ostrich"
        },
         {
            'question': " What is the top color in a rainbow?",
            'answer': "Red"
        },
         {
            'question': "Who was the first man to walk on the moon?",
            'answer': " Neil Armstrong"
        },
         {
            'question': "Which country is home to the kangaroo?",
            'answer': "Australia"
        },
         {
            'question': "Who is the founder of Microsoft?",
            'answer': "Bill Gates"
        },
        
        # Add more questions here
    ]

    quiz = QuizGame(questions)
    quiz.display_welcome_message()

    play_game = True
    while play_game:
        quiz.present_quiz_questions()
        quiz.display_final_results()
        play_game = quiz.play_again()

if __name__ == "__main__":
    main()
