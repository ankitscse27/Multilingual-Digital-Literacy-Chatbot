# ✨ Multilingual Digital Literacy Chatbot ✨

This is a comprehensive, self-contained **Graphical User Interface (GUI) chatbot** built with **Python** and **Tkinter**. It is designed to be an accessible resource for promoting **digital literacy** and **online safety** by providing critical information in multiple Indian languages.

The application is ideal for bridging the digital divide in rural and semi-urban communities by offering actionable, easy-to-understand guidance.

---

## 🌟 Key Features

| Category | Feature | Description |
| :--- | :--- | :--- |
| **🌐 Accessibility** | **5-Language Support** | Seamless operation in **English**, **Hindi (हिंदी)**, **Hinglish**, **Awadhi (अवधी)**, and **Gujarati (ગુજરાતી)**. |
| **📚 Education** | **Actionable Content** | Provides concise information on: **Online Security** (OTP best practices, Phishing), **Government Schemes** (Agriculture, Health, Skills), and **National Initiatives** (*Digital India*). |
| **📝 Interaction** | **Interactive Quiz** | A multiple-choice quiz feature to actively test and reinforce the user's knowledge of online safety concepts. |
| **🤖 Intelligence** | **Basic NLP & Fallback** | Uses **TextBlob** for simple sentiment analysis, enabling friendly, human-like responses to conversational input. |
| **🛠️ Utilities** | **Built-in Functions** | Provides the **current time/date**, a **mock weather report** (for Lucknow), and shares a **joke** in the selected language. |
| **📜 Logging** | **Conversation Log** | Automatically saves a complete, time-stamped history of the chat to a `chat_log.json` file. |
| **🎨 UI/UX** | **Modern Design** | A clean, intuitive, and **WhatsApp-inspired** chat interface with distinct styling for user and bot messages. |

---

## 🚀 Getting Started

Follow these instructions to set up and run the application on your local machine.

### Prerequisites

You must have **Python 3** installed on your system.

The following Python libraries are required:
* `tkinter`: The standard Python GUI library (usually pre-installed).
* `textblob`: For natural language processing and sentiment analysis.

### Installation & Setup

1.  **Clone or Save:**
    Save the Python source code as `literacybot.py`.

2.  **Install Library:**
    Open your terminal or command prompt and install the `textblob` library:

    ```bash
    pip install textblob
    ```

3.  **Download Corpora:**
    The necessary linguistic data for NLP and translation features must be downloaded. Run this command:

    ```bash
    python -m textblob.download_corpora
    ```

### Running the Application

Navigate to the directory containing `chatbot.py` and execute the following command:

```bash
python literacy-bot.py
The application window will launch, starting with the language selection screen.⚙️ Code Structure and ExtensibilityThe application is structured for clarity and easy maintenance within a single ChatbotGUI class.ComponentRoleNotes on ExtensibilityLANG_DATA DictionaryCentral Text RepositoryContains all text strings across all supported languages. Highly extensible: Add new languages or update content by modifying only this dictionary.self.commands DictionaryCommand DispatcherMaps user-recognized keywords ('info', 'quiz') to their specific handler methods (_show_info, start_quiz). Scalable: Easily add new features by defining a new method and registering its keyword here._process_commandCentral Logic HubManages user input flow, state changes (e.g., during the quiz), and special case handling.UI Setup MethodsGUI ConfigurationDedicated methods (e.g., _setup_main_ui) for configuring the visual elements of the Tkinter interface.Feature Logic MethodsCore FunctionalityMethods like _show_otp or _handle_quiz_response contain the specific logic for each feature.🧑‍💻 About the CreatorsThis project was conceived and developed as an initiative to promote digital inclusion.RoleNameDetailsCreatorAnup YadavStudent of BBD University, Resident of Siwan, BiharProgrammerAnkit Singh(A special shout-out to Anup Yadav for the original concept!)
