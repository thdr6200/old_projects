import ast
import sys
import os
import random
import threading
import time
import subprocess

class Processes:
    def start(self):
        hunger = threading.Thread(target=self.feed_thread)
        thirst = threading.Thread(target=self.thirst_thread)
        happiness = threading.Thread(target=self.happiness_thread)
        age = threading.Thread(target=self.age_thread)
        hunger.start()
        thirst.start()
        happiness.start()
        age.start()
    def feed_thread(self):
        while hamtaro.max_stats['hunger'] > 0:
            hamtaro.max_stats['hunger'] -= 1
            hamtaro.write_or_read("w")
            time.sleep(7200)
        hamtaro.max_stats['death'] = "Hamtaro died from hunger."
    def thirst_thread(self):
        while hamtaro.max_stats['thirst'] > 0:
            hamtaro.max_stats['thirst'] -= 1
            hamtaro.write_or_read("w")
            time.sleep(60)
        hamtaro.max_stats['death'] = "Hamtaro died from thirst."
    def happiness_thread(self):
        while hamtaro.max_stats['happiness'] > 0:
            hamtaro.max_stats['happiness'] -= random.randint(15, 20)
            hamtaro.write_or_read("w")
            time.sleep(7200)
        hamtaro.max_stats['death'] = "Hamtaro died from sadness."
    def age_thread(self):
        while self.max_stats['death'] == "":
            if hamtaro.max_stats["heures"] == 24:
                hamtaro.max_stats['jours'] += 1
                hamtaro.max_stats["heures"] = 0
            time.sleep(3600)

class Hamtaro(Processes):
    def first_run(self):
        self.max_stats = {"hunger": 100, "thirst": 100, "happiness": 100, "heures": 0, "jours": 0, "death": ""}
        self.write_or_read("w")
    def reset(self, stat):
        self.max_stats[stat] = 100
    def write_or_read(self, option):
        if option == "w":
            with open(os.environ["APPDATA"] + r"\Hamtaro_Stats.txt", option) as f:
                f.write(str(self.max_stats))
                f.close()
        elif option == "r":
            with open(os.environ["APPDATA"] + r"\Hamtaro_Stats.txt", option) as f:
                result = ast.literal_eval(f.read())
                print(f"Hunger: {result['hunger']}\nThirst: {result['thirst']}\nHappiness: {result['happiness']}\nJours: {result['jours']}\nHeures: {result['heures']}")
                f.close()
        else:
            sys.exit()


COMMANDS = ["init", "check", "feed", "drink", "play"]
HELP = r'''
You can use the script like this:

python hamtaro.py command

Commands:

> init
Start a new game with your little Hamtaro.
> check
Check Hamtaro's stats or Hamtaro death cause.
> feed
You can feed Hamtaro.
> drink
You can let Hamtaro drink.
> play
You can play with Hamtaro.

Rules:

Don't let one of Hamtaro stats decrease. If one of his stats reaches 0%, then he dies.
Also, here's some tips:

- Feed bar loses 1% each two hours.
- Drink bar loses 1% each minute.
- Happiness bar loses between 15%-20% each two hours.

Have fun !
'''

hamtaro = Hamtaro()

if len(sys.argv) == 2:
    if sys.argv[1] == COMMANDS[0]:
        hamtaro.first_run()
        hamtaro.start()
    elif sys.argv[1] == COMMANDS[1]:
        hamtaro.write_or_read("r")
    elif sys.argv[1] == COMMANDS[2]:
        hamtaro.reset("hunger")
    elif sys.argv[1] == COMMANDS[3]:
        hamtaro.reset("thirst")
    elif sys.argv[1] == COMMANDS[4]:
        hamtaro.reset("happiness")
    else:
        print("Argument doesn't exist !")
elif len(sys.argv) == 1:
    print(HELP)
elif len(sys.argv) > 2:
    print("Enter only one argument each time !")
