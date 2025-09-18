# QuizGame
🧠 Python Quiz Game (OOP + MVC)

A Python-based Quiz Game that pulls trivia questions dynamically from the Open Trivia DB API.
This project is designed using Object Oriented Programming (OOP) and MVC-inspired architecture for clarity, maintainability, and scalability.

It demonstrates how to:
* Consume and validate API responses
* Apply models to structure data
* Separate business logic into controllers
* Create a clean entry point for running the application
This project is intended as a portfolio showcase for Python developers applying OOP and software design principles in real world applications.

📂 Project Structure
<pre>
quiz-game/
│── connector.py         # API Client: handles API requests
│── data.py              # Data Manager: manages retries & validation
│── question_model.py    # Model: defines structure of each question
│── quiz_controller.py   # Controller: game logic & user interaction
│── main.py              # Entry point: ties everything together
│── README.md            # Documentation (this file)
</pre>

🏗 How It Works:
1. API Connection (connector.py)
  - Establishes connection to the Open Trivia DB API.
  - Fetches 10 easy-level questions in JSON format.
  - Converts the response into Python data.
2. Data Management (data.py)
  - Handles connection retries (up to 3 attempts).
  - Ensures game exits gracefully if API cannot be reached.
  - Stores valid API responses for later use.
3. Question Model (question_model.py)
  - Encapsulates each question into a structured object.
  - Attributes: type, difficulty, category, text, correct answer, other choices.
  - Handles HTML entity decoding (&quot; → ", &#039; → ' etc.).
4. Quiz Controller (quiz_controller.py)
  - Handles game flow, question display, answer validation, and scoring.
  - Manages both True/False and Multiple Choice questions.
  - Uses shuffling to randomize options.
  - Tracks and displays player’s score dynamically.
5. Main Runner (main.py)
  - Initializes the quiz.
  - Retrieves questions from the API.
  - Passes them into QuizController to start the game.

🚀 Installation & Setup
1. Clone the repository:
<pre>
git clone https://github.com/jmbaleyos-linkedin/QuizGame.git
cd quiz-game
</pre>
2. Install dependencies (only requests is needed):
<pre>
pip install requests
</pre>
3. Run the game:
<pre>
python main.py
</pre>

🎮 Example Gameplay
<pre>
******** This is a Multiple choice question ********
What is the capital of France?
A. Berlin
B. Madrid
C. Paris
D. Rome
Your answer: c
You're correct!
Your current score: 1/1
Press Enter for the next question...
</pre>
<pre>
******** This is a True/False question ********
The Great Wall of China is visible from space.
(True or False)
Your answer: false
Sorry, wrong answer. The correct answer is: True
Your current score: 1/2
</pre>

📐 Software Design Principles Applied
* Encapsulation (OOP) → Each class manages its own data and behavior.
* MVC Pattern →
  - Model → QuestionModel
  - Controller → QuizController
  - View → Console inputs/outputs handled inside the controller
  - Main/Entry → main.py glues everything together
* Separation of Concerns → API logic, data handling, modeling, and gameplay are kept in separate files.

🔮 Future Improvements
* Add a GUI version (Tkinter or PyQt).
* Allow players to select category/difficulty at the start.
* Implement leaderboards (save player scores in a file or DB).
* Add unit tests for data validation and quiz logic.
* Extend to support timed questions.

👨‍💻 Author
Created by Joseph Mel V. Baleyos — Python Developer passionate about OOP and clean architecture.
If you like this project, ⭐ star the repo and connect with me on LinkedIn (www.linkedin.com/in/joseph-mel-baleyos-4466461a0).
