"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    
    """
    Calculate the bake time remaining.
    parameters: elapsed_bake_time
    returns : remaining bake time
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    
    


#TODO (student): Define the 'preparation_time_in_minutes()' function below."""
def preparation_time_in_minutes(number_of_layers):
    """
    Calculate the preparation time in minutes.
    parameters: number_of_layers
    returns : preparation time
    """
    return number_of_layers*PREPARATION_TIME


#TODO (student): define the 'elapsed_time_in_minutes()' function below.

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate the elapsed time in minutes.
    parameters: number_of_layers, elapsed_bake_time
    returns : elapsed time
    """
    return preparation_time_in_minutes(number_of_layers)+ elapsed_bake_time
    


# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
