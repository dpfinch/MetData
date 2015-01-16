#!/usr/bin/env python

# MetData - 16/01/15 - Ben
# Read in weather type, and assign a colour marker for plotting
# Potentially still very buggy, will find out when plotting?

def w_s(integer):

	# Setup empty vector for color and marker information
	output=''

	# Assign weather ID a colour and marker

	# Clear night, white circle
	if integer == 0:
		color = 'white'
		marker = 'o'
		type = 'Clear Night'

	# Sunny day, yellow circle
	elif integer == 1:
		color = 'yellow'
		marker = 'o'
		type = 'Sunshine'

	# Cloudy, grey triangle
	elif integer in [2,3,7,8]:
		color = 'grey'
		marker = '^'
		type = 'Cloudy'

	# Misty, grey square
	elif integer in [5,6]:
		color = 'grey'
		marker = 's'
		type = 'Misty'

	# Light rain, blue triangle
	elif integer in [9,10,11,12]:
		color = 'blue'
		marker = '^'
		type = 'Light Rain'

	# Heavy rain, dark blue triangle
	elif integer in [13, 14, 15]:
		color = 'darkblue'
		marker = '^'
		type = 'Heavy Rain'

	# Sleet, light blue triangle
	elif integer in [16, 17, 18]:
		color = 'lightblue'
		marker = '^'
		type = 'Sleet'

	# Hail, white diamond
	elif integer in [19, 20, 21]:
		color = 'white'
		marker = 'D'
		type = 'Hail'

	# Light snow, white hexagon
	elif integer in [22, 23, 24]:
		color = 'white'
		marker = 'h'
		type = 'Light Snow'

	# Heavy snow, grey hexagon
	elif integer in [25, 26, 27]:
		color = 'grey'
		marker = 'h'
		type = 'Heavy Snow'

	# Thunder, yellow thin diamond
	elif integer in [28, 29, 30]:
		color = 'yellow'
		marker = 'd'
		type = 'Thunder'
	
	# Unspecifed/null weather, black dot
	else:
		color = 'black'
		marker = '.'
		type = 'Undefined'

	# Fill vector of colour and marker information for weather type
	output=(color,marker,type)
	# Send weather symbol information to plotting script
	return(output)


