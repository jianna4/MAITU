import os
from dotenv import load_dotenv

load_dotenv()
print("DeepSeek API Key:", os.getenv("DEEPSEEK_API_KEY"))
