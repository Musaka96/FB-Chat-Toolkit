import fbchat

def login():

	try:	
	except:
		print("id or password is wrong")
		login()
	menu(client)

def menu(client):

	print("1.Messenger")
	print("2.Spammer")
	print("3.Log out")

	choice = input("> ")

	if choice == "1":
		messenger(client)
	if choice == "2":
		spammer()
	if choice == "3":
		login()

def messenger(client):

	who_we_need = input ("Who do we want to chat? --> ")
	friends = client.getUsers(who_we_need)  #gets us a list of names

	counter = 0

	for friend in friends:

		friend = str(friend)
		friend = friend[6:]
		string = ''

		for i in friend:      #all of this just print users nicely

			if i != "(":
				string += i
			else:
				break

		print(counter, ".",string)
		counter += 1

	who_s_it_gonna_be = input("So, who's it gonna be? > ")

	friend = friends[int(who_s_it_gonna_be)]

	try:
		while True:

			last_messages = client.getThreadInfo(friend.uid,0)
			last_messages.reverse()  # messages come in reversed order

			for message in last_messages:
				print(message.body)

			new_mssg = input("Poruka --> ")
			sent = client.send(friend.uid, new_mssg)
			if sent:
				print("Sent!")

	except KeyboardInterrupt:
		menu()
			
def spammer(client):

	who_we_need = input ("Who do we want to spamm? --> ")
	friends = client.getUsers(who_we_need)  #gets us a list of names

	counter = 0

	for friend in friends:

		friend = str(friend)
		friend = friend[6:]
		string = ''

		for i in friend:      #all of this just print users nicely

			if i != "(":
				string += i
			else:
				break

		print(counter, ".",string)
		counter += 1

	who_s_it_gonna_be = input("So, who's it gonna be? > ")

	friend = friends[int(who_s_it_gonna_be)]

	pain = input("How many times do we want to spamm him (enter a number, or 0 for infinity)")

	if pain == "0":

		message = input("Spamm message? > ")
		counter = 0

		try:
			while True:

				poruka = input("Poruka --> ")
				sent = client.send(friend.uid, poruka)

				if sent:

					counter += 1
					print("Sent " + counter + " times")

		except KeyboardInterrupt:
			menu()
	else:

		message = input("Spamm message? > ")
		counter = 0

		try:

			for i in range(int(pain)):

				poruka = input("Poruka --> ")
				sent = client.send(friend.uid, poruka)

				if sent:

					counter += 1
					print("Sent " + counter + " times")

			print("Done ^^")

		except KeyboardInterrupt:
			menu()




login()
