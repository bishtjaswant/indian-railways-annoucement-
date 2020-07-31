import os
import pandas
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text,fileformat):
    mytext = str(text)
    tts= gTTS(text=mytext,lang='hi',slow=False)
    tts.save(fileformat)

def mergeAudio(audiolist):
    combined =AudioSegment.empty()
    for audio in audiolist:
        combined+= AudioSegment.from_mp3(audio)

    return combined



def generateSkeletonAudio():
    # 1 kripaye dhanyasn dijiye
    audio= AudioSegment.from_mp3('railway.mp3')
    start = 88000
    end = 90200
    processd = audio[start:end]
    processd.export("1_hindi.mp3", format="mp3")

    # 2 is from city

    # 3 se chalkar
    audio= AudioSegment.from_mp3('railway.mp3')
    start = 91000
    end = 92100
    processd = audio[start:end]
    processd.export("3_hindi.mp3", format="mp3")


    # 4 is  via city
    

    # 5 k raste
    audio= AudioSegment.from_mp3('railway.mp3')
    start = 91000
    end = 92100
    processd = audio[start:end]
    processd.export("5_hindi.mp3", format="mp3")

    # 6 is to delhi



    # 7  ko jane wali gaadi sankhaya
    audio= AudioSegment.from_mp3('railway.mp3')
    start = 96000
    end = 98900
    processd = audio[start:end]
    processd.export("7_hindi.mp3", format="mp3")

    # 8 is train numbr and name 

    # 9 kuch hi samaye me plateform sankhaya
    audio= AudioSegment.from_mp3('railway.mp3')
    start = 105500
    end = 108200
    processd = audio[start:end]
    processd.export("9_hindi.mp3", format="mp3")

    # 10  is  plateform  number


    # 11 pr aa rhi hain 
    audio= AudioSegment.from_mp3('railway.mp3')
    start = 109000
    end =   112250
    processd = audio[start:end]
    processd.export("11_hindi.mp3", format="mp3")



def generateAnnoucement(file):
    data = pandas.read_excel(file)
    for i,item in data.iterrows():
        # 2 generating from city
        textToSpeech(item['from'],'2_hindi.mp3')

        # 4 generating via city
        textToSpeech(item['via'],'4_hindi.mp3')

        # 6 generating to delhi
        textToSpeech(item['to'],'6_hindi.mp3')

        # 8 generating train numbr and name 
        textToSpeech(str(item['train_number']) +" " + item['train_name'],'8_hindi.mp3')

        # 10  generating  plateform  number
        textToSpeech(item['plateform'],'10_hindi.mp3')
        
        # meriging all Audios 
        audiolist= [f"{i}_hindi.mp3"  for i in range(1,12)]
        annoucement= mergeAudio(audiolist)
        annoucement.export(f"announcement_train_number_{item['train_number']}_{i+1}.mp3",format="mp3")


if __name__ == "__main__":
    print('skeleton generating.........')
    generateSkeletonAudio()
    print('generating annoucement.......')
    generateAnnoucement("annoucenent_hindi.xlsx")