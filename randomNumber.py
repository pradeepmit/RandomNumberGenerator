import struct,time,sys

def lastbit(f):
    return struct.pack('!f', f)[-1] & 1

def getrandbits(k):
    "Return k random bits using a relative drift of two clocks."
    # assume time.sleep() and time.clock() use different clocks
    # though it might work even if they use the same clock
    #XXX it does not produce "good" random bits, see below for details
    result = 0
    for _ in range(k):
        time.sleep(0.000000001) #by tweeking value of sleep argument one can increse or decrese the difference etween random numbers.
        result <<= 1
        result |= lastbit(time.clock())
    return result
def randint(a, b):
    "Return random integer in range [a, b], including both end points."
    return a + randbelow(b - a + 1)

def randbelow(n):
    "Return a random int in the range [0,n).  Raises ValueError if n<=0."
    # from Lib/random.py
    if n <= 0:
       raise ValueError
    k = n.bit_length()  # don't use (n-1) here because n can be 1
    r = getrandbits(k)          # 0 <= r < 2**k
    while r >= n: # avoid skew
        r = getrandbits(k)
    return r
if __name__ == "__main__":
	"This will generate the random numbers which are 73% biased to the higher number."
	iteration = True
	lowList = []
	highList = []
	numberStart = 0
	numberEnd = 100
	try:
		numberStart = int(sys.argv[1])
		numberEnd = int(sys.argv[2])
	except:
		print("Range of random Numbers not passed so the random numbers will lies between %s:%s"%(numberStart,numberEnd))

	highLimit = int((numberEnd - numberStart)*73/100)
	lowLimit = numberEnd-highLimit
	midPoint = int(numberStart + numberEnd)/2

	# print(highLimit,lowLimit, midPoint)
	while iteration:
		if(len(lowList) == lowLimit and len(highList) == highLimit):
			iteration = False
		number = randint(numberStart, numberEnd)
		if(number < midPoint):
			if(len(lowList) < lowLimit):
				lowList.append(number)
		if(number >= midPoint):
			if(len(highList) < highLimit):
				highList.append(number)
	print(len(lowList), len(highList))
	print('Numbers < midPoint',lowList)
	print('Numbers >= midPoint',highList)

