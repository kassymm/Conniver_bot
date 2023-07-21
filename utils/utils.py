import requests
import io
from pydub import AudioSegment


path_to_audio = "/Users/kassym/development/nFactorial/tgbot/audio/voice.opus"
# url = "https://play.ht/api/v1/convert"
# tts_url = "https://play.ht/api/v2/tts"


def convert(url):
    # Download the MP3 file
    mp3_data = requests.get(url).content

    # Load the MP3 data as an audio segment
    audio = AudioSegment.from_file_using_temporary_files(io.BytesIO(mp3_data), format="mp3")
    audio.export(path_to_audio, format='opus', parameters=['-ar', '48000', '-ac', '2'])


