#youtube playlist meta information downloader
#reference: https://stackoverflow.com/a/44185274

import youtube_dl

ydl_opts = {
    'ignoreerrors': True,
    'quiet': True
}

playlist = input("Playlist: ")

with youtube_dl.YoutubeDL(ydl_opts) as ydl:

    playlist_dict = ydl.extract_info(playlist, download=False)

    for video in playlist_dict['entries']:

        print()

        if not video:
            print('ERROR: Unable to get info. Continuing...')
            continue

        for property in ['thumbnail', 'id', 'title', 'description', 'duration']:
            if property == "duration":
                duration = int(video.get(property))
                print(property, '--', f'{int(duration/60)}:{duration%60}')
            else:
                print(property, '--', video.get(property))
