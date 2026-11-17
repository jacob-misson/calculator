#choose unit to convert from
#choose second unit to convert to
#given a value in the first unit, convert it to the second unit

def convert_distance_units(value, from_unit, to_unit):
    # Define conversion factors for different units
    conversion_factors = {
        ("m", "cm"): 100,
        ("cm", "m"): 0.01,
        ("km", "m"): 1000,
        ("m", "km"): 0.001,
        ("in", "cm"): 2.54,
        ("cm", "in"): 0.393701,
        ("ft", "m"): 0.3048,
        ("m", "ft"): 3.28084,
        ("ft", "in"): 12,
        ("in", "ft"): 0.0833333,
        ("km", "mi"): 0.621371,
        ("mi", "km"): 1.60934,
        ("yd", "m"): 0.9144,
        ("m", "yd"): 1.09361,
        ("yd", "ft"): 3,
        ("ft", "yd"): 0.333333,
        ("yd", "in"): 36,
        ("in", "yd"): 0.0277778,
        ("mi", "ft"): 5280,
        ("ft", "mi"): 0.000189394,
        ("mi", "in"): 63360,
        ("in", "mi"): 0.0000157828,
        ("mi", "yd"): 1760,
        ("yd", "mi"): 0.000568182,
        ("meters", "centimeters"): 100,
        ("centimeters", "meters"): 0.01,
        ("kilometers", "meters"): 1000,
        ("meters", "kilometers"): 0.001,
        ("inches", "centimeters"): 2.54,
        ("centimeters", "inches"): 0.393701,
        ("feet", "meters"): 0.3048,
        ("meters", "feet"): 3.28084,
        ("feet", "inches"): 12,
        ("inches", "feet"): 0.0833333,
        ("kilometers", "miles"): 0.621371,
        ("miles", "kilometers"): 1.60934,
        ("yards", "meters"): 0.9144,
        ("meters", "yards"): 1.09361,
        ("yards", "feet"): 3,
        ("feet", "yards"): 0.333333,
        ("yards", "inches"): 36,
        ("inches", "yards"): 0.0277778,
        ("miles", "feet"): 5280,
        ("feet", "miles"): 0.000189394,
        ("miles", "inches"): 63360,
        ("inches", "miles"): 0.0000157828,
        ("miles", "yards"): 1760,
        ("yards", "miles"): 0.000568182
        }
    if from_unit == to_unit:
        return value
    
    if (from_unit, to_unit) in conversion_factors:
        return value * conversion_factors[(from_unit, to_unit)]   

from_unit = input("Enter the unit to convert from: ")
if from_unit not in ["m", "cm", "km", "in", "ft", "mi", "yd", "meters", "centimeters", "kilometers", "inches", "feet", "miles", "yards"]:
        print("Invalid unit. Supported units are: m, cm, km, in, ft, mi, yd.")
        from_unit = input("Enter the unit to convert from (e.g., m, cm, km, in, ft, mi, yd): ")

value = float(input("Enter the value to convert: "))

to_unit = input("Enter the unit to convert to: ")
if to_unit not in ["m", "cm", "km", "in", "ft", "mi", "yd", "meters", "centimeters", "kilometers", "inches", "feet", "miles", "yards"]:
        print("Invalid unit. Supported units are: m, cm, km, in, ft, mi, yd.")
        to_unit = input("Enter the unit to convert to (e.g., m, cm, km, in, ft, mi, yd): ")

print(f"{value} {from_unit} is equal to {convert_distance_units(value, from_unit, to_unit)} {to_unit}")