import time
import subprocess
import gc
import pathlib

# Import logging
import logging

try:
    thread = 1
    file = pathlib.Path("run_file.py")
    while True:
        if file.exists():
            gc.get_count()
            gc.collect()
            print("Thread:", thread)
            subprocess.call("run_file.py", shell=True)
            thread = thread + 1
            time.sleep(60)
        else:
            logging.error("run_file.py does not exist in the directory")
except SyntaxError:
    logging.exception("A syntax error is found")
except ModuleNotFoundError:
    logging.exception("Module not installed or missing")
