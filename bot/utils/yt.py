import yt_dlp

YDL_OPTIONS = {
    "format": "bestaudio/best",
    "quiet": True,
    "noplaylist": True,
    "geo_bypass": True,
    "default_search": "ytsearch",
    "nocheckcertificate": True,
}

def get_audio(query: str):
    """
    Returns:
        stream_url (str): Direct audio stream URL
        title (str): Video title
        duration (int): Duration in seconds
    """
    with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(query, download=False)

        # If search result
        if "entries" in info:
            info = info["entries"][0]

        audio_url = info.get("url")
        title = info.get("title")
        duration = info.get("duration", 0)

        if not audio_url:
            raise Exception("Failed to fetch audio stream")

        return audio_url, title, duration
