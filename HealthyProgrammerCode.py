# Healthy Programmer
"""
9am to 5pm
water - 3.5l - Drank
eyes  - every 30 min - eyesDone
excercise - every 45 min - exDone
"""
import time
from pygame import mixer


def getdateTime():
    import datetime
    return datetime.datetime.now()

def water_timeCal(water_time, eyes_time, exercise_time):
    """

    :param water_time:  water time
    :param eyes_time:   eyes practice time
    :param exercise_time: exercise time
    It will alert the programmer that it is water time.
    """
    print("--------- ITS WATER TIME ---------")
    print("For water we are playing \"BHAR DO JHOLI\"")
    mixer.init()
    mixer.music.load("bhar do jholi.mp3")
    mixer.music.play()
    print("Enter \'1\' to stop this music.")
    to_stop = int(input("Enter here to stop the music : "))
    water_time = 0
    eyes_time = eyes_time + 1
    exercise_time = exercise_time + 1
    if (to_stop == 1):
        mixer.music.stop()
        with open("water.txt", "a") as f:
            f.write("[" + str(getdateTime()) + "]" + "Drank\n")



def eyesPrac_time_cal(water_time, eyes_time, exercise_time):
    """

       :param water_time:  water time
       :param eyes_time:   eyes practice time
       :param exercise_time: exercise time
       It will alert the programmer that it is eyes practice time.
       """
    print("--------- ITS EYES PRACTICE TIME ---------")
    print("For Eyes Exercise we are playing \"LAAKHON SALAAM\"")
    mixer.init()
    mixer.music.load("laakhon salaam.mp3")
    mixer.music.play()
    print("Enter \'1\' to stop this music.")
    to_stop = int(input("Enter here to stop the music : "))
    water_time = water_time + 1
    eyes_time = 0
    exercise_time = exercise_time + 1
    if (to_stop == 1):
        mixer.music.stop()
        with open("eyePractice.txt", "a") as f:
            f.write("[" + str(getdateTime()) + "]" + "Eyes Practice done\n")



def physical_time_cal(water_time, eyes_time, exercise_time):
    """

       :param water_time:  water time
       :param eyes_time:   eyes practice time
       :param exercise_time: exercise time
       It will alert the programmer that it is exercise time.
       """
    print("--------- ITS PHYSICAL PRACTICE TIME ---------")
    print("For Physical Training we are playing \"QASIDA BURDA\"")
    mixer.init()
    mixer.music.load("Qasida Burda.mp3")
    mixer.music.play()
    print("Enter \'1\' to stop this music.")
    to_stop = int(input("Enter here to stop the music : "))
    water_time = water_time + 1
    eyes_time = eyes_time + 1
    exercise_time = 0
    if (to_stop == 1):
        mixer.music.stop()
        with open("PhysicalExercise.txt", "a") as f:
            f.write("[" + str(getdateTime()) + "]" + "Physical Exercise done\n")


total_mins = 8 * 60 * 60
total_water_glass = 3.5 * 4
total_time_reqfor_water = total_mins / total_water_glass
water_time = 0
eyes_time = 0
exercise_time = 0

for i in range(total_mins):
    time.sleep(1)

    if eyes_time > 0 and eyes_time % 30 == 0:
       eyesPrac_time_cal(water_time, eyes_time, exercise_time)
    elif water_time > 0 and water_time % 40  == 0:
        water_timeCal(water_time, eyes_time, exercise_time)
    elif exercise_time > 0 and exercise_time % 45 == 0:
        physical_time_cal(water_time, eyes_time, exercise_time)
    water_time = water_time + 1
    eyes_time = eyes_time + 1
    exercise_time = exercise_time + 1
