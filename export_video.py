import os
import subprocess
import time
from playwright.sync_api import sync_playwright
import imageio_ffmpeg

def main():
    # Paths
    html_path = "file:///Users/ikhaisoshuare/Cascade/presentation.html?autoplay=true"
    temp_dir = "/Users/ikhaisoshuare/Cascade/temp_video"
    output_mp4 = "/Users/ikhaisoshuare/Cascade/Morlen_Pitch_Deck_Final.mp4"
    
    # Ensure temp dir exists
    os.makedirs(temp_dir, exist_ok=True)
    
    print("Launching Playwright browser...")
    with sync_playwright() as p:
        # Launch headless browser
        browser = p.chromium.launch(headless=True)
        
        # Configure video recording
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=1,
            record_video_dir=temp_dir,
            record_video_size={"width": 1920, "height": 1080}
        )
        
        page = context.new_page()
        
        # Capture console and page errors
        page.on("console", lambda msg: print(f"Browser Console [{msg.type}]: {msg.text}"))
        page.on("pageerror", lambda err: print(f"Browser Page Error: {err}"))
        
        print("Navigating to presentation...")
        try:
            page.goto(html_path, wait_until="domcontentloaded", timeout=60000)
        except Exception as e:
            print(f"Navigation warning/error: {e}")
            
        print("Waiting for external CDNs (Tailwind & GSAP) to initialize...")
        # Custom wait for scripts to load
        page.wait_for_function("typeof gsap !== 'undefined' && typeof tailwind !== 'undefined'", timeout=30000)
        
        # Get the path where the video will be recorded
        video_path = page.video.path()
        print(f"Recording started. Output WebM path: {video_path}")
        
        # Wait for the presentation autoplay to finish
        # Total wait time of 85 seconds to ensure all scenes are captured completely
        duration_seconds = 85
        print(f"Recording for {duration_seconds} seconds...")
        
        for i in range(duration_seconds):
            time.sleep(1)
            if (i + 1) % 5 == 0:
                print(f"Recorded {i + 1}s / {duration_seconds}s...")
        
        # Close the page and browser to finalize the video file
        page.close()
        context.close()
        browser.close()
        
        print("Browser session closed. Finalizing WebM file...")
        
        # Wait a moment for file write completion
        time.sleep(2)
        
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Recorded WebM file not found at: {video_path}")
            
        print("Converting WebM to high-quality MP4 using bundled FFmpeg...")
        
        # Convert webm to mp4
        ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
        
        # FFmpeg command: High quality H.264, Slow preset, YUV420p for max player compatibility
        cmd = [
            ffmpeg_exe,
            "-y", # Overwrite if exists
            "-i", video_path,
            "-c:v", "libx264",
            "-crf", "18", # High quality (lower is better, 18 is visually lossless)
            "-preset", "slow",
            "-pix_fmt", "yuv420p",
            output_mp4
        ]
        
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode != 0:
            print("FFmpeg Conversion failed!")
            print("stderr:", result.stderr)
            raise subprocess.CalledProcessError(result.returncode, cmd, output=result.stdout, stderr=result.stderr)
            
        print(f"MP4 conversion successful! File saved to: {output_mp4}")
        
        # Clean up temporary WebM recording
        try:
            import shutil
            shutil.rmtree(temp_dir)
            print("Temporary WebM recordings cleaned up.")
        except Exception as e:
            print(f"Cleanup warning: {e}")

if __name__ == "__main__":
    main()
