from dotenv import load_dotenv
import os

load_dotenv()

print("Python app running...")
print("Loaded API Key:", os.getenv("PY_API_KEY"))
