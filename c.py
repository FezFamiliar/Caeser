import string

alpha = string.ascii_lowercase
freq_a = {}


def encrypt(msg,key):
	result = ""
	for x in range(0,len(msg)):
		for y in range(0,len(alpha)):
			if msg[x].lower() == alpha[y]:
				result += alpha[(y + (key + 1)) % len(alpha) - 1]

	return result.replace(" ","")


def decrypt(msg,key):
	result = ""
	for x in range(0,len(msg)):
		for y in range(0,len(alpha)):
			if msg[x].lower() == alpha[y]:
				result += alpha[y - (key) % len(alpha)]

	return result



def brute(msg):
	result = ""
	for t in range(1,len(alpha)):
		for x in range(0,len(msg)):
			for y in range(0,len(alpha)):
				if msg[x].lower() == alpha[y]:
					result += alpha[y - t % len(alpha)]

		print(result)
		result = ""

def freq(msg):
	global freq

	for i in range(0,len(alpha)):
		freq_a[alpha[i]] = 0

	for x in range(0,len(alpha)):
		for y in range(0,len(msg)):
			if msg[y].lower() == alpha[x]:
				freq_a[alpha[x]] = freq_a[alpha[x]] + 1




print(encrypt("nem voltam en, aron volt",7))
brute("ultcvsahtluhyvucvsa")

