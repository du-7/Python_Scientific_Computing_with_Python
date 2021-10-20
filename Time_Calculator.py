def add_time(start, duration, weekday = False):

    days_dict = dict()

    days_dict = {"monday": 0, "tuesday": 1, "wednesday": 2, "thusday": 3, "friday": 4, "saturday": 5, "sunday": 6}

    days_list = ["Monday", "Tuesday", "Wednesday", "Thusday", "Friday", "Saturday", "Sunday"]

    for d, k in days_dict.items():
        #print(d , "  " , k)
        continue

    start_hour = ""
    start_minute = ""
    am_pm = ""

    duration_hour = ""
    duration_minute = ""
    
    hour_increment = 0
    day_increment = 0
    day_str = ""
    day_flag = False
    day_number = 0
    
    rst_hour = 0
    rst_minute = 0

    start_24 = ""

    new_start = start.split(" ")
    am_pm = new_start[1]
    start_hour = int(new_start[0].split(":")[0])
    start_minute = int(new_start[0].split(":")[1])

    #print (start_hour , "__:__" , start_minute , "__:__" , am_pm)

    if am_pm =="PM" and start_hour < 12:
        start_hour = start_hour + 12
    
    if am_pm =="AM" and start_hour == 12:
        start_hour = start_hour - 12

    #print (start_hour , "__:__" , start_minute)


    new_duration = duration.split(":")
    duration_hour = int(new_duration[0])
    duration_minute = int(new_duration[1])

    #sum minutes

    if start_minute + duration_minute > 60:
        hour_increment = 1
        rst_minute = start_minute + duration_minute - 60
    else: 
        rst_minute = start_minute + duration_minute

    #sum hours

    if (start_hour + duration_hour + hour_increment) >= 24:
        rst_hour = (start_hour + duration_hour + hour_increment) % 24
        day_flag = True
    else:
        rst_hour = hour_increment + start_hour + duration_hour

    #days increment
    if day_flag == True:
        day_increment = int(((start_hour + duration_hour + hour_increment) - ((start_hour + duration_hour + hour_increment) % 24)) / 24)
    
    if day_increment == 1:
        day_str = " (next day)"
    elif day_increment > 1:
        day_str = " (" + str(day_increment) + " days later)"
    
    #calculate final time in format AM_PM
    if rst_minute < 10:
        rst_minute = ("0" + str(rst_minute))
    else:
        rst_minute = str(rst_minute)

    if rst_hour > 12:
        if len(str(rst_hour - 12)) == 1:
            new_time = str(rst_hour-12) + ":" + rst_minute + " PM"
        else:
            new_time = str(rst_hour-12) + ":"+ rst_minute+ " PM"
    elif rst_hour == 12:
        new_time = str(rst_hour) + ":" + rst_minute + " PM"
    elif rst_hour == 0:
        new_time = str(rst_hour+12) + ":" + rst_minute + " AM"
    else:
        if len(str(rst_hour)) == 1:
            new_time = str(rst_hour) + ":" + rst_minute + " AM"
        else:
            new_time = str(rst_hour) + ":"+ rst_minute+ " AM"
    
    if weekday:
        weekday = weekday.lower()
        day_number = days_dict[weekday]
        # print(day_number)

        if day_increment == 0:
            new_time = new_time + ", " + days_list[day_number]
        elif day_increment>=1 and day_increment + day_number <= 6:
            new_time = new_time + ", " + days_list[day_increment + day_number]
        elif day_increment>=1 and day_increment + day_number > 6:
            r = (day_increment + day_number) % 7

            new_time = new_time + ", " + days_list[r]    
    if len(day_str)>1:
        new_time = new_time + day_str
    
    
    return new_time

print(add_time("8:16 PM", "466:02", "tuesday"))
