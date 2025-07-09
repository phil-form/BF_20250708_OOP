import os
import time

class Utils:
    @staticmethod
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def pause(sec: int):
        time.sleep(sec)


Utils.pause('asdf')
