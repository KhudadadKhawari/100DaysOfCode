import requests
from bs4 import BeautifulSoup
import spotipy


BILLBOARD_ENDPOINT = "https://www.billboard.com/charts/hot-100" # this code is scrapping this website for getting the top 100 songs list

# Copy These from Spotify, You will have to login as a developer and create a new app
CLIENT_ID = "COPY IT FROM YOUR SPOTIFY ACC"
CLIENT_SECRET = "COPY FROM YOUR SPOTIFY ACC"
REDIRECT_URI = "http://example.com"

scope = "playlist-modify-public"  # if you change the scope then it will ask again for the redirected url which u will have to copy and paste form your browser
# Authentication
authentication = spotipy.oauth2.SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=scope)
sp = spotipy.Spotify(auth_manager=authentication)

# Getting the USER ID
current_user = sp.current_user()
user_id = current_user["id"]

# Get the YYYY-MM-DD from user
date = input("Enter a Date with this format(YYYY-MM-DD) Ex. (2021-09-03): ")
# date = "2021-09-03"

url = f"{BILLBOARD_ENDPOINT}/{date}"
html_doc = requests.get(url=url).text
soup = BeautifulSoup(html_doc, "html.parser")
raw_songs_list = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

# Getting the songs name from the raw data scrapped form billboard
songs_names = []
for raw_song in raw_songs_list:
    songs_names.append(raw_song.get_text())

# Searching and getting Songs uris from Spotify
year = date.split('-')[0]
songs_uris = []
for song in songs_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")

# Creating a new PLay list
new_playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100")
playlist_id = new_playlist["id"]
# Adding songs to the playlist
sp.playlist_add_items(playlist_id=playlist_id, items=songs_uris)

