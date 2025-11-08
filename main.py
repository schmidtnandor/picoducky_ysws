import time
import keyboard
import mouse


# previous attempts at something better(powershell command made by ai)
# def taskkill(window_titles: list[str]):
#     for window_title in window_titles:
#         command = (
#             "powershell -NoProfile -ExecutionPolicy Bypass -Command "
#             "\"$stringToMatch = '{0}'; "
#             "$processes = Get-Process | Where-Object {{ $_.MainWindowTitle -like '*{0}*' }}; "
#             "foreach ($process in $processes) {{ Taskkill /PID $process.Id /F }}"
#         ).format(window_title)
#         keyboard.write(command)
#         keyboard.press_and_release("enter")
# def taskkill(window_titles: list[str]):
#     for window_title in window_titles:

#         command = (
#             "powershell -NoProfile -ExecutionPolicy Bypass -Command "
#             "\"$stringToMatch = '{0}'; "
#             "$processes = Get-Process | Where-Object {{ $_.MainWindowTitle -like '*{0}*' }}; "
#             'foreach ($process in $processes) {{ Taskkill /PID $process.Id /F }}; pause"'
#         ).format(window_title)
#         keyboard.write(command)

#         keyboard.press_and_release("enter")
#         time.sleep(3)


def type_slowly(string: str):
    for character in string:
        keyboard.write(character)
        time.sleep(0.1)


def taskkill(distraction_processes: list[str]):
    keyboard.press_and_release("win+r")
    time.sleep(0.3)
    keyboard.write("cmd.exe", time.sleep(0.1))
    keyboard.press_and_release("enter")
    for process in distraction_processes:
        time.sleep(0.3)
        keyboard.write(f"taskkill /f /im {process}", time.sleep(0.3))
        time.sleep(0.3)
        keyboard.press_and_release("enter")

    keyboard.write("exit")
    keyboard.press_and_release("enter")


def enter_and_sleep():
    keyboard.press_and_release("enter")
    time.sleep(0.3)


def yt_fullscreen():
    mouse.move(1956, 1184, True)
    time.sleep(0.5)
    mouse.click("left")


def open_vid():
    keyboard.press_and_release("win+r")
    keyboard.write("https://www.youtube.com/watch?v=OO14VSx74MU", time.sleep(0.1))
    keyboard.press_and_release("enter")


keyboard.press_and_release("win+r")
keyboard.write("cmd.exe")
keyboard.write("notepad.exe", time.sleep(0.5))
keyboard.press_and_release("enter")
time.sleep(0.5)
type_slowly("You’ve been staring at your screen mindlessly, am I correct?")
enter_and_sleep()
type_slowly(
    "If procrastination were an Olympic sport, you’d already have a trophy cabinet full of gold medals by now..."
)
enter_and_sleep()
type_slowly(
    "You thought you could get away, don't you? I will watch you from now on... You better do your work now!"
)

# enter the processes that should be closed here
processes = []
if len(processes) > 0:
    taskkill(processes)
    time.sleep(len(processes))
else:
    time.sleep(3)
open_vid()
time.sleep(3)
mouse.move(1956, 1184, True)
time.sleep(0.5)
mouse.click("left")
# of course there are a million other ways to bypass, this is just for fun
keyboard.add_hotkey("f11", yt_fullscreen)
bypass_attempt_count = 0

while True:
    if keyboard.is_pressed("f11"):
        bypass_attempt_count += 1
        yt_fullscreen()
    if keyboard.is_pressed("alt + f4"):
        bypass_attempt_count += 1
        time.sleep(10)
        open_vid()
    # trying to exit out of the video shuts down the pc eventually lol
    if bypass_attempt_count == 10:
        while True:
            keyboard.press_and_release("alt+f4")
            keyboard.press_and_release("enter")
    time.sleep(10)
    if len(processes) > 0:
        taskkill(processes)
