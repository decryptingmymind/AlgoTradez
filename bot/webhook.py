# AlgoTradez Bot - Webhook Listener
# Receives alerts from TradingView via TradersPost

from flask import Flask, request, jsonify
import logging
import json

app = Flask(__name__)
log = logging.getLogger(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()
        log.info(f"📨 Alert received: {data}")
        
        ticker  = data.get('ticker')
        action  = data.get('action')
        qty     = data.get('quantity')
        price   = data.get('price')

        log.info(f"Ticker: {ticker} | Action: {action} | Qty: {qty} | Price: {price}")

        # TODO: Send to broker
        return jsonify({"status": "received", "ticker": ticker, "action": action}), 200

    except Exception as e:
        log.error(f"❌ Webhook error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "AlgoTradez bot is running ✅"}), 200

def start_webhook():
    from config import CONFIG
    host = CONFIG['webhook']['host']
    port = CONFIG['webhook']['port']
    log.info(f"🌐 Webhook listening on {host}:{port}")
    app.run(host=host, port=port)