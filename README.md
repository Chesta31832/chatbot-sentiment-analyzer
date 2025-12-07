# 🤖 Chatbot With Sentiment Analysis

A conversational AI system that maintains full dialogue history and performs conversation-level and message-level sentiment analysis.
This project fulfills **Tier 1 (mandatory)** and **Tier 2 (additional credit)** requirements of the assignment.

🌐 **Live Demo:**
[https://chatbot-sentiment-analyzer-gjqyayywrxbgftquzs72td.streamlit.app/](https://chatbot-sentiment-analyzer-gjqyayywrxbgftquzs72td.streamlit.app/)

---

## 📌 Features

### ✅ Tier 1 — Conversation-Level Sentiment Analysis
*   **Tracks the full conversation** between the user and chatbot.
*   **Computes overall sentiment** at the end:
    *   Positive
    *   Neutral
    *   Negative
*   Uses averaged sentiment polarity across all user messages.

### ⭐ Tier 2 — Statement-Level Sentiment Analysis (Implemented)
*   **Performs sentiment classification** for every individual user message.
*   **Displays results in real time**.
*   Categorizes message polarity using thresholds.

### (Bonus) Mood Trend Summary:
*   Detects whether user’s mood **improved**, **worsened**, or **stayed stable** over the conversation.

---

## 🧠 Chatbot Logic
*   **Lightweight rule-based and sentiment-influenced** conversation handling.
*   Responses are **contextual** and maintain conversation history.

---

## 🎨 UI (Streamlit)
*   Clean, interactive web interface.
*   Real-time chat panel.
*   Sentiment dashboard.
*   Final summarized sentiment report.

---

## 🚀 Deployment
The project is deployed using **Streamlit Cloud**.

**Live app:**
👉 [https://chatbot-sentiment-analyzer-gjqyayywrxbgftquzs72td.streamlit.app/](https://chatbot-sentiment-analyzer-gjqyayywrxbgftquzs72td.streamlit.app/)

Deployment copies the repository directly into Streamlit Cloud and launches using `streamlit run app.py`.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Frontend/UI** | Streamlit |
| **Chat Logic** | Python |
| **Sentiment Analysis** | VADER (Valence Aware Dictionary and sEntiment Reasoner) |
| **Storage** | In-memory conversation store |
| **Deployment** | Streamlit Cloud |

---

## 📂 Project Structure

```
chatbot-sentiment-analyzer/
├── app.py                # Streamlit UI and chat interface
├── main.py               # CLI Entry Point
├── src/
│   ├── __init__.py
│   ├── chatbot.py            # Chatbot response logic
│   ├── sentiment_analyzer.py # Tier 1 & Tier 2 sentiment logic
│   ├── conversation_manager.py # History & Stats
│   └── utils.py              # Helpers & preprocessing
├── tests/
│   ├── test_chatbot.py
│   └── test_sentiment.py     # Unit tests
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run Locally

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Chesta31832/chatbot-sentiment-analyzer.git
    cd chatbot-sentiment-analyzer
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit app**
    ```bash
    streamlit run app.py
    ```

    The app will open automatically in your browser at: `http://localhost:8501`

---

## ❤️ Sentiment Analysis Logic

### Message-Level Sentiment (Tier 2)
Each user message is analyzed individually using VADER:
*   **Polarity < –0.05** → Negative
*   **–0.05 ≤ Polarity ≤ 0.05** → Neutral
*   **Polarity > 0.05** → Positive

These results are displayed alongside each message.

### Conversation-Level Sentiment (Tier 1)
At the end:
1.  Polarity scores of all user messages are averaged.
2.  Final sentiment is categorized as:
    *   **Positive**
    *   **Neutral**
    *   **Negative**
3.  Displayed as the official total sentiment result for the full dialogue.

### 🌀 Mood Trend (Bonus Feature)
A simple slope calculation detects whether sentiment:
*   📈 **Improved**
*   📉 **Declined**
*   ➖ **Stayed steady**

Displayed in the final report.

---

## 🧪 Tests (Optional)
Sample test included:
```bash
pytest
```
Covers:
*   Sentiment thresholds
*   Conversation-level aggregation
*   Handling edge cases (empty/neutral messages)

---

## 🌟 Additional Enhancements
Optional features implemented for bonus credit:
*   Mood trend summarization
*   Clean Streamlit UI
*   Conversation state persistence
*   Modular production-style code layout

---

## 📜 License
MIT License
