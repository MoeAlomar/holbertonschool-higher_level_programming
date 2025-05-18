#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    c0 = tuple_a[0] + tuple_b[0]
    c1 = tuple_a[1] + tuple_b[1]

    tuple_c = (c0, c1)
    return tuple_c
