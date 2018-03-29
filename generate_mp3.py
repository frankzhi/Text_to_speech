from gtts import gTTS
import os
import play
import subprocess


def generateNewMP3(directory, sentence,name):
    '''Generate one piece of new mp3 file '''

    try:
        tts = gTTS(text = '{}'.format(sentence), lang = 'en-us', slow = False)
        if not os.path.exists("./album/{}".format(directory)):
            os.makedirs("./album/{}".format(directory))
        tts.save("./album/{}/{}.mp3".format(directory, name))
        print "{}.mp3 generated.".format(name)


    except UnicodeDecodeError:
        print"Error: Invalid characters cannot be decoded, please check the punctuations in source text!"
        
        


def generateAlbum(filename):
    '''Generate a new mp3 album from selected file'''

    try:
        file = open("{}.txt".format(filename), "r")
        i =1

        for line in file:
            if not line.isspace():         #Skip lines only contain spaces
                generateNewMP3(filename,line,i)
                i+=1
            
        print"TTS completed"
        file.close()


    except IOError:
        
        print "Error: Can't find or fail to read the file, please check again!"
        menu()


def menu():
    '''Generate a menu '''
    
    while True:
        print "====================="
        print "1 generate new mp3"
        print "2 generate new album"
        print "3 play album"
        print "4 end the program"
        print "====================="
        user_input = str(raw_input("Enter the No: "))


        if user_input == "1":
            sentence = str(raw_input("Enter new sentence: "))
            user_choice = str.upper(raw_input("press Y to generate new mp3, press N go back... "))
            if user_choice == "Y":
                generateNewMP3("new_WFD", sentence, "new_wfd")
            else:
                continue
            

        elif user_input == "2":

            filename = raw_input("Enter the file name: ")
            generateAlbum(filename)

        elif user_input == "3":
            albumName = raw_input("Enter the name of album: ")
            countdown = int(input("Enter the countdown time(sec): "))
            play.playAlbum(albumName, countdown)
        

        elif user_input == "4":
            print "End program"
            break
  
        
        else:
            print"Invaid choice"
            continue


menu()
      
            
        








