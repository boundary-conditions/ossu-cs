def add_time(start, duration, start_day=None):
    week_day = {"monday":1,
                "tuesday":2,
                "wednesday":3,
                "thursday":4,
                "friday":5,
                "saturday":6,
                "sunday":7,
                1:"Monday",
                2:"Tuesday",
                3:"Wednesday",
                4:"Thursday",
                5:"Friday",
                6:"Saturday",
                0:"Sunday"
                }
    if start_day != None:
        day_value = week_day[start_day.lower()]
    
    start_hour, start_minute = start.split(':')
    start_minute, half = start_minute.split()
    duration_hour, duration_minute = duration.split(':')
    new_minute = int(duration_minute) + int(start_minute)
    
    extra_hour = 0
    if  new_minute >= 60:
        extra_hour = 1
        new_minute = new_minute - 60
    if new_minute < 10:
        new_minute = f"0{str(new_minute)}"
    
    total_hours = int(start_hour) + int(duration_hour) + extra_hour
    twelve_hour_blocks = total_hours // 12
    new_hour = total_hours - (twelve_hour_blocks * 12)
    if new_hour == 0:
        new_hour = 12
    days_later = twelve_hour_blocks // 2
    switch_half = twelve_hour_blocks % 2
    if switch_half == 1:
        if half == "PM":
            days_later += 1
            half = "AM"
        else:
            half = "PM"
    if start_day == None:        
        if days_later == 0:
            new_time = f"{new_hour}:{new_minute} {half}"
        elif days_later == 1:
            new_time = f"{new_hour}:{new_minute} {half} (next day)"
        else:
            new_time = f"{new_hour}:{new_minute} {half} ({days_later} days later)"
    elif start_day != None:
        new_day = (day_value + days_later) % 7
        if days_later == 0:
            new_time = f"{new_hour}:{new_minute} {half}, {week_day[new_day]}"
        elif days_later == 1:
            new_time = f"{new_hour}:{new_minute} {half}, {week_day[new_day]} (next day)"
        else:
            new_time = f"{new_hour}:{new_minute} {half}, {week_day[new_day]} ({days_later} days later)"
    return new_time




    #return new_time