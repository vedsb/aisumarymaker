import os
import yt_dlp

def download_video(url, output_path="input.mp4"):
    try:
        ydl_opts = {
            'format': 'mp4[height<=360]',
            'outtmpl': output_path
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"✅ Video downloaded successfully as {output_path}")
    except Exception as e:
        print("❌ Error:", e)


if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=0FUFewGHLLg"
    download_video(url)
