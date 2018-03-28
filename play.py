from playsound import playsound
import time
import os



def playAlbum(album, countdown):
    '''Play a selected album'''
    
    i = 1
    numfiles = len([f for f in os.listdir("./album/{}".format(album)) if f[0] != '.'])
    
    for i in range(i,numfiles+1):
        print "No.{}".format(str(i))
        playsound("./album/{}/{}.mp3".format(album, str(i)))

        countDown(countdown)
        albumText = open("{}.txt".format(album), "r")
        lines = albumText.readlines()
        print lines[i-1]

        countDown(3)

def countDown(countdown):
    '''count down seconds'''
    
    for count in reversed(range(1, countdown+1)):
            print count 
            time.sleep(0.95)

##playAlbum("wfd_Dec",3)



