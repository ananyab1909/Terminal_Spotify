from packages import *
import play as pl 

client_id= 'your-client-id'
client_secret= 'your-client-secret'
redirect_uri = 'your-redirect-uri'

sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=['user-read-playback-state', 'user-modify-playback-state', 'streaming','user-library-read'])
sp=spotipy.Spotify(auth_manager=sp_oauth)

def choice():
    print("Press 1 to choose your device")
    print("Press 2 to search and play your song")
    print("Press 3 to pause your song")
    print("Press 4 to resume your song")
    print("Press 5 to add queue")
    print("Press 6 to play the next song")
    print("Press 7 to exit")
os.system('cls' if os.name == 'nt' else 'clear')
choice()

while True:
    response=int(input("Enter your choice:"))
    if response>=7:
        break
    elif response==1:
        pl.connect()
        os.system('cls' if os.name == 'nt' else 'clear')
        choice()
    elif response==2:
        pl.search_play()
        os.system('cls' if os.name == 'nt' else 'clear')
        choice()
    elif response==3:
        pl.pause()
        os.system('cls' if os.name == 'nt' else 'clear')
        choice()
    elif response==4:
        pl.resume()
        os.system('cls' if os.name == 'nt' else 'clear')
        choice()
    elif response==5:
        pl.adding_queue()
        os.system('cls' if os.name == 'nt' else 'clear')
        choice()
    else:
        pl.playing_next()
        os.system('cls' if os.name == 'nt' else 'clear')
        choice()

