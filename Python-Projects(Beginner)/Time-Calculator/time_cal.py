def add_time(start: str, duration: str, day: str="") -> str:
    """ Returns the hour of the day after the sum. """

    start_h, start_m = start[:-3].split(":")
    clock = start.split()[1]  # hour format
    duration_h, duration_m = duration.split(":")

    carry_h = 0  # carrying hours
    days_n = 0  # number of X days later
    days = ""  # X days later (string-formatted)
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday",
                 "Friday", "Saturday", "Sunday"]

    # Calculate result minutes
    minutes = int(start_m) + int(duration_m)
    if minutes > 60:
        carry_h = minutes // 60
        minutes = minutes % 60
    
    # Calculate result hours
    hours = int(start_h) + int(duration_h) + carry_h
    if hours >= 12:
        if clock == "AM" and (hours // 12) % 2 == 1:
            clock = "PM"
        else:
            clock = "AM"

        # Adds days later if sum resulted in 1 or more days
        if clock == "AM":
            if (hours // 12) == 2:
                days_n = (hours // 24)
            elif (hours // 12) == 1 or (hours // 12) > 2:
                days_n = (hours // 24) + 1

        if days_n == 1:
            days = " (next day)"
        elif days_n > 1:
            days = f" ({days_n} days later)"

        hours = hours % 12
        if hours == 0:  # converts 00 to 12
            hours = 12

    if len(day) > 0:
        day_n = week_days[(week_days.index(day.title()) + days_n) % 7]
        day = f", {day_n}"

    new_time = f"{hours}:{str(minutes).rjust(2, '0')} {clock}{day}{days}"

    return new_time