import sys
import logging
import torch

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(name)s:%(message)s', force=True)
logger = logging.getLogger(__name__)
logger.info("Starting CTF Assistant application with OpenHermes model...")
logger.info("Python version: %s", sys.version.replace("\n", " "))
logger.info("Torch version: %s", torch.__version__)
try:
    logger.info("Script path: %s", os.path.abspath(__file__))
except NameError:
    logger.info("Script path: Running in interactive environment (e.g., Jupyter)")
logger.info("Python executable: %s", sys.executable)
