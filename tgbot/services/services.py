from dotenv import load_dotenv
import requests
import os


load_dotenv(dotenv_path=".venv/.env")
ID = os.getenv("ID")
API_KEY = os.getenv("API_KEY")


async def post_audio(text):
    url = "https://play.ht/api/v2/tts"
    HEADERS = {
        "accept": "application/json",
        "content-type": "application/json",
        "AUTHORIZATION": API_KEY,
        "X-USER-ID": ID,
    }
    payload = {
        "quality": "medium",
        "output_format": "mp3",
        "speed": 1,
        "sample_rate": 24000,
        "text": text,
        "voice": "s3://voice-cloning-zero-shot/1899a815-dacf-4987-94cb-cd3c2c489a16/kassym-0/manifest.json",
    }
    response = requests.post(url, json=payload, headers=HEADERS)
    assert response.status_code == 201
    result = response.json()
    return result



def get_audio(job_url):
    get_headers = {
        "accept": "application/json",
        "AUTHORIZATION": API_KEY,
        "X-USER-ID": ID,
    }
    response = requests.get(job_url, headers=get_headers)
    assert response.status_code == 200
    return response.json()
