n = int(input())
my_dict = {}

for i in range(n):
    plant, rarity = input().split("<->")
    if plant not in my_dict.keys():
        my_dict[plant]["Rate"] = rarity
    else:
        my_dict[plant] += rarity

while True:
    command = input()
    if command == "Exhibition":
        break
    command_one = command.split(":")
    if command_one[0] == "Rate":
        plant_command = command_one[1].split("- ")
        plant = plant_command[0].strip()
        rate = plant_command[1]
        if plant not in my_dict.keys():
            continue
        else:
            my_dict[plant].append(rate)
