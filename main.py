from app import create_app
from dotenv import load_dotenv
import os

app = create_app()

env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(env_path)

if __name__ == "__main__":
    app.run(debug=os.getenv("DEV_MODE"))
