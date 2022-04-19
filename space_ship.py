import sys
import os

''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT
# Write code here
launch_time  = sys.stdin.readline()
travel_time = sys.stdin.readline()

lt_hh = int(launch_time[0:2])
lt_mm = int(launch_time[3:5])
tt_hh = int(travel_time[0:2])
tt_mm = int(travel_time[3:5])

tt_total_mm = ( tt_hh * 60 ) + tt_mm

for x in range(1, tt_total_mm+1):
    lt_mm += 1
    if lt_mm > 59:
        lt_mm = 0
        lt_hh += 1
        if lt_hh > 23:
            lt_hh = 0
print(f'{lt_hh:02d} {lt_mm:02d}')

