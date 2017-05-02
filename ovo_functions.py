from pydub import AudioSegment


#/// FUNCTIONS ///

# Prompts user to drag and drop audio file into terminal, then sets audio file as global variable input_sample.
def input_audio():
	input_file_path = raw_input("Drag and drop sample into terminal window.")[:-1]
	global input_sample
	input_sample = AudioSegment.from_file(input_file_path, format="wav")

# Reverses sample and exports .wav file
def reverse_sample():
	input_audio()
	reversed_sample = input_sample.reverse()
	reversed_sample.export("reversed-sample.wav", format = "wav")
	print "Code has run!"

# Degrades sample rate and exports .wav file
def underwater_effect():
	input_audio()
	frame_rate = 4000
	underwater_sample = input_sample.set_frame_rate(frame_rate)
	underwater_sample.export("underwater-sample.wav", format = "wav")
	print "Code has run!"