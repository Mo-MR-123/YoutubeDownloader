import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": [],
    "includes": ['youtube_dl', 're', 'threading', 'os', 'sys'],
    "include_files": ['tcl86t.dll', 'tk86t.dll', 'ffmpeg.exe', 'ffprobe.exe', 'logo.ico']
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "YoutubeMp3Converter",
        version = "0.1",
        description = "YoutubeMp3Converter!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("YoutubeToMp3.py", icon="logo.ico", base=base)])