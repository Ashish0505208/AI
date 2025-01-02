def vacuum_agent():
    states = ["A_CLEAN", "A_DIRTY", "B_CLEAN", "B_DIRTY"]
    actions = {"CLEAN": "SUCK!", "MOVE": {"A": "Move to Right", "B": "Move to Left"}}
    percept_table = {}
    steps = []

    def transition(state):
        room, status = state.split("_")
        if status == "DIRTY":
            return f"{room}_CLEAN", actions["CLEAN"]
        elif room == "A":
            return "B_DIRTY", actions["MOVE"]["A"]
        elif room == "B":
            return "A_DIRTY", actions["MOVE"]["B"]

    # Input validation for room
    room = input("Enter the starting room (A/B): ").upper()
    if room not in ["A", "B"]:
        print("Invalid room. Defaulting to room A.")
        room = "A"

    # Input validation for status
    status = input(f"Enter the status of room {room} (CLEAN/DIRTY): ").upper()
    if status not in ["CLEAN", "DIRTY"]:
        print("Invalid status. Defaulting to DIRTY.")
        status = "DIRTY"

    current_state = f"{room}_{status}"
    i = 0

    while True:
        room, status = current_state.split("_")
        print(f"\nCurrent State: Room {room}, Status: {status}")
        next_state, action = transition(current_state)
        percept_table[f"Action {i + 1}"] = {"Room": room, "Action": action}
        steps.append(action)

        print(f"Percept Table: {percept_table}")
        print(f"Action Taken: {action}")
        print(f"Transitioning to: {next_state}\n")

        current_state = next_state
        i += 1

        # Prompt user to continue or terminate
        user_input = input("Continue to the next action? (yes/no): ").lower()
        if user_input == "no":
            print("\nTerminating the program. Goodbye!")
            break

    print(f"\nTotal Steps Taken: {len(steps)}")
    print(f"Path Cost: {len(steps)}")
    print("Final Percept Table:")
    for action, details in percept_table.items():
        print(f"{action}: {details}")

# Run the vacuum agent
vacuum_agent()