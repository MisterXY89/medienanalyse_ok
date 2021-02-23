
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Create .env file path.
dotenv_path = join(dirname(__file__), '.env')

# Load file from the path.
load_dotenv(dotenv_path)

API_KEY = os.getenv('API_KEY')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')

SEARCH_TERM = 'Organisierte Kriminalität OR Organisierte Kriminalitaet'
LANG = "language:de"

FROM_DATE = '2017-01-01'
TO_DATE = '2020-12-31'
