import os
import eel

from engine.features import *

eel.init("www")

playAssistantSound()

os.system('start msedge.exe --app="http://localhost:8000/www/index.html"')

# os.system("open /Applications/Safari.app --app http://localhost:8000/www/index.html")

eel.start('index.html',mode=None,host='localhost',block=True)

