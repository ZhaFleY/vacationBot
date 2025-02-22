import os
from dotenv import load_dotenv


load_dotenv()

token = os.getenv("token")
db_url = os.getenv("db_url")