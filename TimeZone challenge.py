# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

# My solution

import datetime
import pytz
import random
My_tuple =()

for x in sorted(pytz.country_names):
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            My_tuple += ([x,pytz.country_names[x],zone],)# My_tuple contains all the conbination code country, country, timezone
    else:
        continue

rand_choise = random.sample(My_tuple, 9)                # I choise random 9 of these

key_choise = {}
ind = 1
for item in rand_choise:                                  # I create a key to do a choise after
    code, name, timezone = item
    key_choise.setdefault(ind, []).append(item)
    ind += 1


while True:
    for y in range(1,10):
        print(y,key_choise[y])                            # I print all the 9 opportunities
    code = int(input("\nDigit the code about the timezone you want the time + Enter (0 to Exit) : "))

    if code == 0:                                        # Exit from the program
        break
    if code > 9:
        print("You digit a code out of range!\n")
    else:
        for code, name, timezone in key_choise[code]:
            my_timezone =  timezone
            tz_to_disply = pytz.timezone(my_timezone)
            aware_local_time = datetime.datetime.now(tz=tz_to_disply) #local time in the timezone choised
            print("\nAware local time {}, time zone {} ".format(aware_local_time, tz_to_disply))
            utc_time = datetime.datetime.utcnow() #UtC time
            aware_utc_time = pytz.utc.localize(utc_time)# UTC time with localisation
            print("Aware UTC {}, time zone {}  \n\n".format(aware_utc_time, aware_utc_time.tzinfo))


# # Tim Buchalka solution: I prefer my solution a part the print out (strftime('%A %x %X %z')) I had to do this.
#
# import datetime
# import pytz
#
# available_zones = {'1': "Africa/Tunis",
#                    '2': "Asia/Kolkata",
#                    '3': "Australia/Adelaide",
#                    '4': "Europe/Brussels",
#                    '5': "Europe/London",
#                    '6': "Japan",
#                    '7': "Pacific/Tahiti",
#                    '8': "US/Hawaii",
#                    '9': "Zulu"}
#
# print("Please choose a time zone (or 0 to quit):")
# for place in sorted(available_zones):
#     print("\t{}. {}".format(place, available_zones[place]))
#
# while True:
#     choice = input()
#
#     if choice == '0':
#         break
#
#     if choice in available_zones.keys():
#         tz_to_display = pytz.timezone(available_zones[choice])
#         world_time = datetime.datetime.now(tz=tz_to_display)
#         print("The time in {} is {} {}".format(available_zones[choice], world_time.strftime('%A %x %X %z'),world_time.tzname()))
#         print("Local time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
#         print("UTC time is {}".format(datetime.datetime.utcnow().strftime('%A %x %X')))
#         print()

