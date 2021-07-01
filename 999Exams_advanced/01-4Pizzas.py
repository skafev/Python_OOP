from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
employee = [int(x) for x in input().split(", ")]
pizzas_made = 0
is_complied = False

while True:
    is_complied = False

    if len(employee) == 0:
        print(f"Not all orders are completed.\n"f'Orders left: {", ".join(map(str, pizza_orders))}')
        break
    if len(pizza_orders) == 0:
        print(f"All orders are successfully completed!\n"
              f""f"Total pizzas made: {pizzas_made}\n"
              f""f"Employees: {', '.join(map(str, employee))}")
        break
    current_order = pizza_orders.popleft()
    order_for_pizza = current_order
    current_employee = employee.pop()
    if current_order > 10:
        employee.append(current_employee)
        continue
    if current_order <= 0:
        employee.append(current_employee)
        continue
    if current_order <= current_employee:
        pizzas_made += current_order
    elif current_order > current_employee:
        try:
            while not is_complied:
                current_order -= current_employee
                current_employee = employee.pop()
                if current_employee >= current_order:
                    pizzas_made += order_for_pizza
                    is_complied = True
        except IndexError:
            pizza_orders.insert(0, current_order)# TO CHECK IF I HAVE TO BRING THE FULL AMOUNT OF THE ORDER
            print(f"Not all orders are completed.\n"f'Orders left: {", ".join(map(str, pizza_orders))}')
            break

