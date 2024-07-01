from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
import requests
import json
import subprocess
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message
from pyrogram import Client, filters
from p_bar import progress_bar
from subprocess import getstatusoutput
from aiohttp import ClientSession
import helper
from helper import get_drm_keys
from logger import logging
import time
import asyncio
from pyrogram.types import User, Message
from config import *
import sys
import os
import random
import re
import tempfile
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup
import datetime
import aiohttp

bot = Client("bot",
             bot_token= "6556042495:AAEYgNL0EDhqpA7P6SLJ-dzFath0q7gzttA", 
             #bot_token= os.environ.get("BOT_TOKEN"),
             api_id= 28590119,
             api_hash= "2494557bf21e6c5152f26070aa1a97c7")
auth_users = [1923922961,6200710535,5753557653,6404553499]
#romeo  -1923922961 

owner_id = 1923922961
# Extras 
failed_links = []  # List to store failed links
fail_cap =f"**➜ This file Contain Failed Downloads while Downloding \n You Can Retry them one more time **"

# counter 
global videocount, pdfcount  # Declare videocount and pdfcount as global variables

#url var 
pwdl = os.environ.get("api")

processing_request = False  # Variable to track if a request is being processed


keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="👨🏻‍💻 Devloper",
                url="https://t.me/ITS_NOT_ROMEO",
            ),
            InlineKeyboardButton(
                text="❣️ GITHUB",
                url="https://github.com/Devansh20055",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🪄 Updates Channel",
                url="https://t.me/TEAM_SILENT_KING_OG",
            ),
            
        ],
    ]
)



Busy = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="👨🏻‍💻 Devloper",
                url="https://t.me/ITS_NOT_ROMEO",
            ),
            InlineKeyboardButton(
                text="❣️ GITHUB",
                url="https://github.com/Devansh20055",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Join to Check My Status ",
                url="https://t.me/+R3s25D9fxYtiMTE1",
            ),
            
        ],
    ]
)


@bot.on_message(filters.command(["logs"]) )
async def send_logs(bot: Client, m: Message):
    try:
        
        # Assuming `assist.txt` is located in the current directory
         with open("Assist.txt", "rb") as file:
            sent= await m.reply_text("**📤 Sending you ....**")
            await m.reply_document(document=file)
            await sent.delete(True)
    except Exception as e:
        await m.reply_text(f"Error sending logs: {e}")


# List of image URLs
image_urls = [
    "https://graph.org/file/9dbe3901f43b11e98e6f0.jpg",
    "https://graph.org/file/c5ec0a02be408b354d3fc.jpg",
    "https://graph.org/file/c186818a566c501f14abf.jpg",
    "https://graph.org/file/850ef256ede1370257b5d.jpg",
    "https://graph.org/file/40700542e58889b5c42fe.jpg",
    "https://graph.org/file/94a7875bb51006e7bd528.jpg",
    # Add more image URLs as needed
]



@bot.on_message(filters.command(["start"]))
async def start_command(bot: Client, message: Message):
    # Choose a random image URL from the list
    random_image_url = random.choice(image_urls)
    
    
    # Caption for the image
    caption = f"**𝐇𝐞𝐥𝐥𝐨 𝐃𝐞𝐚𝐫  👋!\n\n➠ 𝐈 𝐚𝐦 𝐚 𝐓𝐞𝐱𝐭 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 𝐁𝐨𝐭 𝐌𝐚𝐝𝐞 𝐖𝐢𝐭𝐡 ♥️\n➠ Can Extract Videos & Pdf Form Your Text File and Upload to Telegram\n\n➠ 𝐔𝐬𝐞 /drm 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐅𝐫𝐨𝐦 𝐓𝐗𝐓 𝐅𝐢𝐥𝐞  \n\n➠𝐌𝐚𝐝𝐞 𝐁𝐲: @ITS_NOT_ROMEO **\n"
    
    # Send the image with the caption
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=random_image_url,
        caption=caption,
        reply_markup=keyboard
    )

@bot.on_message(filters.command('h2t'))
async def run_bot(bot: Client, m: Message):
    user_id = m.from_user.id
    if user_id not in auth_users:
        await m.reply_text("**HEY BUDDY THIS IS ONLY FOR MY ADMINS TO USE THIS CONATCH MY DEV : @ITS_NOT_ROMEO  **")
    else:
        editable = await m.reply_text(" Send Your HTML file\n")
        input: Message = await bot.listen(editable.chat.id)
        html_file = await input.download()
        await input.delete(True)
        await editable.delete()
        with open(html_file, 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')
            tables = soup.find_all('table')
            videos = []
            for table in tables:
                rows = table.find_all('tr')
                for row in rows:
                    cols = row.find_all('td')
                    name = cols[0].get_text().strip()
                    link = cols[1].find('a')['href']
                    videos.append(f'{name}:{link}')
        txt_file = os.path.splitext(html_file)[0] + '.txt'
        with open(txt_file, 'w') as f:
            f.write('\n'.join(videos))
        await m.reply_document(document=txt_file,caption="Here is your txt file.")
        os.remove(txt_file)



def is_subscription_expired(user_id):
    with open("Subscription_data.txt", "r") as file:
        for line in file:
            data = line.strip().split(", ")
            if int(data[0]) == user_id:
                end_date = datetime.datetime.strptime(data[2], "%d-%m-%Y") #%Y-%m-%d
                today = datetime.datetime.today()
                return end_date < today
    return True  # User not found in Subscription_data.txt or no subscription data found



# Define the myplan command handler
@bot.on_message(filters.command("myplan"))
async def myplan_command_handler(bot, message):
    user_id = message.from_user.id
    with open("Subscription_data.txt", "r") as file:
        for line in file:
            data = line.strip().split(", ")
            if int(data[0]) == user_id:
                subscription_start = data[1]
                expiration_date = data[2]
                today = datetime.datetime.today()
                if today > datetime.datetime.strptime(expiration_date, "%d-%m-%Y"):
                    plan = "EXPIRED "
                    response_text = f"**✨ User ID: {user_id}\n📊 PLAN STAT : {plan}\n\n🔰 Activated on : {subscription_start}\n🧨 Expiration Date: {expiration_date} \n\n 🫰🏼 ACTIVATE YOUR PLAN NOW ! \n⚡️ TO ACTIVATE MESSAGE : @ITS_NOT_ROMEO :D **"
                else:
                    plan = "ALIVE!"  
                    response_text = f"**✨ User ID: {user_id}\n📊 PLAN STAT : {plan}\n🔰 Activated on : {subscription_start}\n🧨 Expiration Date: {expiration_date}**"
                await message.reply(response_text)
                return
    if user_id in auth_users:
        await message.reply("YOU HAVE LIFE TIME ACCESS :) ")
    else:
        await message.reply("No subscription data found for you.")


@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    
        if failed_links:
         error_file_send = await m.reply_text("**📤 Sending you Failed Downloads List Before Stoping   **")
         with open("failed_downloads.txt", "w") as f:
          for link in failed_links:
            f.write(link + "\n")
    # After writing to the file, send it
         await m.reply_document(document="failed_downloads.txt", caption=fail_cap)
         await error_file_send.delete()
         os.remove(f'failed_downloads.txt')
         failed_links.clear()
         processing_request = False  # Reset the processing flag
         #await m.reply_text("**Note This Is BETA Stage May have Bugs  **")
         await m.reply_text("🚦**STOPPED**🚦", True)
         os.execl(sys.executable, sys.executable, *sys.argv)
        else:
         processing_request = False  # Reset the processing flag
         #await m.reply_text("**Note This Is BETA Stage May have Bugs  **")
         await m.reply_text("🚦**STOPPED**🚦", True)
         os.execl(sys.executable, sys.executable, *sys.argv)
   

@bot.on_message(filters.command("restart"))
async def restart_handler(_, m):
   
     processing_request = False  # Reset the processing flag
     await m.reply_text("🤖**Restarting Bot **🤖", True)
     os.execl(sys.executable, sys.executable, *sys.argv)
    

@bot.on_message(filters.command(["drm"]))
async def account_login(bot: Client, m: Message):
    global processing_request
    if m.from_user.id not in auth_users:
            await m.reply_text("** YOU ARE NOT IN ADMIN LIST **",reply_markup=keyboard)
            return

    if processing_request:
            await m.reply_text("**🫨 I'm currently processing another request.\n Please try again later.**",reply_markup=Busy)
            return
    else:
        
        editable = await m.reply_text(f"**➠ 𝐒𝐞𝐧𝐝 𝐌𝐞 𝐘𝐨𝐮𝐫 𝐓𝐗𝐓 𝐅𝐢𝐥𝐞 𝐢𝐧 𝐀 𝐏𝐫𝐨𝐩𝐞𝐫 𝐖𝐚𝐲 \n\n➠ TXT FORMAT : LINK : URL \n➠ 𝐌𝐨𝐝𝐢𝐟𝐢𝐞𝐝 𝐁𝐲: @ITS_NOT_ROMO **")
        input: Message = await bot.listen(editable.chat.id)
        editable = await editable.edit(f"**⚙️PROCESSING INPUT.......**")

        if input.document:
            processing_request = True
            x = await input.download()        
            await input.delete(True)
            file_name, ext = os.path.splitext(os.path.basename(x))
            credit = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
            path = f"./downloads/{m.chat.id}"

            try:
                links = []
                videocount = 0
                pdfcount = 0
                with open(x, "r", encoding="utf-8") as f:
                    for line in f:
                        link = line.strip().split("://", 1)
                        links.append(link)
                        if ".pdf" in link[1]:
                            pdfcount += 1 
                        else:
                            videocount += 1
            except Exception as e:
                await m.reply_text("Error occurred while processing the file.🥲")
                print("Error:", e)
                os.remove(x)
                processing_request = False  # Reset the processing flag
                return

        else:
            content = input.text
            content = content.split("\n")
            links = []
            videocount = 0
            pdfcount = 0

            for i in content:
                link = i.split("://", 1)
                links.append(link)
                if ".pdf" in link[1]:
                    pdfcount += 1 
                else:
                    videocount += 1
    await editable.edit(f"**Total links found are : {len(links)}\n┃\n┠ Total Video Count : {videocount}\n┠ Total Pdf Count: {pdfcount}  \n┠ Send From where you want to download initial is  : `1` \n┃\n┠ Send `stop` If don't want to Contine \n┖ Bot By : @ITS_NOT_ROMEO**" )
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)
    if raw_text.lower() == "stop":
        await editable.edit(f"**Task Stoped ! **")
        await input0.delete(True)
        processing_request = False  # Reset the processing flag
        os.remove(x)
        return
    

    await editable.edit(f"**ENTER TILL WHERE YOU WANT TO DOWNLOAD \n┃\n┠ Starting Dowload Form : `{raw_text}`\n┖ Last Index Of Links is : `{len(links)}` **")
    input9: Message = await bot.listen(editable.chat.id)
    raw_text9 = input9.text
    
    if int(input9.text) > len(links) :
        await editable.edit(f"**PLZ ENTER NUMBER IN RANGE OF INDEX COUNT    **")
        processing_request = False  # Reset the processing flag
        await m.reply_text("**Exiting Task......  **")
        return
    else: await input9.delete(True)
    


    await editable.edit("**Enter Batch Name or send d for grabbing from text filename.**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    if raw_text0 == 'd':
        b_name = file_name
    else:
        b_name = raw_text0


    # await editable.edit("**Enter resolution \n SEND 1 for 720p \n 2 for 480 \n 3 for 360 \n 4 for 240**")
    await editable.edit("**Enter resolution \n SEND 1 for 720p \n 2 for 480 \n 3 for 360 \n 4 for 240**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    quality = input2.text
    await input2.delete(True)
    
    
    await editable.edit("**Enter Your Name or send `de` for use default**")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    if raw_text3 == 'de':
        CR = "@ITS_NOT_ROMEO"
    else:
        CR = raw_text3


    await editable.edit("**🖼 Thumbnail \n\n• Custom Thumbnail : Use @vtelegraphbot and send me link \n• If you don't want Send :  `no` **")  
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    #await editable.delete()
    thumb = input6.text
    thumb2 = input6.text

    await editable.edit("**⚡️ Thumnail in PDF too ? \n\n• If need Same thumb on pdf as video send : `yes` \nNOTE : if you have given stumb for Video then only use this   \n• SEND `no` If you dont want to add \n\n• Want other thumbnail ? \n\n• Send `custom`  IF need Different thubnail for pdf **")  
    input7 = message = await bot.listen(editable.chat.id)
    raw_text7 = input7.text.lower()  # Convert to lowercase
    await input7.delete(True)
    

    if raw_text7 == "custom":
     await editable.edit("**Send URl of Pdf Thumbanil **")  
     input8 = message = await bot.listen(editable.chat.id)
     raw_text8 = input8.text.lower()  # Convert to lowercase
     await input8.delete(True)
     await editable.delete()
     thumb3 = input8.text 

    else: await editable.delete() 
      
    
    if thumb.startswith("http://") or thumb.startswith("https://"):
        # getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        getstatusoutput(f"wget {thumb} -O thumb1.jpg")
        thumb = "thumb1.jpg"
    else:
        thumb == "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)
  
    try:
        for i in range(count - 1, int(input9.text)):
        #for i in range(count - 1, len(links)):    

            V = links[i][1].replace("file/d/","uc?export=download&id=")\
               .replace("www.youtube-nocookie.com/embed", "youtu.be")\
               .replace("?modestbranding=1", "")\
               .replace("/view?usp=sharing","")\
               .replace("youtube.com/embed/", "youtube.com/watch?v=")

            url = "https://" + V

            if "acecwply" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'

            elif "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url:
             url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0'}).json()['url']


            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip() 
            name = f'{name1[:60]}'

            if "/master.mpd" in url :
                if "https://sec1.pw.live/" in url:
                    url = url.replace("https://sec1.pw.live/","https://d1d34p8vz63oiq.cloudfront.net/")
                    print(url)
                else: 
                    url = url    
                print("mpd check")
                key = await helper.get_drm_keys(url)
                print(key)
                await m.reply_text(f"got keys form api : \n`{key}`")
          
            if "/master.mpd" in url:
                cmd= f" yt-dlp -k --allow-unplayable-formats -f bestvideo.{quality} --fixup never {url} "
                print("counted")
            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"bestvideo.{quality}"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            if "m3u8" or "livestream" in url:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "romeo.mp4"'
                #cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.%(ext)s"'
            else: 
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "romeo.mp4"'
                print("counted 2 ")
            
            # else
            #     cmd = f'yt-dlp -f "{ytf}+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'

            try:   
                cc = f' **➭ Index » {str(count).zfill(3)} **\n**➭ Title »  {name1}.mkv**\n**➭ 𝐁𝐚𝐭𝐜𝐡 » {b_name} **\n**➭ Quality » {raw_text2}**\n\n✨ **𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃𝐄𝐃 𝐁𝐘 : {CR}**\n**━━━━━━━✦✗✦━━━━━━━**'
                cc1 = f'**➭ Index » {str(count).zfill(3)} **\n**➭ Title » {name1}.pdf** \n**➭ 𝐁𝐚𝐭𝐜𝐡 »  {b_name}**\n\n✨ **𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃𝐄𝐃 𝐁𝐘 : {CR}**\n**━━━━━━━✦✗✦━━━━━━━**'                            
               
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        await copy.copy(chat_id = -1002097681261)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e: 
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                elif ".pdf" in url:
                    try:
                        time.sleep(1)
                        #prog = await m.reply_text(f"📥 **Downloading **\n\n**➭ Index » {str(count).zfill(3)} **\n**➭ File » ** `{name}`\n**➭ Link »** `{url}`\n\n✨ **Bot Made by Devansh**\n**━━━━━━━✦✗✦━━━━━━━**")
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        time.sleep(1)
                        #await prog.delete (True)
                        start_time = time.time()
                        reply = await m.reply_text(f"**⚡️ Starting Uploding ...** - `{name}`")
                        time.sleep(1)
                        if raw_text7 == "custom" :
                           subprocess.run(['wget', thumb3, '-O', 'pdfthumb.jpg'], check=True)  
                           thumbnail = "pdfthumb.jpg"
                           copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1, thumb=thumbnail, progress=progress_bar, progress_args=(reply, start_time))
                           os.remove(thumbnail)
                        elif thumb == "no" and raw_text7 == "no":
                        
                             copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1, progress=progress_bar, progress_args=(reply, start_time))
                        elif raw_text7 == "yes" and thumb != "no":
                              subprocess.run(['wget', thumb2, '-O', 'thumb1.jpg'], check=True)  # Fixing this line
                              thumbnail = "thumb1.jpg"
                              copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1,thumb=thumbnail, progress=progress_bar, progress_args=(reply, start_time))
                        else:
                            subprocess.run(['wget', thumb2, '-O', 'thumb1.jpg'], check=True)  
                            thumbnail = "thumb1.jpg"
                            copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1, thumb=thumbnail, progress=progress_bar, progress_args=(reply, start_time))
                        await reply.delete (True)
                        os.remove(f'{name}.pdf')
                        count += 1
                        time.sleep(2)
                    except FloodWait as e:
                        #await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue

                else:
                    prog = await m.reply_text(f"📥 **Downloading **\n\n**➭ Count » {str(count).zfill(3)} **\n**➭ Video Name » ** `{name}`\n**➭ Quality** » `{raw_text2}`\n**➭ Video Url »** `{url}`\n**➭ Thumbnail »** `{input6.text}` \n\n✨ **Bot Made by Devansh**\n**━━━━━━━✦✗✦━━━━━━━**")
                    time.sleep(2)
                    res_file = await helper.drm_download_video(url,quality, name,key)
                    filename = res_file
                    await prog.delete(True)
                    time.sleep(1)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, thumb2)
                    count += 1
                    

            except Exception as e:
                await m.reply_text(f"**This #Failed File is not Counted**\n**Name** =>> `{name1}`\n**Link** =>> `{url}`\n\n ** Fail reason »** {e}")
                failed_links.append(f"{name1} : {url}")
                count += 1
                continue

    except Exception as e:
        await m.reply_text(e)
    time.sleep(2)


    if failed_links:
     error_file_send = await m.reply_text("**📤 Sending you Failed Downloads List **")
     with open("failed_downloads.txt", "w") as f:
        for link in failed_links:
            f.write(link + "\n")
    # After writing to the file, send it
     await m.reply_document(document="failed_downloads.txt", caption=fail_cap)
     await error_file_send.delete()
     failed_links.clear()
     os.remove(f'failed_downloads.txt')
    await m.reply_text("🔰Done🔰")
    await m.reply_text("**✨Thanks for Choosing**")
    processing_request = False  # Reset the processing flag  



    
  
processing_request = False  
bot.run()
