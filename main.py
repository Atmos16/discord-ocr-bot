'''

Discord OCR BOT
Created By: RKuangDev

Made with PyTesseract and DiscordPy

'''

#libraries
import io
import os
from keep_alive import keep_alive
import discord
import datetime
import pytesseract
import requests
from PIL import Image
from PIL import ImageFilter
from discord.ext import commands

#Initiation
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
# client = discord.Client(intents=discord.Intents.all()) # 
imageFileTypes = ['png', 'jpg', 'jpeg']

#Grabbing List of Channel IDs
# def storedChannelIDs():
#     idList = []
#     with open ("channel ID.txt", "r") as file:
#         for id in file:
#             idList.append(int(id.strip()))
#     return idList

#OCR Function Proccess Image and Print Text
def OCRImage(imageLink):
    response = requests.get(imageLink)
    img = Image.open(io.BytesIO(response.content))
    text = pytesseract.image_to_string(img, lang='eng+kor+jpn+tha')
    return text

# def getToken():
#     with open("token.txt","r") as tokenFile:
#         token = tokenFile.readline()
#         return token
token = os.getenv("DISCORD_TOKEN") # renderで入力かな
    
#Calling Channel Id function + Prompt
# よくわからないので全部消す
# token = getToken()
# channelIDList = storedChannelIDs()
# print("\nLoaded Channel IDs:")
# for x in channelIDList:
#     print(x)

@client.event
async def on_message(message):
    # #Check if message's channel id in channel id filter
    # if message.channel.id in channelIDList:
        
    #checks for attachments
    if message.attachments:
        # print(message.content)
        # print(message.attachments[0])
        
        #stores url to image
        link = message.attachments[0].url
        linkTemp = message.attachments[0].url
        
        #checks if attachment is image type
        fileType = linkTemp.split(".")
        
        #if it is an image type
        if fileType[-1].lower().split("?")[0] in imageFileTypes:
            
            #Log Url to console
            print(f"[{datetime.datetime.now()}] {link}")
            
            #calls OCR function
            content = OCRImage(link)
            
            #if content is not empty send embed
            if content:
                
                #Embed formatting
                embed=discord.Embed()
                embed.colour = 0x725E7A
                embed.set_author(name="Discord OCR")
                embed.add_field(name="Content:", value=content, inline=True)
                # embed.set_footer(text="Made By: RKuangDev - GitHub")
                await message.channel.send(embed=embed)
     
# Web サーバの立ち上げ
keep_alive()         
client.run(token,bot=True)