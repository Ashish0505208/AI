def vacuum_agent():
	actions = {"CLEAN": "SUCK!", "MOVE": {"A": "Move to Right", "B": "Move to Left"}}
	room = input("Enter starting room (A/B): ").upper()
	percept_table, i = {}, 0
	while True:
		status = input(f"Enter status of room {room} (CLEAN/DIRTY): ").upper()
		status = status if status in ["CLEAN", "DIRTY"] else "DIRTY"
		if status == "DIRTY":
			action = actions["CLEAN"]
			percept_table[f"Action {i+1}"] = {"Room": room, "Action": action}
			print(f"\nAction {i+1}: Room {room} | {action}")
			i += 1
		next_room = "B" if room == "A" else "A"
		action = actions["MOVE"][room]
		percept_table[f"Action {i+1}"] = {"Room": room, "Action": action}
		print(f"Action {i+1}: Room {room} | {action}\n")
		i += 1
		room = next_room
		if input("Continue? (yes/no): ").lower() == "no":
			break
	print("\nFinal Percept Table:")
	for action_num, details in percept_table.items():
		print(f"{action_num}: Room {details['Room']} | {details['Action']}")
	print(f"\nTotal Steps: {i} | Path Cost: {i}")
vacuum_agent()
