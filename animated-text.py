import time

animation = "-\\|/"

for i in range(25):
    time.sleep(0.1)
    print("\r" + animation[i % len(animation)], end='', flush=True)
