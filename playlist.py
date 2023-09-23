from pytube import YouTube , Playlist

def Download(link):
    playlist = Playlist(link)
    for url in playlist:
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download(output_path='playlist')
   


link = input("Enter the YouTube video URL: ")
Download(link)