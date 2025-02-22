import logging

logging.basicConfig(
    level=logging.INFO,
    filename='logs/logfile.log',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger()