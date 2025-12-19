from supabase import create_client
from dotenv import load_dotenv
import os
from pathlib import Path


load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")


if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError(" ERROR: No se pudo leer SUPABASE_URL o SUPABASE_ANON_KEY desde .env")


SUPABASE_URL = SUPABASE_URL.strip('"')
SUPABASE_KEY = SUPABASE_KEY.strip('"')

print("SUPABASE_URL:", SUPABASE_URL)
print("SUPABASE_KEY:", SUPABASE_KEY[:5] + "...")


supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

