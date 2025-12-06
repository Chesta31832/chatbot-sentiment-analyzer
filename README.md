# Chatbot with Sentiment Analysis

A Python-based conversational chatbot that performs real-time sentiment analysis on user messages. This project analyzes emotions in conversations and provides insights into the overall conversation mood.

## Features

- **Real-time Sentiment Analysis**: Analyzes each user message using VADER sentiment analysis.
- **Dynamic Responses**: The chatbot adapts its responses based on the detected sentiment (Positive, Negative, Neutral).
- **Conversation Tracking**: Maintains a history of the conversation and calculates overall sentiment trends.
- **Visual Feedback**: Uses color-coded terminal output to indicate sentiment (Green for positive, Red for negative, Yellow for neutral).
- **Summary Statistics**: Provides a conversation summary with sentiment trends upon exit.

## Project Structure

```
chatbot-sentiment-analyzer/
├── src/
│   ├── __init__.py
│   ├── chatbot.py              # Rule-based chatbot logic
│   ├── conversation_manager.py # Manages history and statistics
│   ├── sentiment_analyzer.py   # VADER analysis wrapper
│   └── utils.py                # UI and formatting utilities
├── tests/                      # Unit tests
├── main.py                     # Application entry point
├── requirements.txt            # Project dependencies
└── README.md
```

## Installation

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone https://github.com/Chesta31832/chatbot-sentiment-analyzer.git
   cd chatbot-sentiment-analyzer
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main application:

```bash
python main.py
```

Type your messages to chat with the bot. Type `quit`, `exit`, or `bye` to end the conversation and see the summary.

## Testing

Run the test suite to ensure everything is working correctly:

```bash
pytest
```

## Technologies Used

- **Python 3.x**
- **VADER Sentiment**: For lexicon and rule-based sentiment analysis.
- **Colorama**: For cross-platform colored terminal text.
- **Pytest**: For unit testing.
