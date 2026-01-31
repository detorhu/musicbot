import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")  # string ya file-based session
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

MONGO_URI = os.getenv("MONGO_URI")  # optional
