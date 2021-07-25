import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests


'''
MUST USE OWN SPOTIFY ACCOUNT.
-FIRST GO TO THE DEVELOPER DASHBOARD AND CREATE A NEW SPOTIFY APP.
-AFTER CREATING A SPOTIFY APP, COPY THE CLIENT ID AND CLIENT SECRET.
'''
CLIENT_ID = "ENTER CLIENT ID"
CLIENT_SECRET = "ENTER CLIENT SECRET"
SPOTIPY_REDIRECT_URI= "http://example.com"
SPOTIFY_URI = []

'''
ASK USER FOR THEIR DATE PREFERENCE AND RETURN THE TOP 100 BILLBOARD SONGS ON THAT SPECIFIC DATE 
THE USER CHOSE USING BEAUTFULSOUP
'''
user_input = input("Which year do you want to travel to? Please enter the date in this format YYYY-MM-DD:\n")
URL = f"https://www.billboard.com/charts/hot-100/{user_input}"
response = requests.get(URL)
response.raise_for_status()
webpage = response.text

'''
MUST USE SPOTIPY IN ORDER TO ACCESS OWN'S SPOTIFY ACCOUNT.
-MUST PASS "playlist-modify-private" IN ORDER TO CREATE A PRIVATE PLAYLIST.
-AFTER USING SPOTIPY AUTHENTICATION, IT WILL LEAD YOU TO THE SPOTIPY_REDIRECT_URI, AND MUST COPY THE ENTIRE URL INTO THE
THE PYCHARM PROMPT.
-AFTER ENTERING THE URL TO THE PYCHARM PROMPT, RESTART PYCHARM AND A FILE CALLED 'token.txt' WILL BE AUTOMATICALLY GENERATED.
'''
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,scope="playlist-modify-private",
                                                show_dialog=True,cache_path="token.txt"))

'''
BY USING BEAUTIFULSOUP AND THE USER INPUT (DATE INPUT), MUST SCRAPE THE BILLBOARD TOP 100 WEBSITE.
'''
soup = BeautifulSoup(webpage, "html.parser")
songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
artists = soup.find_all(name="span", class_="chart-element__information__artist text--truncate color--secondary")

