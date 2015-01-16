#!/usr/bin/env python

# MetData - 16/01/15 - Ben
# Read in weather type, and assign a colour marker for plotting
# Potentially still very buggy, will find out when plotting?

def w_s(integer):

	# Setup empty vector for color and marker information
	color_marker=''

	# Assign weather ID a colour and marker

	# Clear night, white circle
	if integer == 0:
		color = 'white'
		marker = 'o'

	# Sunny day, yellow circle
	elif integer == 1:
		color = 'yellow'
		marker = 'o'

	# Cloudy, grey triangle
	elif integer in [2,3,7,8]:
		color = 'grey'
		marker = '^'

	# Misty, grey square
	elif integer in [5,6]:
		color = 'grey'
		marker = 's'

	# Light rain, blue triangle
	elif integer in [9,10,11,12]:
		color = 'blue'
		marker = '^'

	# Heavy rain, dark blue triangle
	elif integer in [13, 14, 15]:
		color = 'darkblue'
		marker = '^'

	# Sleet, light blue triangle
	elif integer in [16, 17, 18]:
		color = 'lightblue'
		marker = '^'

	# Hail, white diamond
	elif integer in [19, 20, 21]:
		color = 'white'
		marker = 'D'

	# Light snow, white hexagon
	elif integer in [22, 23, 24]:
		color = 'white'
		marker = 'h'

	# Heavy snow, grey hexagon
	elif integer in [25, 26, 27]:
		color = 'grey'
		marker = 'h'

	# Thunder, yellow thin diamond
	elif integer in [28, 29, 30]:
		color = 'yellow'
		marker = 'd'
	
	# Unspecifed/null weather, black dot
	else:
		color = 'black'
		marker = '.'

	# Fill vector of colour and marker information for weather type
	color_marker=(color,marker)
	# Send weather symbol information to plotting script
	return(color_marker)


