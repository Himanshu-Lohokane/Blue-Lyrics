import os
import PyInstaller.__main__

# Define the path to your main script
script_path = "lyrics.py"

# Define the name of the output executable
output_name = "Will_you"

# Run PyInstaller to create the executable
PyInstaller.__main__.run([
    script_path,
    '--onefile',  # Create a single executable file
    '--name', output_name,  # Name of the output executable
    '--add-data', 'main.mp3;.',  # Include the main.mp3 file
    '--console',  # Open a console window to see output
])

print(f"Executable created: dist/{output_name}.exe")
