#!/usr/bin/env python3

"""
Electricity Bill Calculator (Assumed Slabs)

Assumptions (adjust as needed):
- First 50 units:    ₹0.50 per unit
- Next 100 units:    ₹0.75 per unit (51–150)
- Next 100 units:    ₹1.20 per unit (151–250)
- Above 250 units:   ₹1.50 per unit
- Surcharge:         20% on the energy charge
"""

def compute_bill(units):
	if units < 0:
		raise ValueError("Units cannot be negative")
	if units <= 50:
		charge = units * 0.50
	elif units <= 150:
		charge = 50 * 0.50 + (units - 50) * 0.75
	elif units <= 250:
		charge = 50 * 0.50 + 100 * 0.75 + (units - 150) * 1.20
	else:
		charge = 50 * 0.50 + 100 * 0.75 + 100 * 1.20 + (units - 250) * 1.50
	return charge * 1.20  # adding 20% surcharge


def main():
	try:
		units_str = input("Enter electricity units consumed: ").strip()
		if not units_str:
			raise ValueError("No input provided")
		units = float(units_str)
		bill = compute_bill(units)
		print(f"Total bill: ₹{bill:.2f}")
	except ValueError as e:
		print(f"Error: {e}")


if __name__ == "__main__":
	main()
