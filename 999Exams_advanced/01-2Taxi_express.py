from collections import deque

customers = deque([int(x) for x in input().split(", ")])
taxis = [int(x) for x in input().split(", ")]
total_time = sum(customers)


def print_when_all_customers_reach_destination():
    return "All customers were driven to their destinations\n" \
           ""f"Total time: {total_time} minutes"


def print_when_they_are_customers_left():
    return "Not all customers were driven to their destinations\n" \
           ""f"Customers left: {', '.join(map(str, customers))}"


while True:
    if len(customers) == 0:
        print(print_when_all_customers_reach_destination())
        break
    if len(taxis) == 0:
        print(print_when_they_are_customers_left())
        break
    current_customer = customers.popleft()
    current_taxi = taxis.pop()
    if current_taxi < current_customer:
        customers.insert(0, current_customer)
