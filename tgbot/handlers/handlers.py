from aiogram import types
from utils.utils import convert, path_to_audio
from services.services import post_audio, get_audio
import time
# import asyncio


async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm impster bot!\nI will be mocking you")


async def tts(message: types.Message):
    post_data = await post_audio(message.text.removeprefix("/tts "))
    job_id = post_data["id"]
    job_url = f"https://play.ht/api/v2/tts/{job_id}"

    get_data = {'output': None}
    while get_data["output"] is None:
        get_data = get_audio(job_url)
        time.sleep(1)

    link = get_data["output"]["url"]
    convert(link)
    await message.answer_voice(voice=types.InputFile(path_to_audio))


async def echo(message: types.Message):
    await message.answer(message.text)
