from pygame import mixer
from datetime import datetime
from time import time


print("\n---Welcome to the Event Scheduler---@designed by the Abhishek Shukla.\n\n\n")


def exit_prgrame():
    user_input = input("Press 'q' to quit the programme and 'c' to Continue the Alarm and 'a' to check Acticity Log\n")
    if user_input == "q":
        print("Quiting the Reminder...\n Thank You for using the Reminder designed with python! Visit again!!!!")
        exit()
    elif user_input == "c":
        pass
    else:
        def check_log():
             with open("mylogs.txt", "r") as f:
                for item in f:
                    print(item)
                exit_prgrame()

        check_log()






def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f" {msg} {datetime.now()}\n")

if __name__ == '__main__':
    #musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 10
    exercisesecs = 20
    eyessecs = 30
    while True:
        if time() - init_water > watersecs:
            print("Water drinking time. Enter 'drank' to stop the alarm")
            musiconloop("water.mp3", 'drank')
            init_water = time()
            log_now("Drank Water at")
            # check_log()
            exit_prgrame()


        if time() - init_eyes > eyessecs:
            print("Eyes Exercise time. Enter 'doneey' to stop the alarm")
            musiconloop("eyes.mp3", 'doneey')
            init_eyes = time()
            log_now("Done Eyes Exercise at")
            exit_prgrame()
        if time() - init_exercise > exercisesecs:
            print("Physical Exercise time. Enter 'doneex' to stop the alarm")
            musiconloop("exercise.mp3", 'doneex')
            init_exercise = time()
            log_now("Done Physical Exercise at")
            exit_prgrame()


        # def check_log():
        #     inp = input("Press 'y' to check the acticity logs\n")
        #     if inp == "y":
        #         with open("mylogs.txt", "r") as f:
        #             for item in f:
        #                 print(item)
        #     else:
        #         pass
        #
        # check_log()






