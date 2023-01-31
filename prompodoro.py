# Modules needed in this script.
import time

def read_file(path:str) -> list[str]:
    """Read File

    Args:
        path (str): File path

    Returns:
        list[str]: Text file by line.
    """
    try:
        with open(path, "r") as file:
            return file.read().split('\n')
    except IOError:
        print("File not accessible")

class Pomodoro:

    def __init__(self) -> None:
        pass

def pomodoro_timer(duration):
    for remaining in range(duration, 0, -1):
        minutes, seconds = divmod(remaining, 60)
        print(f"\r{minutes:02}:{seconds:02} remaining", end="", flush=True)
        time.sleep(1)
    print("\nTime's up! Take a break.")

if __name__ == '__main__':
    pomodoro_duration = 25 * 60  # 25 minutes in seconds
    print("🍅 Pomodoro timer started for 25 minutes.")
    pomodoro_timer(pomodoro_duration)