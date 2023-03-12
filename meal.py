def main():
    #variable clock from user
    clock = input("What time is it? ")
    
    #convert var clock into float
    period = convert(clock)

    #check period with using conditionals
    if period >= 7.0 and period <= 8.0:
        print("breakfast time")
    elif period >= 12.0 and period <= 13.0:
        print("lunch time")
    elif period >= 18.0 and period <= 19.0:
        print("dinner time")

def convert(time):
    #create variables hours and minutes
    hours, minutes = time.split(":")
    
    #convert minutes into the float
    con_minutes = int(minutes)/60
    
    #convert whole time into the float
    con_time = int(hours) + con_minutes
    
    #return converted time
    return con_time


if __name__ == "__main__":
    main()
