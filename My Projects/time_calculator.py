def add_time(start, duration, day=None):
    global new_time
    # get the user's day input
    st_date = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7}

    # after adding the time gives out the new date
    new_date = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 0: "Sunday"}

    # get the start_time number(hour, min)
    num1 = start.split(":")
    st_hour = int(num1[0])
    am_pm = num1[1].split()  # split again because of the AM, PM
    st_min = int(am_pm[0])

    # get the duration_time number(hour, min)
    num2 = duration.split(":")
    dr_hour = int(num2[0])
    dr_min = int(num2[1])

    # the new added time
    new_hour = st_hour + dr_hour
    new_min = st_min + dr_min
    no_of_days = 0

    # min
    if new_min >= 60:
        min = new_min // 60
        new_hour += min  # add an hour for every 60 min
        new_min = new_min % 60  # makes the minute less than 60

    # makes it two zero if new_min only got one zero
    if new_min == 0:
        new_min = "00"

        # makes a zero in front if there is only one number in new_min
    elif new_min < 10:
        new_min = "0{}".format(new_min)

    n = new_hour // 12
    # makes the hour less than 12
    while n >= 1 and new_hour > 12:
        new_hour = new_hour % 12
        if new_hour == 0:
            new_hour = 12
            break

    # make AM, PM changes
    while n >= 1:
        if st_hour == 12 and n == 1:
            am_pm[1] = am_pm[1]
            break

        if n >= 1 and am_pm[1] == "AM":
            am_pm[1] = "PM"
            n -= 1
        elif n >= 1 and am_pm[1] == "PM":
            am_pm[1] = "AM"
            no_of_days += 1  # add a number of day after PM change to AM
            n -= 1

    # for user to input day if they want to
    if day is not None:
        st_day = day.capitalize()
        find = st_date[st_day]
        find = (find + no_of_days) % 7
        new_day = new_date[find]
        if no_of_days == 1:
            new_time = f"{new_hour}:{new_min} {am_pm[1]}, {new_day} (next day)"
        elif no_of_days == 0:
            new_time = f"{new_hour}:{new_min} {am_pm[1]}, {st_day}"
        else:
            new_time = f"{new_hour}:{new_min} {am_pm[1]}, {new_day} ({no_of_days} days later)"
    else:
        if no_of_days == 1:
            new_time = f"{new_hour}:{new_min} {am_pm[1]} (next day)"
        elif no_of_days == 0:
            new_time = f"{new_hour}:{new_min} {am_pm[1]}"
        else:
            new_time = f"{new_hour}:{new_min} {am_pm[1]} ({no_of_days} days later)"

    return new_time
