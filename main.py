import os
from dotenv import load_dotenv
from pydub import AudioSegment
from pydub import effects
from speed import speed_change

load_dotenv()

NAPSTER_KEY = os.getenv("NAPSTER_KEY")
NAPSTER_SECRET = os.getenv("NAPSTER_SECRET")

sound = AudioSegment.from_file("fireflies.mp3", format="mp3")
sound = speed_change(sound, 0.5)
sound = sound.set_frame_rate(1000)

alert = AudioSegment.from_file("alert.mp3", format="mp3")
alert = alert.set_frame_rate(1000)
alert = speed_change(alert, 0.5)

sound = sound.overlay(alert)

sound.export("fireflies_reversed.mp3", format="mp3")