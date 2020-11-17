import pygame
import time
from numpy import load


sc= "/home/pi/test/"

d = open(sc + "data.txt", "r")
file1 = sc + "Alarm4.mp3"
file2 = sc + "Alarm8.mp3"
file3 = sc + "Alarm12.mp3"

def readtime():
        i = 0
        for x in d:
            i = i+1
            if i == 6:
                return x
    
def choose():
        t = readtime()
        if t == "4":
            files = file1
        elif t == "8":
            files = file2
        elif t == "12":
            files = file3
        return files
        
def play():
        F = choose()
        while True:
            #print("run again")
            try:
                status = load(sc+ "sign.npy")
                print(status)
                if status == 1:
                    print("alarm")
                    pygame.mixer.init()
                    pygame.mixer.music.load(F)
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue
            except IOError:
                print("Oops IO Error!")
            except ValueError:
                print("Oops Value Error!")
            
            time.sleep(1)

if __name__ == "__main__":
    play()