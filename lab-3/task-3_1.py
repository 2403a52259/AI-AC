#!/usr/bin/env python3

"""
Electricity Bill Calculator (Fixed Rate)
- Uses a constant fixed rate per unit.
- Change RATE_PER_UNIT to adjust.
"""

RATE_PER_UNIT = 5.0  # ₹ per unit

def compute_bill(units, rate=RATE_PER_UNIT):
	if units < 0:
		raise ValueError("Units cannot be negative")
	return units * rate


def main():
	try:
		units_str = input("Enter units consumed: ").strip()
		if not units_str:
			raise ValueError("No input provided")
		units = float(units_str)
		bill = compute_bill(units)
		print(f"Total bill: ₹{bill:.2f}")
	except ValueError as e:
		print(f"Error: {e}")


if __name__ == "__main__":
	main()
