# readrides.py

import csv

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

# # A dictionary
# row = {
#     'route': route,
#     'date': date,
#     'daytype': daytype,
#     'rides': rides,
# }

def read_rides_as_dictionary(filename):
    '''
    Read the bus ride data as a list of dictionaries
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides,
            }
            records.append(record)
    return records

# # A class
# class Row:
#     def __init__(self, route, date, daytype, rides):
#         self.route = route
#         self.date = date
#         self.daytype = daytype
#         self.rides = rides

def read_rides_as_class(filename):
    '''
    Read the bus ride data as a list of objects from a class
    '''
    records = []

    class Row:
        def __init__(self, route, date, daytype, rides):
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides

    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records

# # A named tuple
from collections import namedtuple
# Row = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])

def read_rides_as_named_tuple(filename):
    '''
    Read the bus ride data as a list of named tuples
    '''
    records = []

    Row = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])

    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records

# # A class with __slots__
# class Row:
#     __slots__ = ['route', 'date', 'daytype', 'rides']
#     def __init__(self, route, date, daytype, rides):
#         self.route = route
#         self.date = date
#         self.daytype = daytype
#         self.rides = rides

def read_rides_as_class_with_slots(filename):
    '''
    Read the bus ride data as a list of objects from class with slots
    '''
    records = []

    class Row:
        __slots__ = ['route', 'date', 'daytype', 'rides']
        def __init__(self, route, date, daytype, rides):
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides

    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records


from dataclasses import dataclass

def read_rides_as_data_class(filename):
    '''
    Read the bus ride data as a list of objects from a data class
    '''
    records = []
    
    @dataclass
    class Row:
        route: str
        date: str
        daytype: str
        rides: int

    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_data_class_with_slots(filename):
    '''
    Read the bus ride data as a list of objects from a data class with slots
    '''
    records = []
    
    @dataclass(slots=True)
    class Row:
        route: str
        date: str
        daytype: str
        rides: int

    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_tuples('Data/ctabus.csv')
    print('Memory Use (Tuple): Current %.2fMB, Peak %.2fMB' % tuple(x / (1024 * 1024) for x in tracemalloc.get_traced_memory()))
    
    tracemalloc.clear_traces()

    rows = read_rides_as_dictionary('Data/ctabus.csv')
    print('Memory Use (Dictionary): Current %.2fMB, Peak %.2fMB' % tuple(x / (1024 * 1024) for x in tracemalloc.get_traced_memory()))
    
    tracemalloc.clear_traces()

    rows = read_rides_as_class('Data/ctabus.csv')
    print('Memory Use (Class): Current %.2fMB, Peak %.2fMB' % tuple(x / (1024 * 1024) for x in tracemalloc.get_traced_memory()))
    
    tracemalloc.clear_traces()

    rows = read_rides_as_named_tuple('Data/ctabus.csv')
    print('Memory Use (Named Tuple): Current %.2fMB, Peak %.2fMB' % tuple(x / (1024 * 1024) for x in tracemalloc.get_traced_memory()))
    
    tracemalloc.clear_traces()

    rows = read_rides_as_class_with_slots('Data/ctabus.csv')
    print('Memory Use (Class with Slots): Current %.2fMB, Peak %.2fMB' % tuple(x / (1024 * 1024) for x in tracemalloc.get_traced_memory()))
    
    tracemalloc.clear_traces()

    rows = read_rides_as_data_class('Data/ctabus.csv')
    print('Memory Use (Data Class): Current %.2fMB, Peak %.2fMB' % tuple(x / (1024 * 1024) for x in tracemalloc.get_traced_memory()))
    
    tracemalloc.clear_traces()

    rows = read_rides_as_data_class_with_slots('Data/ctabus.csv')
    print('Memory Use (Data Class with Slots): Current %.2fMB, Peak %.2fMB' % tuple(x / (1024 * 1024) for x in tracemalloc.get_traced_memory()))