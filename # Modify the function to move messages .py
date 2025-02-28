# Modify the function to move messages to a new list
def send_messages(messages, sent_messages):
    """Prints each message and moves it to a new list."""
    while messages:  # Loop until the messages list is empty
        message = messages.pop(0)  # Remove the first message from the list
        print(f"Sending message: {message}")  # Print the message being sent
        sent_messages.append(message)  # Add it to the sent messages list

# List of messages to be sent
messages_list = ["Hello!", "How are you?", "Python rocks!", "Keep calm and learn Python"]

# List to store sent messages
sent_messages_list = []

# Call the function to send messages
send_messages(messages_list, sent_messages_list)

# Print both lists to confirm changes
print("\nRemaining messages:", messages_list)  # Should be empty after sending
print("Sent messages:", sent_messages_list)  # Should contain all sent messages
