jobs = [int(x) for x in input().split(", ")]

index = int(input())
total_clock_cycles = 0

while True:
    current_value = min(jobs)
    current_index = jobs.index(current_value)
    if current_index == index:
        total_clock_cycles += current_value
        break
    total_clock_cycles += current_value
    jobs.remove(current_value)
    jobs.insert(current_index, 10000)

print(total_clock_cycles)