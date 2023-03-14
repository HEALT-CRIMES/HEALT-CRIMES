Create a report generation function
Your spaceship has three tanks: Main, External and Hydrogen. You want to create an app to display the amount of fuel in each tank, and 
  the average amount of fuel between the three tanks. Because you wish to reuse this code in other projects, you want to create a function with the logic.

Create a function named generate_report. The function will take three parameters named main_tank, external_tank and
hydrogen_tank. When run, the function will display output which resembles the following:




def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank} 
    """
    print(output)
    
    genrate_report(80,70,75)
    
    #######################################
    KEYWORDS
   
from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")
  
 'Arrival: Saturday 16:42'
################################################
Combination of arguments and keyword arguments
from datetime import timedelta, datetime

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")
  
 Since you've added a required argument, it's no longer possible to call the function without any arguments:
  arrival_time("Moon")
'Moon Arrival: Saturday 16:54'

##############################
Variable arguments

The arguments in the functions are required. But when variable arguments are used, the function allows you to pass any number of arguments (including 0). The syntax for using variable arguments is to prefix a single asterisk (*) before the argument name.

The following function prints the received arguments:}
  
  def variable_length(*args):
    print(args)
    
    exampple
    def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"
      
 #sequence_time(4, 14, 18)
#'Total time to launch is 36 minutes' 
#sequence_time(4, 14, 48)
#'Total time to launch is 1.1 hours'
    #
    #############################################################
    For a function to accept any number of keyword arguments, it must use a similar syntax. In this case, a double asterisk is required:
      def variable_length(**kwargs):
    print(kwargs)
    
     variable_length(tanks=1, day="Wednesday", pilots=3)#Assigns them as a dictionary
{'tanks': 1, 'day': 'Wednesday', 'pilots': 3}
######################
def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")
 Apollo 11 crew:
  
>>> crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")
3 astronauts assigned for this mission:
captain: Neil Armstrong
pilot: Buzz Aldrin
command_pilot: Michael Collins
    
  
  
