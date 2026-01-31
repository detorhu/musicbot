import base64, requests
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

def spotify_track(query):
    token = base64.b64encode(
        f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}".encode()
    ).decode()

    r = requests.post(
        "https://accounts.spotify.com/api/token",
        headers={"Authorization": f"Basic {token}"},
        data={"grant_type": "client_credentials"}
    )

    access = r.json()["access_token"]

    res = requests.get(
        "https://api.spotify.com/v1/search",
        headers={"Authorization": f"Bearer {access}"},
        params={"q": query, "type": "track", "limit": 1}
    )

    track = res.json()["tracks"]["items"][0]
    return f"{track['name']} {track['artists'][0]['name']}"
