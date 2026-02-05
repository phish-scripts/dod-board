# phish.dev

'''
supabase client creation

edit your credentials (like the url, key) here
'''

import os
from supabase import create_client, Client


url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SERVICE_ROLE")
supabase_client: Client = create_client(url, key)