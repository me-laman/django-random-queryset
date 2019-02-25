# encoding: utf-8
from __future__ import division

import math
import random


class SmallPopulationSize(Exception):
    pass


def min_max(sample_size, min_id, max_id, rows_count):
    assert (max_id - min_id) + 1 == rows_count
    population = list(range(min_id, max_id + 1))
    return random.sample(population, sample_size)


def random_count(selected_ids, amount):
    return random.sample(list(selected_ids), amount)
