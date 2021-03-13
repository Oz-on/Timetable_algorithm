# Author: Oskar Domingos
# Solution of the problem

import time
import matplotlib.pyplot as plt
from coursework.utility import load_data
from datetime import datetime


def get_difference(time1, time2):
    start = datetime.strptime(time1, "%H:%M")
    end = datetime.strptime(time2, "%H:%M")
    return (end - start).seconds / 3600


class Tree:
    def __init__(self, root_key):
        self.key = root_key
        self.time_difference = 0.0
        self.total_time = 0.0
        self.child = None

    def insert_value(self, child_key):
        difference = get_difference(self.key, child_key)
        if difference > self.time_difference:
            self.time_difference = difference
            self.total_time += self.time_difference
            self.child = Tree(child_key)

    def insert_tree(self, tree):
        difference = get_difference(self.key, tree.get_root_val())
        if self.child is None or tree.total_time > self.child.total_time:
            self.time_difference = difference
            self.total_time = self.time_difference + tree.total_time
            self.child = tree

    def get_root_val(self):
        return self.key

    def get_child(self):
        return self.child


def get_leaf(tree):
    if tree.get_child() is None:
        return tree.get_root_val()
    return get_leaf(tree.get_child())


def get_period(slots):
    max_duration = 0
    max_tree = None

    periods = {}
    for i in range(len(slots) - 1, -1, -1):
        start, end = slots[i].split(' ')
        if start not in periods.keys():
            periods[start] = Tree(start)
        if end in periods.keys():
            periods[start].insert_tree(periods[end])
            del periods[end]
        else:
            periods[start].insert_value(end)

    for tree in periods.values():
        if tree.total_time > max_duration:
            max_duration = tree.total_time
            max_tree = tree

    return [max_tree.get_root_val(), get_leaf(max_tree), max_duration]


if __name__ == '__main__':
    # Calculate results more time to check complexity
    x = [
        load_data('input_data_4.txt'),
        load_data('input_data_9.txt'),
        load_data('input_data_50.txt'),
        load_data('input_data_100.txt'),
        load_data('input_data_200.txt'),
        load_data('input_data_400.txt'),
        load_data('input_data_1000.txt'),
    ]
    y = []

    for m in x:
        time_start = time.time()
        get_period(m)
        y.append(time.time() - time_start)

    plt.plot([len(m) for m in x], y, 'r')
    plt.xlabel('Data size')
    plt.ylabel('Running time in seconds')
    plt.title('Algorithm analysis')
    plt.show()
