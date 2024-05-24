from packages import *

client_id= 'your-client-id'
client_secret= 'your-client-secret'
redirect_uri = 'your-redirect-uri'

sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=['user-read-playback-state', 'user-modify-playback-state', 'streaming','user-library-read'])
sp=spotipy.Spotify(auth_manager=sp_oauth)

def connect():
    devices = sp.devices()
    for device in devices['devices']:
        print('{}'.format(device['name']))
    choice=int(input("Enter which device: \n"))
    device_id = devices['devices'][choice-1]['id']
    print("Connecting to your device....\n")
    sp.transfer_playback(device_id=device_id)
    playback = sp.current_playback()
    if playback is not None:
        device_id1 = playback['device']['id']
        if device_id1 == device_id:
            print('Spotipy is connected to the selected device.')
    else:
        print('No active device found')
    current_song = sp.current_playback()
    if current_song is not None:
        print("Currently playing:")
        print("Song:", current_song["item"]["name"])
        print("Artist:", current_song["item"]["artists"][0]["name"])
        duration=current_song["progress_ms"]
        minutes = (duration/1000)/60
        seconds = (duration/1000)%60
        print("Current position:", minutes, "minutes" , seconds , "seconds")
    else:
        print("No song is currently playing.")
    time.sleep(3)
        
def search_play():
    song_name = input('Enter the name of the song you want to search for:\n ')
    results = sp.search(q=song_name, limit=10, type='track')
    for i, t in enumerate(results['tracks']['items']):
        print(f"{i+1}. {t['name']} - {t['artists'][0]['name']}")
    n=int(input("Enter which:"))
    if(0<n<=10):
        track_id = results['tracks']['items'][n-1]['id']
        print("Specific position or beginning?\n")
        print("Specific only for premium users")
        n=int(input("Press your choice\n"))
        if (n==1):
            start_time=int(input("Enter your time"))
            start_position_ms = start_time * 1000; 
            sp.start_playback(uris=[])
            print("Playing your song...")
            sp.start_playback(uris=['spotify:track:' + track_id], position_ms=start_position_ms)
        else:
            sp.start_playback(uris=[])
            print("Playing your song...")
            sp.start_playback(uris=['spotify:track:' + track_id])

        track = sp.track(track_id)
        name = track['name']
        artist = track['artists'][0]['name']
        print(f"Name: {name}\nSinger: {artist}")
        time.sleep(4)
    else:
        print("Try Again")
        time.sleep(2)
    
def pause():
    sp.pause_playback()
    print("Song paused...")
    time.sleep(4)
    
def resume():
    sp.start_playback()
    print("Song resumed...")
    print("Do you want to rewind?\n")
    print("Only for premium users")
    ans=input("Enter Y/N")
    if ans == 'Y':
        time_rewind=int(input("Enter your seconds\n"))
        rewind=time_rewind*1000;
        print("Rewinding.....")
        current_playback = sp.current_playback()
        if current_playback and current_playback['is_playing']:
            position_ms = max(current_playback['progress_ms'] - rewind, 0)
            sp.start_playback(uris=[current_playback['item']['uri']], position_ms=position_ms)
    else:
        print("Thanks")
    print("Do you want to go fast-forward?\n")
    print("Only for premium users")
    ans1=input("Enter Y/N")
    if ans1 == 'Y':
        time_rewind=int(input("Enter your seconds\n"))
        rewind=time_rewind*1000;
        print("Fast forwarding.....")
        current_playback = sp.current_playback()
        if current_playback and current_playback['is_playing']:
            position_ms = max(current_playback['progress_ms'] + rewind, 0)
            sp.start_playback(uris=[current_playback['item']['uri']], position_ms=position_ms)
    else:
        print("Thanks")

def adding_queue():
    print("Yes to queue your song and no to exit")
    while True:
        ans=input("Enter yes or no \n")
        if ans.lower()=='yes':
            song = input('Enter the name of the song you want to search for: ')
            results = sp.search(q=song, limit=10, type='track')
            for i, t in enumerate(results['tracks']['items']):
                print(f"{i+1}. {t['name']} - {t['artists'][0]['name']}")
            n=int(input("Enter which:"))
            if(n>0):
                track_id = results['tracks']['items'][n-1]['id']
            else:
                print("Try Again")
            print("Song adding....")
            time.sleep(1)
            sp.add_to_queue(uri=track_id)
            print("Added")
        else:
            print("Queue exiting.....")
            break
        time.sleep(1)

def playing_next():
    sp.next_track()
    print("Displaying song...")
    time.sleep(2)
    current_track = sp.current_playback()
    song_name = current_track['item']['name']
    artist_name = current_track['item']['artists'][0]['name']
    print(f"Currently playing: {song_name} by {artist_name}")
    time.sleep(4)
