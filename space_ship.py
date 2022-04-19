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

add_hh = lt_hh + tt_hh
if add_hh >= 24:
    add_hh -= 24
add_mm = lt_mm + tt_mm
if add_mm >= 60:
    add_mm -= 60
    add_hh += 1

attack_time = f'{add_hh} {add_mm}'
print(attack_time)
