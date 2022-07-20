#For this exercise, then, we’ll assume that you run 10 km
#each day as part of your exercise regime.
#You want to know how long, on average, that run takes.
##
##Write a function (run_timing) that asks how long it
##took for you to run 10 km.The function continues to ask how
##long (in minutes) it took for additional runs, until
##the user presses Enter. At that point, the function
##exits—but only after calculating and displaying the
##average time that the 10 km runs took.

def run_timing():
    time_entered = 0
    total_time = 0
    trips = 0
    while True:
        
        time_entered = input('Enter 10km run time (enter to quit): ')
        if time_entered == "":
            return f'The average time for a 10km run is {total_time/trips} minutes'
        try:
            time_entered_int = int(time_entered)
        except ValueError as e:
            print('Hey thats not a number!!!')
        else:
            total_time += time_entered_int
            trips += 1
    

print(run_timing())
    
