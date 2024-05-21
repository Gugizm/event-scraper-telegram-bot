import logging

# Configure logging
logger = logging.getLogger(__name__)

# Import modules
from .abstract_classes import AbstractScraper
from .scraper import EventScraper