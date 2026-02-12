messages = ["Hi", "Welcome to the platform", "OK"]

lengths = [len(message) for message in messages]

for message, length in zip(messages, lengths):
    print("Message:", message)
    print("Length:", length)

    if length > 10:
        print(" --> Long message detected")

    print()
