from playwright.sync_api import sync_playwright
import time
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            record_video_dir="/Users/ikhaisoshuare/Cascade",
            record_video_size={"width": 1920, "height": 1080}
        )
        page = context.new_page()
        
        print("Loading presentation...")
        page.goto('file:///Users/ikhaisoshuare/Cascade/Sylon_Pitch_Deck.html')
        
        # Allow the first slide to animate
        time.sleep(3)
        
        print("Recording slides...")
        for i in range(5): # 5 transitions to reach slide 6
            page.keyboard.press('ArrowRight')
            time.sleep(3) # Wait for animation to finish before next slide
            
        print("Finalizing video...")
        time.sleep(4) # Let final slide sit
        
        page.close()
        context.close()
        browser.close()
        
        print("Video successfully recorded!")

if __name__ == '__main__':
    run()
