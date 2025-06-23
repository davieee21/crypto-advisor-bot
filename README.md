

````markdown
# 🤖 CryptoBuddy – Your AI-Powered Cryptocurrency Advisor 🌍🚀

**CryptoBuddy** is a beginner-friendly, rule-based Python chatbot designed to simulate how AI can assist with crypto investment decisions. It offers advice based on **profitability** and **sustainability** using predefined cryptocurrency data.

Whether you're exploring AI for the first time or getting your feet wet in crypto, CryptoBuddy is your trusted sidekick! 💬

---

## 🔧 Features

✅ **Conversational Interface** – Chat with the bot using natural language.  
✅ **Profitability Advice** – Recommends coins with rising trends and strong market cap.  
✅ **Sustainability Check** – Identifies environmentally friendly cryptos with high sustainability scores.  
✅ **Trend Analysis** – Lists coins with upward price trends.  
✅ **Custom Rules-Based Logic** – No machine learning needed—pure Python `if-else`.  
✅ **Friendly Personality** – Engages the user with a warm tone and helpful responses.  
✅ **Looped Chat** – Keeps the conversation going until you say `"exit"`.  
✅ **Built-in Disclaimer** – Encourages responsible investing with a risk warning.

---

## 🧠 How It Works

CryptoBuddy uses a predefined dataset of three popular cryptocurrencies: **Bitcoin**, **Ethereum**, and **Cardano**.

```python
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    ...
}
````

The chatbot then uses keyword detection (`any()` with `if-else`) to match user input with specific query types:

* **Profitability Queries:** e.g., "Which coin is profitable?" → looks for rising price + high market cap.
* **Sustainability Queries:** e.g., "Which crypto is eco-friendly?" → looks for low energy use + high sustainability score.
* **Trend Queries:** e.g., "What's trending up?" → lists coins with price\_trend = "rising".

---

## 🖥️ How to Use

### ✅ Prerequisites

* Python 3.x installed
* VS Code, Google Colab, or Jupyter Notebook

### 🚀 Run the Bot

1. Clone the repo:

```bash
git clone https://github.com/davieee21/crypto-advisor-bot.git
cd crypto-advisor-bot
```

2. Run the script:

```bash
python crypto_advisor_bot.py
```

3. Start chatting!

```text
👋 Hello! I'm CryptoBuddy — your AI-powered crypto sidekick!
💡 Ask me about crypto trends, profitability, or sustainability.
🛑 Type 'exit' anytime to end our chat.
```

---

## 🎥 Demo & Screenshots

📸 Screenshots and a screen recording demo are included in the LMS submission.

---

## ⚠️ Disclaimer

> CryptoBuddy is a logic-based assistant meant for learning purposes.
> It **does not provide financial advice**. Always do your own research (DYOR) before investing in cryptocurrencies.

---

## 🧠 Summary (AI Learning Perspective)

CryptoBuddy mimics basic AI by analyzing user input, identifying intent, and applying rule-based logic to return data-driven advice. This simple chatbot introduces foundational AI concepts like pattern recognition, keyword mapping, and decision trees—**without using machine learning**.

---

## 📬 Author

Made with ❤️ by [Davis Ongeri](https://github.com/davieee21)
For the **PLP AI/ML Week 1 Assignment**