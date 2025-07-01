counterEast = 0
counterWest = 0
counterNorth = 0
counterSouth = 0
currentDirection = 'N'

# Read the entire file and split into a list based on commas
with open("./myEnv/input.txt", "r") as file:
    data = file.read().strip()
    instructions = data.split(',')

for item in instructions:
    current = item.strip()
    direction = current[0]           # First letter
    number = int(current[1:])        # The rest is the number

    if direction == "R":
        if currentDirection == 'N':
            counterEast += number
            currentDirection = 'E'
        elif currentDirection == 'E':
            counterSouth += number
            currentDirection = 'S'
        elif currentDirection == 'S':
            counterWest += number
            currentDirection = 'W'
        elif currentDirection == 'W':
            counterNorth += number  
            currentDirection = 'N'
    elif direction == "L":
        if currentDirection == 'N':
            counterWest += number
            currentDirection = 'W'
        elif currentDirection == 'E':
            counterNorth += number
            currentDirection = 'N'
        elif currentDirection == 'S':
            counterEast += number
            currentDirection = 'E'
        elif currentDirection == 'W':
            counterSouth += number
            currentDirection = 'S'

print (f"East {counterEast}, West {counterWest}, North {counterNorth}, South {counterSouth}")

print(abs(counterEast - counterWest) + abs(counterNorth - counterSouth))