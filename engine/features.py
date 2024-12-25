from playsound import playsound
import eel


#Playing assiatnt sound function
@eel.expose
def playAssistantSound():
    music_dir="www\\assets\\jarvis voice.mp3"
    playsound(music_dir)