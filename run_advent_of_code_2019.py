from day_1 import get_total_fuel, get_total_fuel_correct
from day_2 import get_first_code_of_restored_gravity_assist_test_program, get_input_of_restored_gravity_assist_program
from day_3 import get_manhattan_distance_from_central_point, get_minimized_signal_delay_from_central_point

# -- Day 1 -------------------------------------------------------------------------------------------------------------

total_fuel = get_total_fuel()

print "Total fuel required is: " + str(total_fuel) + "\n"

total_fuel = get_total_fuel_correct()

print "Total correct fuel required is: " + str(total_fuel) + "\n"

# -- Day 2 -------------------------------------------------------------------------------------------------------------

print "The restored test program is: " + str(get_first_code_of_restored_gravity_assist_test_program()) + "\n"

print "The input of restored program is: " + str(get_input_of_restored_gravity_assist_program()) + "\n"

# -- Day 3 -------------------------------------------------------------------------------------------------------------

print "The Manhattan distance is: " + str(get_manhattan_distance_from_central_point()) + "\n"

print "The minimized signal delay is: " + str(get_minimized_signal_delay_from_central_point()) + "\n"
