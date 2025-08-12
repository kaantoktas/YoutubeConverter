import yt_dlp


video_url = input("İndirmek istediğiniz YouTube videosunun URL'sini girin: ")


ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': '%(title)s.%(ext)s',
    'verbose': True, 
}


try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        video_title = info_dict.get('title', None)
        print(f"\n'{video_title}' adlı video indiriliyor...")
        ydl.download([video_url])

    print("Video başarıyla indirildi!")

except Exception as e:
    print(f"Bir hata oluştu: {e}")