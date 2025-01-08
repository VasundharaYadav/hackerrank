if __name__ == '__main__':
    n = int(input())  # Number of commands
    lst = []  # Initialize the list
    
    for _ in range(n):
        command = input().split()  # Read the command
        action = command[0]
        
        if action == "insert":
            index, value = int(command[1]), int(command[2])
            lst.insert(index, value)
        elif action == "print":
            print(lst)
        elif action == "remove":
            value = int(command[1])
            lst.remove(value)
        elif action == "append":
            value = int(command[1])
            lst.append(value)
        elif action == "sort":
            lst.sort()
        elif action == "pop":
            lst.pop()
        elif action == "reverse":
            lst.reverse()
