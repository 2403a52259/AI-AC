#!/usr/bin/env python3

"""
Temperature Conversion Utilities
- celsius_to_fahrenheit(c): Convert °C to °F
- fahrenheit_to_celsius(f): Convert °F to °C
"""

def celsius_to_fahrenheit(c):
	return c * 9/5 + 32


def fahrenheit_to_celsius(f):
	return (f - 32) * 5/9


if __name__ == "__main__":
	val = input("Enter temperature with unit (e.g., 37C or 98.6F): ").strip()
	try:
		if not val:
			raise ValueError("No input provided")
		u = val[-1].upper()
		num = float(val[:-1])
		if u == "C":
			print(f"{num}C = {celsius_to_fahrenheit(num):.2f}F")
		elif u == "F":
			print(f"{num}F = {fahrenheit_to_celsius(num):.2f}C")
		else:
			raise ValueError("Unit must be 'C' or 'F'")
	except ValueError as e:
		print(f"Error: {e}")
