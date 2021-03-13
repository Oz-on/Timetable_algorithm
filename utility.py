# Author: Oskar Domingos
# This is a helper file which generates data

from datetime import datetime
import random


def load_data(file_name):
    with open(file_name, 'r') as file:
        data = file.read().split('\n')
        slots = [slot for slot in data if slot != '']

    return slots


def generate_data(n):
    filename = f'input_data_{n}.txt'
    with open(filename, 'w') as file:
        for i in range(n):
            start_hour = random.randint(7, 20)
            start_minute = random.choice([0, 30])
            end_hour = random.randint(start_hour, 23)
            if start_hour == end_hour:
                end_minute = random.choice([30])
            else:
                end_minute = random.choice([0, 30])

            slot = f'{start_hour}:{start_minute} {end_hour}:{end_minute}\n'

            file.write(slot)

    # Sort that numbers
    slots = load_data(filename)
    n = len(slots)
    # Unsorted list
    for i in range(1, n):
        # Compare with sorted list
        start1, end1 = slots[i].split(' ')
        time1_start = datetime.strptime(start1, "%H:%M")
        time1_end = datetime.strptime(end1, "%H:%M")
        for j in range(i):
            start2, end2 = slots[j].split(' ')

            time2_start = datetime.strptime(start2, "%H:%M")
            time2_end = datetime.strptime(end2, "%H:%M")
            if time1_start < time2_start:
                slots[j], slots[i] = slots[i], slots[j]

            elif time1_start == time2_start and time1_end < time2_end:
                slots[j], slots[i] = slots[i], slots[j]

    # Remove duplicates
    slots_w_d = []
    for i in range(len(slots)):
        if slots[i] not in slots_w_d:
            slots_w_d.append(slots[i])

    with open(filename, 'w') as file:
        for slot in slots_w_d:
            file.write(f'{slot}\n')


if __name__ == '__main__':
    generate_data(50)
    generate_data(100)
    generate_data(200)
    generate_data(400)