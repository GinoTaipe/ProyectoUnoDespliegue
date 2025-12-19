from dotenv import load_dotenv
import os
from pathlib import Path

dotenv_path = Path(__file__).parent / ".env"
print("¿Existe el .env?", dotenv_path.exists())

load_dotenv(dotenv_path=dotenv_path)

print("SUPABASE_URL =", os.getenv("SUPABASE_URL"))
print("SUPABASE_KEY =", os.getenv("SUPABASE_ANON_KEY"))