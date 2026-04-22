# AlgoTradez Bot - Main Entry Point
# Author: Anthony Meza (@decryptingmymind)

import time
import logging
from webhook import start_webhook
from config import CONFIG

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler('../logs/bot.log'),
        logging.StreamHandler()
    ]
)

log = logging.getLogger(__name__)

def main():
    log.info("🚀 AlgoTradez Bot Starting...")
    log.info(f"Broker: {CONFIG['broker']}")
    log.info(f"Mode: {CONFIG['mode']}")
    start_webhook()

if __name__ == "__main__":
    main()