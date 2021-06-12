#!/usr/bin/python3
import subprocess
import time


def speak(text_to_speech, block=True):
	print(text_to_speech)
	process = subprocess.Popen(["espeak", text_to_speech], stdout=subprocess.PIPE)
	if block:
		output, error = process.communicate()

def beep():
	print('\a')



def count_down(duration):
	speak_interval=10
	start_count_down=3
	while duration > 0:
		sduration=str(duration)
		if duration % speak_interval == 0:
			speak(sduration, block=False)
		elif duration <= start_count_down:
			speak(sduration, block=False)
		else:
			print(sduration)
		duration=duration-1
		time.sleep(1)




def individual_finger(finger, rest_interval, active_interval):
	speak(finger + " finger")
	count_down(rest_interval)

	speak("Start", block=False)
	beep()
	count_down(active_interval)

	speak("Rest")



def exercise_fingers(fingers, active_interval,rest_interval):
	for finger in fingers:
		individual_finger(finger,active_interval,rest_interval)

def finger_workout():
	sets=2
	set_rest=60
	active_interval=5
	rest_interval=5
	fingers = ["pointer", "middle", "ring", "pinkey"]

	preamble=True


	if preamble:
		speak("Preparing finger work out")
		speak("Hang individual fingers on command")
		speak("Hang interval for each finger " + str(active_interval) + " seconds")
		speak("Rest interval " + str(rest_interval) + " seconds")
		speak("Rest between sets " + str(set_rest) + " seconds")

		active_set_time = ((active_interval+rest_interval) * len(fingers))
		print(active_set_time)
		workout_time = (active_set_time * sets) + (set_rest * (sets-1))
		workout_mins = int((workout_time / 60))
		speak("Estemated workout time " + str(workout_mins) + " minutes")

		speak("Start on beep sound ")
		speak("example start beep")
		time.sleep(0.5)
		beep()
		time.sleep(1)
		speak("Beginning workout")


	
	for i in range(sets):
		speak("Set Number "+ str(i) +" Prepare for set")
		exercise_fingers(fingers, active_interval, rest_interval)

		if i < sets-1:
			speak("Set " + str(i) + " out of " + str(sets) +" complete. Rest between sets " + str(set_rest) + "seconds")
			count_down(set_rest)
	
	time.sleep(1)
	speak("Finger board exercise complete")
	speak("Good Job Stew")



finger_workout()