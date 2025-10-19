import os
from pathlib import Path
import shutil
import subprocess
import mpy_cross

# receiver or sender
type_response = input("sender or receiver? (s/r) ")
type_dir = "sender" if type_response == "s" else "receiver"

# Cleanup
if "out" in os.listdir():
    shutil.rmtree("out")
os.makedirs("out", exist_ok=True)

# Copy py files from sender/receiver dir
[shutil.copy(file, "out/" + file.name) for file in Path(type_dir).glob("*.py")]

# Compile and clean process
compile_response = input("Compile files? (y/n) ")
if compile_response == "y":
    # Compile only py files in dirs
    for py in Path("out").rglob("*.py"):
        mpy_cross.run(py.resolve())

    # Delete py files
    while True:
        mpy = [f for f in Path("out").rglob("*.mpy")]
        py = [f for f in Path("out").rglob("*.py")]
        if len(mpy) == len(py):
            [Path.unlink(f) for f in py]
            break


# Upload files
upload_response = input("Upload files? (y/n) ")
if upload_response == "y":
    commands = ["mpremote", "fs", "cp"]

    py_files = [f"{file.name}" for file in Path("out").glob("*.py")]
    if py_files:
        subprocess.call(commands + py_files + [":"])
