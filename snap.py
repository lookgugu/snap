from guizero import App, Box, Picture, PushButton, Text, MenuBar, Window, TextBox
import os
from random import shuffle, randint

emojoi_dir = "emojis"
emojis = [os.path.join(emojoi_dir, f) for f in os.listdir(emojoi_dir) if os.path.isfile(os.path.join(emojoi_dir, f))]
shuffle(emojois)

app = App("Snap!", height=350)
rulewindow = 