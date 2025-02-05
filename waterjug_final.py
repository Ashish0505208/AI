def vacuum_agent():
    actions = {"CLEAN": "SUCK!", "MOVE": {"A": "Move to Right", "B": "Move to Left"}}
    room = input("Enter starting room (A/B): ").upper()
    percept_table, i = {}, 0
    while True:
        status = input(f"Enter status of room {room} (CLEAN/DIRTY): ").upper()
        status = status if status in ["CLEAN", "DIRTY"] else "DIRTY"
        if status == "DIRTY":
            action = actions["CLEAN"]
        else:
            action = actions["MOVE"][room]
            next_room = "B" if room == "A" else "A"
            percept_table[f"Action {i+1}"] = {"Room": room, "Action": action}
            print(f"\nAction {i+1} | Room: {room} | Action: {action}")
            room = next_room
            i += 1
            if status == "CLEAN" and input("Continue? (yes/no): ").lower() == "no":
                break
            continue
        percept_table[f"Action {i+1}"] = {"Room": room, "Action": action}
        print(f"\nAction {i+1} | Room: {room} | Action: {action}")
        if input("Continue? (yes/no): ").lower() == "no":
            break
        i += 1
    print("\nFinal Percept Table:")
    for action_num, details in percept_table.items():
        print(f"{action_num}: Room {details['Room']} | {details['Action']}")
    print(f"\nTotal Steps: {i} | Path Cost: {i}")
vacuum_agent()