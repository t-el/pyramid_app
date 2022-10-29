import os
from supabase.client import create_client,Client
from dotenv import load_dotenv
load_dotenv()
url  = os.environ.get('SUPABASE_URL')
key  = os.environ.get('SUPABASE_KEY')

base : Client = create_client(supabase_url=str(url),supabase_key=str(key))  # type: ignore
base.auth._start_auto_refresh_token(value=3600)
