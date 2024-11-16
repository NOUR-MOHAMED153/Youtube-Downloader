from pytube import YouTube
from tkinter import filedialog as fl


while True:

    #take url from user:
    url = str(input("Inter video url here : "))

    #take file path from user:
    file_path=fl.askdirectory(title=' Select Folder to Download')
    
    
    #choose video or audio:
    file_ex=input("video or audio : ").lower()
    
    #if user want video:
    if file_ex == "video" or file_ex == "v" :
        #take resolution from user:
        res = str(input("enter video resolution [ 360p , 480p , 720p ]: ")).lower()
        
        #downloading video:
        try:
            print("Downloading video...")
            YouTube(url).streams.get_by_resolution(res).download(file_path)
            print("Downloaded.")
        except:
            print("Error url , please try again ")
            
    #if user want audio :
    elif file_ex == "audio" or file_ex == "a":
        #downloading audio:
        try:
            print("Downloading audio...")
            YouTube(url).streams.get_audio_only().download(file_path)
            print("Downloaded.")
        except:
            print("Error url , please try again")
    else :
        print("please choose only audio or video ")
        

    
