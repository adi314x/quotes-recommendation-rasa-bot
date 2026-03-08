# 💬 Quotes Recommendation Chatbot

A conversational AI chatbot built with **Rasa NLU** that recommends quotes based on user mood and intent. The chatbot understands natural language and delivers motivational, inspirational, romantic, humorous, and success-related quotes through an interactive web interface.

---

## ✨ Features

- **Intent Recognition** — Understands user emotions and needs using Rasa NLU
- **6 Quote Categories** — Motivation, Inspiration, Love, Humor, Success, and General
- **Multiple Response Variations** — 5 unique responses per category to avoid repetition
- **Fallback Handling** — Gracefully handles unrecognized input with helpful suggestions
- **Follow-up Conversations** — Asks users if they want more quotes after each response
- **Web Interface** — Clean, browser-based chat UI powered by Flask
- **REST API** — Communicates via Rasa's REST webhook for easy integration

---

## 📁 Project Structure

```
chatbot-using-rasa-nlu/
├── data/
│   ├── nlu.yml              # Training data - user intents and examples
│   ├── stories.yml           # Conversation flow patterns
│   └── rules.yml             # Deterministic single-turn rules
├── actions/
│   └── actions.py            # Custom action server (placeholder)
├── models/                   # Trained model files
├── templates/
│   └── index.html            # Web chat interface
├── tests/
│   └── test_stories.yml      # Automated test conversations
├── app.py                    # Flask web server
├── config.yml                # NLU pipeline and policy configuration
├── domain.yml                # Intents, responses, and session config
├── credentials.yml           # Channel configurations (REST, SocketIO)
├── endpoints.yml             # Action server and tracker store config
├── requirements.txt          # Python dependencies
└── README.md
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| NLU Engine | Rasa NLU (DIET Classifier) |
| Dialogue Management | Rasa Core (TED Policy, Memoization Policy) |
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| API | Rasa REST Webhook |

---

## 🚀 Setup Instructions

### Prerequisites

- **Python 3.8 – 3.10** (Rasa requires Python within this range)
- **pip** (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/quotes-recommendation-chatbot.git
cd quotes-recommendation-chatbot
```

### Step 2: Create a Virtual Environment

```bash
python -m venv rasa_env
```

Activate the virtual environment:

- **Windows (PowerShell):**
  ```powershell
  .\rasa_env\Scripts\Activate
  ```
- **macOS / Linux:**
  ```bash
  source rasa_env/bin/activate
  ```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Train the Model (Optional)

A pre-trained model is included in the `models/` directory. To retrain:

```bash
rasa train
```

### Step 5: Run the Chatbot

You need **two terminals** (both with the virtual environment activated):

**Terminal 1 — Start the Rasa Server:**
```bash
rasa run --enable-api --cors "*"
```

**Terminal 2 — Start the Flask Web App:**
```bash
python app.py
```

### Step 6: Open the Chat Interface

Open your browser and go to:

```
http://localhost:5000
```

Start chatting! Try messages like:
- *"hi"*
- *"motivate me"*
- *"give me a love quote"*
- *"make me laugh"*
- *"quotes on success"*

---

## 🧪 Testing

### Interactive Testing (Rasa Shell)

```bash
rasa shell
```

### Automated Testing (Test Stories)

```bash
rasa test
```

---

## 🤖 Supported Intents

| Intent | Example User Messages |
|--------|----------------------|
| `greet` | "hi", "hello", "good morning" |
| `goodbye` | "bye", "see you", "take care" |
| `motivation` | "motivate me", "I need a push", "feeling low" |
| `inspiration` | "inspire me", "I feel lost", "need clarity" |
| `love` | "love quote", "something romantic", "I miss someone" |
| `funny` | "make me laugh", "humor quote", "cheer me up" |
| `success` | "quotes on success", "winning mindset", "ambition quotes" |
| `affirm` | "yes", "sure", "give me more" |
| `deny` | "no", "enough", "maybe later" |
| `bot_challenge` | "are you a bot?", "are you real?" |

---

## 📜 License

This project is developed for educational purposes as part of a college project.

---

## 🙌 Acknowledgements

- [Rasa Open Source](https://rasa.com/) — Conversational AI framework
- [Flask](https://flask.palletsprojects.com/) — Python web framework
- Quote authors — All quotes are attributed to their original authors
