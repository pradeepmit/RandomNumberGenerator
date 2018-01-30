Write a custom random number generation algo which should be 73% biased to the higher number. Like if I want ‘a random number between 1 to 10’ 100 times then it should give ‘number more than 5’ 73 times and ‘less than 5’ 27 times. You’re not allowed to use any predefined random number generation function nor use of any kind of third party library to generate random number.

This Program fullfil the requirement mentioned in above description.
To run this file user need the Python3 installed on their system.

This algorithm generate the random numbers without using the random module.
This is based on time clock and struct.

To run the program type the following command on terminal:
python3 randomNumber.py 20 150

Here i passed two arguments 20 and 50. Actually it is the range. Random numbers will generate between 20 and 150 both included.
If no argument passed then number will be in range of 0:100.

Formula:
eg:
numberStart = 20
numberEnd = 150
HighLimit = int((numberEnd - numberStart)*73/100)
lowLimit = numberEnd-highLimit
midPoint = int(numberStart + numberEnd)/2

random_number >= midpoint will go in highlist
random_number < midpoint will go in lowlist.