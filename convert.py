import imageio_ffmpeg
import subprocess

ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()
print(f"Using ffmpeg at: {ffmpeg_path}")

subprocess.run([
    ffmpeg_path, '-y', '-i', 'Sylon_Pitch_Deck.webm',
    '-c:v', 'libx264', '-crf', '23', '-preset', 'fast', 'Sylon_Pitch_Deck.mp4'
])
print("Conversion complete!")
