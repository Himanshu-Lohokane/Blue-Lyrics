import os

# Suppress the pygame welcome message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import time
import sys
from pathlib import Path

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def main():
    pygame.init()
    pygame.mixer.init()

    lyrics = [
        ("Your morning eyes, I could stare like watching stars", 0.5, 7.5),
        ("I could walk you by and I'll tell without a thought", 7.5, 14.5),
        ("You'd be mine, would you mind if I took your hand tonight", 14.5, 21.5),
        ("Know you're all that I want, this life", 21.5, 29.5),
        ("I'll imagine we fell in love", 29.5, 31.5),
        ("I'll nap under moonlight skies with you", 31.5, 36.5),
        ("I think I'll picture us, you with the waves", 36.5, 39.5),
        ("The ocean's colors on your face", 39.5, 43.5),
        ("I'll leave my heart with your air", 43.5, 47.5),
        ("So let me fly with you", 47.5, 50.5),
        ("Will you be forever with me...? ♥", 50.5, 56.5)
    ]

    try:
        # Load and play the music
        music_path = resource_path("main.mp3")
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play()
        start_time = time.time()
        
        for line, start_sec, end_sec in lyrics:
            current_time = time.time() - start_time
            wait_time = start_sec - current_time
            
            if wait_time > 0:
                time.sleep(wait_time)
            
            duration = end_sec - start_sec
            char_delay = duration / len(line)
            
            for char in line:
                print(char, end='', flush=True)
                time.sleep(char_delay)
            print()

        while pygame.mixer.music.get_busy():
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopped by user")
    except Exception as e:
        print(f"\nError: {e}")
    finally:
        pygame.mixer.quit()
        pygame.quit()

if __name__ == "__main__":
    main()