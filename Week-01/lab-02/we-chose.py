import random , os
sites = ['https://google.com','https://github.com','https://gitlab.com']
cho = random.choice(sites)
print("Opening {} in chrome ".format(cho))
# windows only for now
os.system("start chrome {}".format(cho))
