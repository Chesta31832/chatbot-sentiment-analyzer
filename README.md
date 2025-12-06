# Chatbot with Sentiment Analysis

A Python-based chatbot that conducts conversations and performs real-time sentiment analysis on user messages.

## Features

### Tier 1 (Mandatory) ✅
- Full conversation history tracking
- Overall conversation sentiment analysis
- Clear emotional direction indication

### Tier 2 (Additional Credit) ✅
- Statement-level sentiment analysis for each message
- Real-time sentiment display
- Sentiment trend analysis and mood shift detection

## Technologies Used

- **Python 3.8+**: Core programming language
- **VADER Sentiment**: Primary sentiment analysis (optimized for social media/conversational text)
- **TextBlob**: Secondary sentiment validation
- **Colorama**: Terminal color output for better UX
- **Pytest**: Unit testing framework

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd chatbot-sentiment-analyzer

# Install dependencies
pip install -r requirements.txt

# Download TextBlob corpora
python -m textblob.download_corpora
```

## How to Run

```bash
python main.py
```

Type your messages and the chatbot will respond. Type 'quit', 'exit', or 'bye' to end the conversation and view the final sentiment analysis.

## Sentiment Logic

### Individual Message Analysis (Tier 2)
- Uses VADER (Valence Aware Dictionary and sEntiment Reasoner)
- Compound score ranges: -1 (most negative) to +1 (most positive)
- Classification:
  - Positive: compound score ≥ 0.05
  - Negative: compound score ≤ -0.05
  - Neutral: -0.05 < compound score < 0.05

### Overall Conversation Sentiment (Tier 1)
- Calculates weighted average of all message sentiments
- Provides sentiment trend analysis
- Detects mood shifts (improving/declining/stable)

## Project Structure

