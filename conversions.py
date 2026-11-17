
def convert_weight_units(value, from_unit, to_unit):
    conversion_factors = {
        ("kg", "g"): 1000,
        ("g", "kg"): 0.001,
        ("lb", "kg"): 0.453592,
        ("kg", "lb"): 2.20462,
        ("oz", "g"): 28.3495,
        ("g", "oz"): 0.035274,
        ("lb", "oz"): 16,
        ("oz", "lb"): 0.0625,
        ("mg", "g"): 0.001,
        ("g", "mg"): 1000,
        ("kg", "mg"): 1000000,
        ("mg", "kg"): 0.000001,
        ("lb", "mg"): 453592,
        ("mg", "lb"): 0.00000220462,
        ("oz", "mg"): 28349.5,
        ("mg", "oz"): 0.000035274,
        ("stone", "kg"): 6.35029,
        ("kg", "stone"): 0.157473,
        ("stone", "lb"): 14,
        ("lb", "stone"): 0.0714286,
        ("stone", "oz"): 224,
        ("oz", "stone"): 0.00446429,
        ("ton", "kg"): 907.185,
        ("kg", "ton"): 0.00110231,
        ("ton", "lb"): 2000,
        ("lb", "ton"): 0.0005,
        ("ton", "oz"): 32000,
        ("oz", "ton"): 0.00003125,
        ("tonne", "kg"): 1000,
        ("kg", "tonne"): 0.001,
        ("tonne", "lb"): 2204.62,
        ("lb", "tonne"): 0.000453592,
        ("tonne", "oz"): 35273.96,
        ("oz", "tonne"): 0.0000283495,
        ("tonne", "ton"): 0.984207,
        ("ton", "tonne"): 1.01605,
        ("tonne", "stone"): 157.473,
        ("stone", "tonne"): 0.00635029,
        ("tonne", "mg"): 1000000000,
        ("mg", "tonne"): 0.000000001,
        ("tonne", "g"): 1000000,
        ("g", "tonne"): 0.000001,
        ("tonne", "oz"): 35273.96,
        ("oz", "tonne"): 0.0000283495,
        ("tonne", "lb"): 2204.62,
        ("lb", "tonne"): 0.000453592,
        ("tonne", "ton"): 0.984207,
        ("kilogram", "gram"): 1000,
        ("gram", "kilogram"): 0.001,
        ("pound", "kilogram"): 0.453592,
        ("kilogram", "pound"): 2.20462,
        ("ounce", "gram"): 28.3495,
        ("gram", "ounce"): 0.035274,
        ("pound", "ounce"): 16,
        ("ounce", "pound"): 0.0625,
        ("milligram", "gram"): 0.001,
        ("gram", "milligram"): 1000,
        ("kilogram", "milligram"): 1000000,
        ("milligram", "kilogram"): 0.000001,
        ("pound", "milligram"): 453592,
        ("milligram", "pound"): 0.00000220462,
        ("ounce", "milligram"): 28349.5,
        ("milligram", "ounce"): 0.000035274,
        ("stone", "kilogram"): 6.35029,
        ("kilogram", "stone"): 0.157473,
        ("stone", "pound"): 14,
        ("pound", "stone"): 0.0714286,
        ("stone", "ounce"): 224,
        ("ounce", "stone"): 0.00446429,
        ("ton", "kilogram"): 907.185,
        ("kilogram", "ton"): 0.00110231,
        ("ton", "pound"): 2000,
        ("pound", "ton"): 0.0005,
        ("ton", "ounce"): 32000,
        ("ounce", "ton"): 0.00003125
    }
    if from_unit == to_unit:
        return value
    
    if (from_unit, to_unit) in conversion_factors:
        return value * conversion_factors[(from_unit, to_unit)]

def convert_temperature_units(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    if from_unit == "C" and to_unit == "F":
        return (value * 9/5) + 32
    elif from_unit == "F" and to_unit == "C":
        return (value - 32) * 5/9
    elif from_unit == "C" and to_unit == "K":
        return value + 273.15
    elif from_unit == "K" and to_unit == "C":
        return value - 273.15
    elif from_unit == "F" and to_unit == "K":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "K" and to_unit == "F":
        return (value - 273.15) * 9/5 + 32

def convert_volume_units(value, from_unit, to_unit):
    # Define conversion factors for different units
    conversion_factors = {
        ("L", "mL"): 1000,
        ("mL", "L"): 0.001,
        ("gal", "L"): 3.78541,
        ("L", "gal"): 0.264172,
        ("qt", "L"): 0.946353,
        ("L", "qt"): 1.05669,
        ("pt", "L"): 0.473176,
        ("L", "pt"): 2.11338,
        ("cup", "mL"): 240,
        ("mL", "cup"): 0.00416667,
        ("fl oz", "mL"): 29.5735,
        ("mL", "fl oz"): 0.033814,
        ("tbsp", "mL"): 14.7868,
        ("mL", "tbsp"): 0.067628,
        ("tsp", "mL"): 4.92892,
        ("mL", "tsp"): 0.202884,
        ("Litre", "Millilitre"): 1000,
        ("Millilitre", "Litre"): 0.001,
        ("Gallon", "Litre"): 3.78541,
        ("Litre", "Gallon"): 0.264172,
        ("Quart", "Litre"): 0.946353,
        ("Litre", "Quart"): 1.05669,
        ("Pint", "Litre"): 0.473176,
        ("Litre", "Pint"): 2.11338,
        ("Cup", "Millilitre"): 240,
        ("Millilitre", "Cup"): 0.00416667,
        ("Fluid Ounce", "Millilitre"): 29.5735,
        ("Millilitre", "Fluid Ounce"): 0.033814,
        ("Tablespoon", "Millilitre"): 14.7868,
        ("Millilitre", "Tablespoon"): 0.067628,
        ("Teaspoon", "Millilitre"): 4.92892,
        ("Millilitre", "Teaspoon"): 0.202884,

    }
    if from_unit == to_unit:
        return value

    if (from_unit, to_unit) in conversion_factors:
        return value * conversion_factors[(from_unit, to_unit)]

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

Category = input("Enter the category of units to convert (weight, temperature, volume, distance): ")
if Category not in ["weight", "temperature", "volume", "distance"]:
        print("Invalid category. Supported categories are: weight, temperature, volume, distance.")
        Category = input("Enter the category of units to convert (weight, temperature, volume, distance): ")



if Category == "weight":
    from_unit = input("Enter the unit to convert from (e.g., kg, g, lb, oz, mg, stone, ton, tonne): ")
    if from_unit not in ["kg", "g", "lb", "oz", "mg", "stone", "ton", "tonne", "kilogram", "gram", "pound", "ounce", "milligram"]:
        print("Invalid unit. Supported units are: kg, g, lb, oz, mg, stone, ton, tonne.")
        from_unit = input("Enter the unit to convert from (e.g., kg, g, lb, oz): ")

    value = float(input("Enter the value to convert: "))

    to_unit = input("Enter the unit to convert to (e.g., kg, g, lb, oz): ")
    if to_unit not in ["kg", "g", "lb", "oz", "mg", "stone", "ton", "tonne", "kilogram", "gram", "pound", "ounce", "milligram"]:
        print("Invalid unit. Supported units are: kg, g, lb, oz, mg, stone, ton, tonne.")
        to_unit = input("Enter the unit to convert to (e.g., kg, g, lb, oz): ")

    print(f"{value} {from_unit} is equal to {convert_weight_units(value, from_unit, to_unit)} {to_unit}")


if Category == "temperature":
    from_unit = input("Enter the unit to convert from (C, F, K): ")
    if from_unit not in ["C", "F", "K"]:
        print("Invalid unit. Supported units are: C, F, K.")
        from_unit = input("Enter the unit to convert from (C, F, K): ")

    value = float(input("Enter the value to convert: "))

    to_unit = input("Enter the unit to convert to (C, F, K): ")
    if to_unit not in ["C", "F", "K"]:
        print("Invalid unit. Supported units are: C, F, K.")
        to_unit = input("Enter the unit to convert to (C, F, K): ")

    print(f"{value} {from_unit} is equal to {convert_temperature_units(value, from_unit, to_unit)} {to_unit}")

if Category == "volume":
    from_unit = input("Enter the unit to convert from (e.g., L, mL, gal, qt, pt, cup, fl oz, tbsp, tsp): ")
    if from_unit not in ["L", "mL", "gal", "qt", "pt", "cup", "fl oz", "tbsp", "tsp", "Litre", "Millilitre", "Gallon", "Quart", "Pint", "Cup", "Fluid Ounce", "Tablespoon", "Teaspoon"]:
            print("Invalid unit. Supported units are: L, mL, gal, qt, pt, cup, fl oz, tbsp, tsp.")
            from_unit = input("Enter the unit to convert from (e.g., L, mL, gal, qt, pt, cup, fl oz, tbsp, tsp): ")

    value = float(input("Enter the value to convert: "))

    to_unit = input("Enter the unit to convert to (e.g., L, mL, gal, qt, pt, cup, fl oz, tbsp, tsp): ")
    if to_unit not in ["L", "mL", "gal", "qt", "pt", "cup", "fl oz", "tbsp", "tsp", "Litre", "Millilitre", "Gallon", "Quart", "Pint", "Cup", "Fluid Ounce", "Tablespoon", "Teaspoon"]:
            print("Invalid unit. Supported units are: L, mL, gal, qt, pt, cup, fl oz, tbsp, tsp.")
            to_unit = input("Enter the unit to convert to (e.g., L, mL, gal, qt, pt, cup, fl oz, tbsp, tsp): ")

    print(f"{value} {from_unit} is equal to {convert_volume_units(value, from_unit, to_unit)} {to_unit}")
        



if Category == "distance":
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