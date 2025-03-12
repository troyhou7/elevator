import sys

TIME_BETWEEN_FLOORS = 10
START_ARG = "start"
FLOORS_ARG = "floors"

def elevator():
	if len(sys.argv) != 3:
		arg_error()
	args = {}
	for arg in sys.argv[1:]:
		if "=" not in arg:
			arg_error()
		key, val = arg.split("=")
		args[key] = val

	if START_ARG not in args or FLOORS_ARG not in args:
		arg_error()

	try:
		start_floor = int(args[START_ARG])
		visit_floors = [int(num) for num in args[FLOORS_ARG].split(",")]

		print(start_floor)
		if start_floor < 1:
			print("Starting floor " + str(start_floor) + " invalid.  Must be 1 or greater.")
			sys.exit(1)
		for num in visit_floors:
			if num < 1:
				print("Invalid floor to visit: " + str(num) + ". Must be 1 or greater")
				sys.exit(1)

		# Assumption: All buttons are pressed at the beginning, meaning elevator will continue its direction and stop at each floor along the way-- not first pressed first
		# Assumption: no duplicate floors -- assuming this is one elevator ride starting when someone gets in at start_floor, then presses all buttons in the list
		visit_floors.append(start_floor)
		visit_floors = list(set(visit_floors))
		visit_floors.sort()

		# Assumption: Direction of elevator is down if there are any floors pressed that are lower than the starting floor
		down_first = visit_floors[0] != start_floor
		cur_floor = start_floor
		visited = [start_floor]
		time_total = 0

		# With our assumptions, the time total will always be one of the following:
		# Down only: (start_floor - lowest_floor)*TIME_BETWEEN_FLOORS
		# Down and Up : (start_floor - lowest_floor)*TIME_BETWEEN_FLOORS + (highest_floor - lowest_floor)*TIME_BETWEEN_FLOORS 
		# Up only : (highest_floor - lowest_floor)*TIME_BETWEEN_FLOORS

		if down_first:
			visit_down = []
			visit_up = []
			# Option: Could use binary search to find index of start_floor to split the array more efficiently
			for num in visit_floors:
				if num < start_floor:
					visit_down.append(num)
				elif num > start_floor:
					visit_up.append(num)

			# Start visiting lower floors in descending order.  At each, add the time it took to get there and update current floor
			for i in range(len(visit_down) - 1, -1, -1):
				visited.append(visit_down[i])
				time_total += (cur_floor - visit_down[i])*TIME_BETWEEN_FLOORS
				cur_floor = visit_down[i]
			# Same thing but now we start going back up the higher floors
			for new_floor in visit_up:
				visited.append(new_floor)
				time_total += (new_floor - cur_floor)*TIME_BETWEEN_FLOORS
				cur_floor = new_floor
		else:
			# We are just going up from current floor, so incrementally add everything after first index
			for i in range(1, len(visit_floors), 1):
				visited.append(visit_floors[i])
				time_total += (visit_floors[i] - cur_floor)*TIME_BETWEEN_FLOORS
				cur_floor = visit_floors[i]

		visited = ",".join(str(floor) for floor in visited)
		print(time_total, visited)

	except:
		arg_error()


def arg_error():
	print("Must run script with arguments in the following format: start=<int> floors=<int1,int2,int3...>")
	sys.exit(1)

if __name__ == "__main__":
	elevator()