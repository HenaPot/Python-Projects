from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import os



# spotify authorization
CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
SPOTIPY_REDIRECT_URI = os.environ["SPOTIPY_REDIRECT_URI"]
# USERNAME = os.environ["USERNAME"]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path=".cache"
    )
)
user_id = sp.current_user()["id"]

# the day Breanna and I met :D
date = "2022-04-12"
url = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url)
billboard_html = response.text
soup = BeautifulSoup(billboard_html, "html.parser")
jumbled_list = soup.find_all(name= "h3", id="title-of-a-story", class_="c-title")
mixed_list = [item.get_text().strip() for item in jumbled_list]

get_item_before = "Songwriter(s):"
top_100_songs = []

# indices start from 1 because the 1st itemin the mixed list is a get_item_before (NOT A SONG NAME)
for i in range(1, len(mixed_list)):
    if mixed_list[i] == get_item_before:
        top_100_songs.append(mixed_list[i-1])

# print(len(top_100_songs))
# print(top_100_songs)

song_uris = []
year = date.split("-")[0]
for song in top_100_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(
            user= user_id,
            name=f"{date} Top 100 ",
            public=False,
            description="Trending songs on the day we met <3"
        )

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
