hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

total_mins = mins + dura
final_mins = total_mins % 60
additional_hours = total_mins // 60

final_hour = (hour + additional_hours) % 24

print(str(final_hour) + ":" + str(final_mins))
