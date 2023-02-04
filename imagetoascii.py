import ascii_magic
import pickle
import os
import time
from tqdm import tqdm
import sys
import fpstimer
from pathlib import Path
from playsound import playsound
import play_reference

timer=fpstimer.FPSTimer(30)
number=-1
numberdisplay=-1
path=Path('C:/Users/roger/Desktop/Scripts/filename.pickle5999')

if path.is_file() == False:
    for i in tqdm(range(6000), desc="Converting Frames"):

        number = number+1
        output=ascii_magic.from_image_file("C:/Users/roger/Desktop/Scripts/Python/BAD_APPLE/data/frame{}.jpg".format(number))
        #ascii_magic.to_terminal(output)

        with open('filename.pickle{}'.format(number), 'wb') as handle:
            pickle.dump(output, handle, protocol=pickle.HIGHEST_PROTOCOL)
else:
    print("File already created")

for countdown in range(5):
    print("starting in " + str(countdown))
    time.sleep(0.5)
playsound("C:/Users/roger/Desktop/Scripts/Python/BAD_APPLE/badapple.mp3", block=False)
for frame in range(6000):
    numberdisplay=numberdisplay+1
    with open('filename.pickle{}'.format(numberdisplay), 'rb') as handle:
        b = pickle.load(handle)     
    sys.stdout.write("\r" + str(b))
    os.system('cls')
    timer.sleep()
    play_reference.playVideo()

