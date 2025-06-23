# crypto_advisor_bot.py

# Step 1: Dataset
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

# Step 2: Personality Intro
print("👋 Hello! I'm CryptoBuddy — your AI-powered crypto sidekick!")
print("💡 Ask me about crypto trends, profitability, or sustainability.")
print("🛑 Type 'exit' anytime to end our chat.\n")

# Step 3: User Interaction Loop
# Better keyword detection by checking presence of similar keywords

while True:
    user_query = input("You: ").lower()

    if user_query == "exit":
        print("👋 Bye! Remember: Always DYOR (Do Your Own Research) before investing.")
        break

    elif any(word in user_query for word in ["sustainable", "sustainability", "eco-friendly"]):
        best = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"🌱 CryptoBuddy: {best} is the most sustainable crypto with a score of {crypto_db[best]['sustainability_score']*10}/10.")

    elif any(word in user_query for word in ["trend", "trending", "rising", "up"]):
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        print(f"📈 CryptoBuddy: These cryptos are trending up: {', '.join(trending)}.")

    elif any(word in user_query for word in ["profit", "invest", "profitable", "money"]):
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                print(f"💰 CryptoBuddy: For profit, go with {coin} — it's rising and has a strong market cap!")
                break
        else:
            print("🤔 CryptoBuddy: No ideal match right now, but keep an eye on market trends!")

    else:
        print("❓ CryptoBuddy: I didn’t quite get that. Ask about sustainability, trends, or profitability.")


# Disclaimer (already shown on exit)
