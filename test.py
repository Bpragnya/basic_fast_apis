import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
print(os.getenv('DATABASE_URL'))

print(os.environ.get("DATABASE_URL"))