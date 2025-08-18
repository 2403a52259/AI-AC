#!/usr/bin/env python3

"""General temperature conversion utility: Celsius (C), Fahrenheit (F), Kelvin (K)."""


def convert_temperature(value, from_unit, to_unit):
	"""Convert temperature between C, F, and K.
	
	Args:
		value (float): temperature value
		from_unit (str): one of 'C', 'F', 'K' (case-insensitive)
		to_unit (str): one of 'C', 'F', 'K' (case-insensitive)
	
	Returns:
		float: converted temperature
	"""
	u_from = from_unit.strip().upper()
	u_to = to_unit.strip().upper()

	if u_from == u_to:
		return float(value)

	# Convert source to Celsius as a pivot
	v = float(value)
	if u_from == "C":
		c = v
	elif u_from == "F":
		c = (v - 32) * 5/9
	elif u_from == "K":
		c = v - 273.15
	else:
		raise ValueError("Unsupported from_unit. Use 'C', 'F', or 'K'.")

	# Convert Celsius to target
	if u_to == "C":
		return c
	elif u_to == "F":
		return c * 9/5 + 32
	elif u_to == "K":
		return c + 273.15
	else:
		raise ValueError("Unsupported to_unit. Use 'C', 'F', or 'K'.")
