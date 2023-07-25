from pygame import mixer
import tkinter

mixer.init()

mixer.music.load("Tarasti Hai Nigahen_192(PagalWorld.com.se).mp3")

def Volume(i):
    mixer.music.set_volume(1+i)
def Start():
    mixer.music.play()
def Pause():
    mixer.music.pause()
def Stop():
    mixer.music.stop()
def Resume():
    mixer.music.unpause()
    
root = tkinter.Tk()
root.title("Music Player")

label = tkinter.Label(root,text = "Music Player",background="Light Blue",font=("Times New Roman",37))
label.pack(fill="both")

Start_Button = tkinter.Button(root,text = "Start",command=Start,width=10)
Start_Button.pack()

pause_Button = tkinter.Button(root,text = "Pause",command=Pause,width=10)
pause_Button.pack()


Resume_Button = tkinter.Button(root,text = "Resume",command=Resume,width=10)
Resume_Button.pack()

Stop_Button = tkinter.Button(root,text = "Stop",command=Stop,width=10)
Stop_Button.pack()


root.mainloop()