import logging
from datetime import datetime
import os

if not os.path.exists("logs"):
    os.makedirs("logs")

log_filename = f"logs/pipeline_{datetime.now().strftime('%Y-%m-%d')}.log"

logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console.setFormatter(formatter)
logging.getLogger("").addHandler(console)
