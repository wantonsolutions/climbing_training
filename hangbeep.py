#!/usr/bin/python3
import subprocess
import time


def speak(text_to_speech, block=True):
	print(text_to_speech)
	process = subprocess.Popen(["espeak", text_to_speech], stdout=subprocess.PIPE)
	if block:
		output, error = process.communicate()

def timed_speak(text_to_speech):
	start_talking = time.time()
	speak(text_to_speech, block=True)
	talking_duration = int(time.time() - start_talking)
	return talking_duration


def beep():
	print('\a')



def count_down(duration):
	#don't count right away
	hold_first_n=2
	full_duration=duration
	speak_interval=10
	start_count_down=3
	while duration > 0:
		sduration=str(duration)
		if full_duration-duration < hold_first_n and duration > start_count_down:
			print(sduration)
		elif duration % speak_interval == 0:
			speak(sduration, block=False)
		elif duration <= start_count_down:
			speak(sduration, block=False)
		else:
			print(sduration)
		duration=duration-1
		time.sleep(1)




def individual_finger(finger, active_interval, rest_interval,):
	duration = timed_speak(finger)
	duration += timed_speak("Hold for " + str(active_interval) + "seconds")
	count_down(rest_interval - duration)

	speak("Start", block=False)
	beep()
	count_down(active_interval)

	speak("Rest")

def start_example():
	speak("Start on beep sound ")
	speak("example start beep")
	time.sleep(0.5)
	beep()
	time.sleep(1)

def describe_workout(workout_name, fingers, sets, set_rest, active_interval, rest_interval):
	speak("Running finger workout protocol "+ workout_name)
	speak("Active interval for each exercise " + str(active_interval) + " seconds")
	speak("Rest interval " + str(rest_interval) + " seconds")
	speak("Rest between sets " + str(set_rest) + " seconds")

	active_set_time = ((active_interval+rest_interval) * len(fingers))
	workout_time = (active_set_time * sets) + (set_rest * (sets-1))
	workout_mins = int((workout_time / 60))
	speak("Estemated workout time " + str(workout_mins) + " minutes")



def exercise_fingers(fingers, active_interval,rest_interval):
	for finger in fingers:
		#this just prevents a rest from running on the first iteration
		rest=rest_interval
		if finger == fingers[0]:
			rest=5
		individual_finger(finger,active_interval,rest)


def workout(workout_name,fingers,sets, set_rest, active_interval, rest_interval, preamble=True):
	if preamble:
		describe_workout(workout_name,fingers,sets,set_rest, active_interval, rest_interval)
		start_example()
	
	
	speak("Beginning workout " + workout_name)
	
	for i in range(sets):
		speak("Set Number "+ str(i) +" Prepare for set")
		exercise_fingers(fingers, active_interval, rest_interval)

		if i < sets-1:
			duration = timed_speak("Set " + str(i) + " out of " + str(sets-1) +" complete. Rest between sets " + str(set_rest) + " seconds")
			count_down(set_rest - duration)

	time.sleep(1)
	speak("Finger board exercise complete")
	speak("Good Job Stew")


def warmup():
	sets=3
	set_rest=30
	active_interval=10
	rest_interval=10
	fingers=[ "All four fingers", "All four fingers", "First Two Fingers", "Last Two fingers"]
	workout_name="warm up"
	preamble=False
	workout(workout_name,fingers,sets,set_rest,active_interval,rest_interval,preamble)


def mono_training():
	sets=5
	set_rest=60
	active_interval=5
	rest_interval=5
	fingers = ["pointer finger", "middle finger", "ring finger", "pinkey finger"]
	workout_name="mono training"
	workout(workout_name, fingers,sets,set_rest,active_interval,rest_interval)


warmup()
mono_training()