from telethon import TelegramClient
from telethon.tl import types as TelegramTypes
import sys
# Use your own values from my.telegram.org
api_id   = <API ID>
api_hash = <API HASH>
client   = TelegramClient('mySession', api_id, api_hash)

channel = None

# Printing download progress
def progressCallback(current, total):
    sys.stdout.write(f'Download {current} out of {total} bytes: {current/total:.2%}\r')

async def listMedia():
    global channel
    async for message in client.iter_messages(channel,reverse=True):
        if message.media is not None: # target media
            print(f"Media: {message.id}:{message.text}")

async def downloadMediaFrom(download_path,message_ids):
    global channel
    async for message in client.iter_messages(channel,ids=message_ids):
        if message.media is not None: # target media
            print(f"Downloading Media: {message.id}:{message.text}")
            await client.download_media(message.media, progress_callback=progressCallback)
            print(f"Downloaded Media: {message.id}:{message.text}")

async def list_channel():
    global channel
    async for dialog in client.iter_dialogs():
        if type(dialog.entity) is TelegramTypes.Channel:
            print(f"{dialog.entity.id}: {dialog.entity.title}")
    channel = int(input("channel name/id : "))


# The first parameter is the .session file name (absolute paths allowed)
def main():

    global channel

    if channel is not None :
        print(f"Channel Name: {channel}")

    while True:
        print("1. List Channel")
        print("2. List Media")
        print("3. Download Media")
        print("0. Quit")
        choice = int(input("Enter Choice: "))
        if choice is 1:
            print("choice 1 is selected")
            with client:
                client.loop.run_until_complete(list_channel())
        if choice is 2:
            with client:
                client.loop.run_until_complete(listMedia())
        elif choice is 3:
            ids_input = input("Enter id's(comma seperated): ")
            ids_split = ids_input.split(",")
            ids = [int(i) for i in ids_split]
            with client:
                client.loop.run_until_complete(downloadMediaFrom(None,ids))
        elif choice is 0:
            exit()
        else:
            continue

if __name__ == "__main__":
    main()
