def get_chatbot_response(message):
    if message[:2] != "!!":
        return ''

    points, command, args = message.split(' ', 2)
    if command == "Hey":
        return "What's up!"
    elif command == "add":
        num1, num2 = args.split()
        return int(num1) + int(num2)
    elif command == "divide":
        
        num1, num2 = args.split()
        if int(num2) == 0:
            return "Invalid number: 0 try another"
        return float(num1) / float(num2)
    elif command == "say":
        return args
    else:
        return "Oops! I didn't recognize your command :("
