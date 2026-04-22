# AlgoTradez Bot - Configuration

CONFIG = {
    "broker": "alpaca",
    "mode": "paper",  # Change to "live" when ready
    "alpaca": {
        "api_key": "YOUR_API_KEY",
        "secret_key": "YOUR_SECRET_KEY",
        "base_url": "https://paper-api.alpaca.markets"
    },
    "webhook": {
        "host": "0.0.0.0",
        "port": 5000,
        "secret": "YOUR_WEBHOOK_SECRET"
    },
    "risk": {
        "max_position_size": 0.02,  # 2% per trade
        "max_daily_loss": 0.05      # 5% max daily loss
    }
}