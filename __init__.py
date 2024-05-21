import logging
from logging.handlers import RotatingFileHandler
import os

# Configure logging
if not os.path.exists('logs'):
    os.makedirs('logs')

log_file = os.path.join('logs', 'app.log')
file_handler = RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=5)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

# Import modules
from . import manage
from . import scraper
from . import bot

# Import configuration
from . import config