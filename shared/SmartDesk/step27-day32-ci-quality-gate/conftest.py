import os

os.environ["OFFLINE"] = "1"          # tests never call a real API
os.environ.pop("OPENAI_API_KEY", None)
