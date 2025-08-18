#!/usr/bin/env python3

"""Factorial calculation using while loop."""


def factorial(n):
	"""Calculate factorial of a non-negative integer using while loop.
	
	Args:
		n (int): non-negative integer
		
	Returns:
		int: factorial of n
		
	Raises:
		ValueError: if n is negative
	"""
	if n < 0:
		raise ValueError("Factorial is not defined for negative numbers")
	if n == 0:
		return 1
	
	result = 1
	i = 1
	while i <= n:
		result *= i
		i += 1
	return result


if __name__ == "__main__":
	try:
		n = int(input("Enter a non-negative integer: "))
		print(f"{n}! = {factorial(n)}")
	except ValueError as e:
		print(f"Error: {e}")
