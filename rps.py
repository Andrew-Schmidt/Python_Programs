import random
cpu = ["r", "p", "s"]
computer=random.choice(cpu)
user = input("choose rock:r paper:p or scissors:s | ")
def main():
	compare(user)
	cont = input("do you want to continue?")
def choose():
	while cont != "no":
		user = input("choose rock:r paper:p or scissors:s | ")
		return user
		main()
def compare(choose):
	if user == computer:
		print("tie")
	if user == "r":
		if computer == "s":
			print("user wins")
		elif computer == "p":
			print("computer wins")
	if user == "s":
		if computer == "r":
			print("computer wins")
		elif computer == "p":
			print("user wins")
	if user == "p":
		if computer == "s":
			print("computer wins")
		elif computer == "r":
			print("user wins")
main()

