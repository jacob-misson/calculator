WEIGHT_IN_GRAMS= {
    "mg": 0.001,
    "g": 1,
    "kg": 1000,
    "oz": 28.3495,
	"lb": 453.592,
    "stone": 6350.29,
    "ton": 907185,     #US short ton
    "tonne": 1000000,  #Metric ton
}

#Full names map to the short names
ALIASES = {
    "milligram": "mg",
    "gram": "g",
	"kilogram": "kg",
    "ounce": "oz",
    "pound": "lb",
}

def normalise_unit(unit):
    unit = unit.strip().lower()
    if unit.endswith("s") and unit[:-1] in ALIASES:
            unit = unit[:-1]
    return ALIASES.get(unit, unit)  # Return the short name if it's an alias, otherwise return the original unit

def convert_weight(value, from_unit, to_unit):
     grams = value * WEIGHT_IN_GRAMS[from_unit]
     return grams / WEIGHT_IN_GRAMS[to_unit]

def ask_unit(prompt):
    while True:
          unit = normalise_unit(input(prompt))
          if unit in WEIGHT_IN_GRAMS:
                 return unit
          print("invalid unit")

def ask_number(prompt):
    while True:
          try:
                return float(input(prompt))
          except ValueError:
                print("Please enter a number")
                
units = ", ".join(WEIGHT_IN_GRAMS)
from_unit = ask_unit(f"Enter the unit to convert from ({units}): ")
value = ask_number("Enter the value to convert: ")
to_unit = ask_unit(f"Enter the unit to convert to {units}): ")

result = convert_weight(value, from_unit, to_unit)
print(f"{value} {from_unit} is equal to {result:.6g} {to_unit}")
