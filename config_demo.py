import os
from dotenv import load_dotenv

load_dotenv()

app_name = os.getenv("APP_NAME")
environment = os.getenv("ENVIRONMENT")
api_timeout = os.getenv("API_TIMEOUT")

print(f"The app name: {app_name}")
print(f"The environment: {environment}")
print(f"The api_tmout: {api_timeout}")
# for numeric
api_timeout = int(os.getenv("API_TIMEOUT"))
print(f"The integer api_tmout: {api_timeout}")
