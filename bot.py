import random

hellow = ["hi", "hello", "good day","hello there"]
bye = [ "see you later","bye" ,"goodbye", "i am Leaving", "have a Good day"]
howare = ["how are you","whats up","how you doing"]
name = ["whats your name","what is your name","do you have any name","what should i call you","name"]
q1 = ["what is the color of sky","what is the color of sky?"]
q2 = ["Who was the first President of India?","Who was the first President of India"]
q3 = ["Brain of computer","Brain of computer is?"]
q4 = ["National animal of India","National animal of India?"]
q5 = ["Gateway of India","Gateway of India is located at?"]



print("*******************\n")

while True:
	a = input('YOU -')

	if a in hellow:
		botans = ["Hello !","hi","hi there","welcome"]
		print('Bot  - '+random.choice(botans)+'\n')

	elif a in bye:
		botans = ["sad to see you go :(","bye","miss you"]
		print('Bot  - '+random.choice(botans)+'\n')

	elif a in howare:
		botans = ["I am fine ,thanks ","Happy","I am good"]
		print('Bot  -'+ random.choice(botans)+'\n')

	elif a in name:
		botans = ["My name is GK bot","You can call me GK bot","GK Bot in your service","My friends call me GK Bot"]
		print('Bot -'+ random.choice(botans)+'\n')

	elif a in bye:
		botans = ["Sad to see you go :(", "Talk to you later", "Goodbye!","Have a nice Day"]
		print('Bot  - '+random.choice(botans)+'\n')

# answer

	elif a in q1:
		botans = ["The color of sky is Blue"]
		print('Bot  - '+random.choice(botans)+'\n')
	elif a in q2:
		botans = ["Dr. Rajendra Prasad , (born December 3, 1884, Zeradei, India—died February 28, 1963, Patna), Indian politician, lawyer, and journalist who was the first president of the Republic of India (1950–62)."]
		print('Bot  - '+random.choice(botans)+'\n')
	elif a in q3:
		botans = ["CPU,The Central Processing Unit (CPU) is the primary component of a computer that acts as its “control center.” The CPU, also referred to as the “central” or “main” processor, is a complex set of electronic circuitry that runs the machine's operating system and apps."]
		print('Bot  - '+random.choice(botans)+'\n')
	elif a in q4:
		botans = ["TIGER,As the largest member of the cat family, Tigers are strong, powerful and one of nature's most feared predators. Their beautiful orange and black striped coats provide camouflage when hunting prey at night, when they can reach speeds of 65 km/hr (~40 mph)."]
		print('Bot  - '+random.choice(botans)+'\n')
	elif a in q5:
		botans = ["Mumbai"]
		print('Bot  - '+random.choice(botans)+'\n')

	else:
		print('Bot  - Sorry What ?''\n')