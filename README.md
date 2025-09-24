# Multilingual-Digital-Literacy-Chatbot
A multilingual digital literacy chatbot built with Python and Tkinter. This standalone GUI application teaches online safety and cybersecurity through an interactive quiz and keyword-based responses. It supports multiple languages, including English, Hindi, and Gujarati, using a simple rule-based system.
# Building things for the web.
Also, giving a quick, just-for-fun shout-out to the creator, Anup Yadav.😉


FOR ENHANCED VERSION

Multilingual Digital Literacy Chatbot
This is a graphical user interface (GUI) chatbot application built with Python's Tkinter library. It's designed to provide information on digital literacy, online safety, and various government schemes in multiple Indian languages. The application is user-friendly, self-contained, and easily extensible.

✨ Features
🌐 Multilingual Support: The chatbot operates in five languages/dialects:

English

Hindi (हिंदी)

Hinglish (Hindi + English)

Awadhi (अवधी)

Gujarati (ગુજરાતી)

📚 Educational Content: Provides concise information on key topics relevant to rural and semi-urban users:

Digital Literacy & Online Security (OTP, Phishing).

Government Schemes (Agriculture, Health, Skills, Sanitation).

National Initiatives (Digital India, Make in India).

📝 Interactive Quiz: A multiple-choice quiz to test the user's knowledge of online safety concepts.

🤖 Basic NLP: Uses TextBlob to perform simple sentiment analysis on user input that isn't a recognized command, allowing for friendly, human-like responses.

🛠️ Utility Functions:

Tells the current time and date.

Provides a mock weather report for Lucknow.

Tells a joke in the selected language.

🎨 Image Generation: Simulates an image generation feature by creating a placeholder image URL based on user text input.

📜 Conversation Logging: Automatically saves the conversation history to a chat_log.json file for review.

🎨 Modern UI: A clean, WhatsApp-inspired chat interface with distinct colors for user and bot messages.

🚀 Getting Started
Follow these instructions to get a copy of the project up and running on your local machine.

Prerequisites
You need to have Python 3 installed on your system. Additionally, you'll need the following Python libraries:

tkinter: Usually comes pre-installed with Python. If not, you may need to install it separately (e.g., sudo apt-get install python3-tk on Debian/Ubuntu).

textblob: A library for processing textual data.

Installation
Clone the repository or save the code: Save the Python code into a file named chatbot.py.

Install the required library: Open your terminal or command prompt and install textblob.

Bash

pip install textblob
Download TextBlob Corpora: After installing the library, you need to download the necessary data for translation and sentiment analysis. Run the following command in your terminal:

Bash

python -m textblob.download_corpora
Running the Application
Navigate to the directory where you saved chatbot.py and run the following command:

Bash

python chatbot.py
The application window will open, starting with the language selection screen.

Code Structure
The code is organized within a single class, ChatbotGUI, for simplicity.

LANG_DATA Dictionary: This large dictionary at the top of the file holds all the text strings for the application in every supported language. This makes it incredibly easy to manage translations or add new languages without changing the core application logic.

__init__(self, master): The constructor initializes the main window, sets up application state variables (like current_lang and state), and builds the initial language selection screen.

UI Setup (_setup_... methods):

_setup_language_selection(): Creates the initial screen with buttons for each language.

_setup_main_ui(): Builds the main chat interface after a language is selected.

_setup_chat_window(): Configures the text area where the conversation is displayed.

_setup_input_area(): Creates the text entry box and the "Send" button.

Command Handling:

self.commands Dictionary: This dispatcher maps command strings (like 'info', 'quiz') to their corresponding handler methods (like _show_info, start_quiz). This is a clean and scalable alternative to a long if/elif/else chain.

_process_command(self, command): This is the central logic hub. It takes the user's raw input, checks for special cases (like "otp"), handles multi-step states (like the quiz), and uses the self.commands dictionary to call the correct function.

Feature Logic (_show_..., _handle_..., start_... methods):

Each command has a dedicated method that retrieves the appropriate text from LANG_DATA and displays it.

The quiz logic is managed by changing self.state to "quiz" and tracking the question number and score.

The NLP logic in _handle_nlp_response is the fallback for any input that is not a recognized command.

Logging (_log_user_question): This method appends each user query and bot response to chat_log.json, along with a timestamp.

🧑‍💻 About the Creators
This chatbot was created by Anup Yadav (student of BBD University, resident of Siwan, Bihar) with programming by Ankit Singh.
