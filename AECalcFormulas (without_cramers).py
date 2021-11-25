import math


class BasicMath:
    @classmethod
    def add(cls):
        a = float(input('Enter Value: '))
        b = float(input('Enter Value: '))
        print(a, "+", b)
        return a + b

    @classmethod
    def subtract(cls):
        a = float(input('Enter Value: '))
        b = float(input('Enter Value: '))
        print(a, "-", b)
        return a - b

    @classmethod
    def multiply(cls):
        a = float(input('Enter Value: '))
        b = float(input('Enter Value: '))
        print(a, "*", b)
        return a * b

    @classmethod
    def divide(cls):
        a = float(input('Enter Value: '))
        b = float(input('Enter Value: '))
        print(a, "/", b)
        return a / b

    @classmethod
    def exponent(cls):
        a = float(input('Enter Value: '))
        x = float(input("Enter x Value: "))
        print(a, "^", x)
        return a**x

    @classmethod
    def root(cls):
        a = float(input('Enter Value: '))
        print("sqrt", a)
        return math.sqrt(a)

    @classmethod
    def logarithm(cls):
        a = float(input('Enter Argument Value: '))
        b = float(input('Enter Base Value: '))
        print("Log", b, a)
        return math.log(a, b)

    @classmethod
    def sin(cls):
        a = float(input('Enter Value: '))
        print("Sin", a)
        return math.sin(a)

    @classmethod
    def cos(cls):
        a = float(input('Enter Value: '))
        print("Cos", a)
        return math.cos(a)

    @classmethod
    def tan(cls):
        a = float(input('Enter Value: '))
        print("Tan", a)
        return math.tan(a)

    @classmethod
    def arc_sin(cls):
        a = float(input('Enter Value: '))
        print("ArcSin", a)
        return math.asin(a)

    @classmethod
    def arc_cos(cls):
        a = float(input('Enter Value: '))
        print("ArcCos", a)
        return math.acos(a)


class AdvancedMath:
    class Physics:
        @classmethod
        def speed(cls):
            a = float(input('Distance (m): '))
            b = float(input('Time (s): '))
            answer_s = float(a / b)
            limit_s = round(answer_s, 2)
            return limit_s

        @classmethod
        def velocity(cls):
            a = float(input('Displacement (m): '))
            b = float(input('Time (s): '))
            answer_v = float(a / b)
            limit_v = round(answer_v, 2)
            return limit_v

        @classmethod
        def acc(cls):
            a = float(input('Change in velocity (m/s): '))
            b = float(input('Time (s): '))
            answer = float(a / b)
            limit_a = round(answer, 2)
            return limit_a

        @classmethod
        def pressure(cls):
            a = float(input('Force (N): '))
            b = float(input('Area (m**2): '))
            answer_a = float(a / b)
            limit_a = round(answer_a, 2)
            return limit_a

        @classmethod
        def force(cls):
            a = float(input('Mass (kg): '))
            b = float(input('Area (m**2): '))
            answer_f = float(a * b)
            limit_f = round(answer_f, 2)
            return limit_f

        @classmethod
        def momen(cls):
            a = float(input('Mass (kg): '))
            b = float(input('Velocity (m/s): '))
            answer_m = float(a * b)
            limit_m = round(answer_m, 2)
            return limit_m

        @classmethod
        def power(cls):
            a = float(input('Work (Nm): '))
            b = float(input('Time (s): '))
            answer_p = float(a / b)
            limit_p = round(answer_p, 2)
            return limit_p

        @classmethod
        def volt(cls):
            a = float(input('Current (A): '))
            b = float(input('Resistance (ohm): '))
            answer_v = float(a * b)
            limit_v = round(answer_v, 2)
            return limit_v

        @classmethod
        def current(cls):
            a = float(input('Voltage (V): '))
            b = float(input('Resistance (ohm): '))
            answer_c = float(a / b)
            limit_c = round(answer_c, 2)
            return limit_c

        @classmethod
        def resistance(cls):
            a = float(input('Voltage (V): '))
            b = float(input('Current (A): '))
            answer_r = float(a / b)
            limit_r = round(answer_r, 2)
            return limit_r

        @classmethod
        def ke(cls):
            a = float(input('Mass (kg): '))
            b = float(input('Time (s): '))
            answer_ke = float(1 / 2 * a * b ** 2)
            limit_ke = round(answer_ke, 2)
            return limit_ke

        @classmethod
        def work(cls):
            a = float(input('Force (N): '))
            b = float(input('Distance (m): '))
            answer_w = float(a * b)
            limit_w = round(answer_w, 2)
            return limit_w

        @classmethod
        def coulombslaw(cls):
            k = 9000000000
            a = float(input('First charge (C): '))
            b = float(input('Second charge (C): '))
            c = float(input('Distance (m): '))
            answer_co = float(k * a * b) / (c ** 2)
            limit_co = round(answer_co, 2)
            return limit_co

        @classmethod
        def driftv(cls):
            a = float(input('Current (A): '))
            b = float(input('Number of electrons: '))
            c = float(input('Area (m^2): '))
            d = float(input('Charge (C): '))
            answer_dr = float(a / (b * c * d))
            limit_dr = round(answer_dr, 5)
            return limit_dr

    class Chemistry:
        @classmethod
        def density(cls):
            a = float(input('Mass (M): '))
            b = float(input('Volume (V): '))
            answer_d = float(a * b)
            limit_d = round(answer_d, 2)
            return limit_d

        @classmethod
        def boyle_p1(cls):
            a = float(input('V1: '))
            b = float(input('V2: '))
            c = float(input('P2: '))
            answer_p1 = ((c * b) / a)
            limit_p1 = round(answer_p1, 4)
            return limit_p1

        @classmethod
        def boyle_v1(cls):
            a = float(input('P1: '))
            b = float(input('P2: '))
            c = float(input('V2: '))
            answer_v1 = ((b * c) / a)
            limit_v1 = round(answer_v1, 4)
            return limit_v1

        @classmethod
        def boyle_p2(cls):
            a = float(input('V1: '))
            b = float(input('V2: '))
            c = float(input('P1: '))
            answer_p2 = (c * a) / b
            limit_p2 = round(answer_p2, 4)
            return limit_p2

        @classmethod
        def boyle_v2(cls):
            a = float(input('P1: '))
            b = float(input('P2: '))
            c = float(input('V1: '))
            answer_v2 = (a * c) / b
            limit_v2 = round(answer_v2, 4)
            return limit_v2

        @classmethod
        def combined_gas_law_v1(cls):
            a = float(input('P1: '))
            b = float(input('P2: '))
            c = float(input('V2: '))
            d = float(input('T1: '))
            e = float(input('T2: '))
            answer_v1 = ((d * b * c) / (a * e))
            limit_v1 = round(answer_v1, 4)
            return limit_v1

        @classmethod
        def combined_gas_law_v2(cls):
            a = float(input('P1: '))
            b = float(input('P2: '))
            c = float(input('V1: '))
            d = float(input('T1: '))
            e = float(input('T2: '))
            answer_v2 = ((a * c * e) / (d * b))
            limit_v2 = round(answer_v2, 4)
            return limit_v2

        @classmethod
        def combined_gas_law_p1(cls):
            a = float(input('V2: '))
            b = float(input('P2: '))
            c = float(input('V1: '))
            d = float(input('T1: '))
            e = float(input('T2: '))
            answer_p1 = ((d * b * a) / (c * e))
            limit_p1 = round(answer_p1, 4)
            return limit_p1

        @classmethod
        def combined_gas_law_p2(cls):
            a = float(input('P1: '))
            b = float(input('V1: '))
            c = float(input('T2: '))
            d = float(input('V2: '))
            e = float(input('T1: '))
            answer_p2 = ((a * b * c) / (d * e))
            limit_p2 = round(answer_p2, 4)
            return limit_p2

        @classmethod
        def combined_gas_law_t1(cls):
            a = float(input('P1: '))
            b = float(input('V1: '))
            c = float(input('T2: '))
            d = float(input('P2: '))
            e = float(input('V2: '))
            answer_t1 = ((a * b * c) / (d * e))
            limit_t1 = round(answer_t1, 4)
            return limit_t1

        @classmethod
        def combined_gas_law_t2(cls):
            a = float(input('P1: '))
            b = float(input('V1: '))
            c = float(input('T1: '))
            d = float(input('P2: '))
            e = float(input('V2: '))
            answer_t2 = ((d * e * c) / (a * b))
            limit_t2 = round(answer_t2, 4)
            return limit_t2



    class Geometry:
        @classmethod
        def square_area(cls):
            a = float(input('Side: '))
            answer_area = (a * a)
            limit_area = round(answer_area, 2)
            return limit_area

        @classmethod
        def square_perimeter(cls):
            a = float(input('Side: '))
            answer_perimeter = (4 * a)
            limit_perimeter = round(answer_perimeter, 2)
            return limit_perimeter

        @classmethod
        def rectangle_area(cls):
            a = float(input('Length: '))
            b = float(input('Width: '))
            answer_area = (a * b)
            limit_area = round(answer_area, 2)
            return limit_area

        @classmethod
        def rectangle_perimeter(cls):
            a = float(input('Length: '))
            b = float(input('Width: '))
            answer_perimeter = 2 * (a + b)
            limit_perimeter = round(answer_perimeter, 2)
            return limit_perimeter

        @classmethod
        def parallelogram_area(cls):
            a = float(input('Base: '))
            b = float(input('Height: '))
            answer_area = (a * b)
            limit_area = round(answer_area, 2)
            return limit_area

        @classmethod
        def parallelogram_perimeter(cls):
            a = float(input('Side: '))
            b = float(input('Base: '))
            answer_perimeter = 2 * ( a + b)
            limit_perimeter = round(answer_perimeter, 2)
            return limit_perimeter

        @classmethod
        def trapezoid_area(cls):
            a = float(input('Height: '))
            b = float(input('Base 1: '))
            c = float(input('Base 2: '))
            answer_area =  1/2 * a * (b + c)
            limit_area = round(answer_area, 2)
            return limit_area

        @classmethod
        def trapezoid_perimeter(cls):
            a = float(input('Side 1: '))
            b = float(input('Side 2: '))
            c = float(input('Base 1: '))
            d = float(input('Base 2: '))
            answer_perimeter = (a + b + c + d)
            limit_perimeter = round(answer_perimeter, 2)
            return limit_perimeter

        @classmethod
        def triangle_area(cls):
            a = float(input('Height: '))
            b = float(input('Base: '))
            answer_area = 1 / 2 * (a * b)
            limit_area = round(answer_area, 2)
            return limit_area

        @classmethod
        def triangle_perimeter(cls):
            a = float(input('Side 1: '))
            b = float(input('Side 2: '))
            c = float(input('Base: '))
            answer_perimeter = (a + b + c)
            limit_perimeter = round(answer_perimeter, 2)
            return limit_perimeter

        @classmethod
        def circle_area(cls):
            a = float(input('Radius: '))
            answer_area = 3.14 * a ** 2
            limit_area = round(answer_area, 2)
            return limit_area

        @classmethod
        def circle_circumference(cls):
            a = float(input('Radius: '))
            answer_circumference = 2 * 3.14 * a
            limit_circumference = round(answer_circumference, 2)
            return limit_circumference

        @classmethod
        def rectangular_prism_volume(cls):
            a = float(input('Length: '))
            b = float(input('Width: '))
            c = float(input('Height: '))
            answer_volume = (a * b * c)
            limit_volume = round(answer_volume, 2)
            return limit_volume

        @classmethod
        def rectangular_prism_surface(cls):
            a = float(input('Length: '))
            b = float(input('Width: '))
            c = float(input('Height: '))
            answer_sa = 2 * (b * c + c * a + b * c)
            limit_sa = round(answer_sa, 2)
            return limit_sa

        @classmethod
        def cube_volume(cls):
            a = float(input('Side: '))
            answer_volume = (a * a * a)
            limit_volume = round(answer_volume, 2)
            return limit_volume

        @classmethod
        def cube_sa(cls):
            a = float(input('Side: '))
            answer_sa = 6 * (a ** 2)
            limit_sa = round(answer_sa, 2)
            return limit_sa

        @classmethod
        def cylinder_volume(cls):
            a = float(input('Radius: '))
            b = float(input('Height: '))
            answer_volume = 3.14 * (a **2 * b)
            limit_volume = round(answer_volume, 2)
            return limit_volume

        @classmethod
        def cylinder_sa(cls):
            a = float(input('Radius: '))
            b = float(input('Height: '))
            answer_sa = 6.28 * (a * b) + 6.28 * (a ** 2)
            limit_sa = round(answer_sa, 2)
            return limit_sa

        @classmethod
        def sphere_volume(cls):
            a = float(input('Radius: '))
            answer_volume = 4/3 * (3.14 * (a * a * a))
            limit_volume = round(answer_volume, 2)
            return limit_volume

        @classmethod
        def sphere_sa(cls):
            a = float(input('Radius: '))
            answer_sa = 4 * (3.14 * (a ** 2))
            limit_sa = round(answer_sa, 2)
            return limit_sa

        @classmethod
        def cone_volume(cls):
            a = float(input('Radius: '))
            b = float(input('Height: '))
            answer_volume = 1/3 * 3.14 * (a ** 2 * b)
            limit_volume = round(answer_volume, 2)
            return limit_volume

        @classmethod
        def cone_sa(cls):
            a = float(input('Radius: '))
            b = float(input('Height: '))
            answer_sa = 3.14 * a * ( a + math.sqrt(a ** 2 + b ** 2))
            limit_sa = round(answer_sa, 2)
            return limit_sa

        @classmethod
        def pyramid_volume(cls):
            a = float(input('Length: '))
            b = float(input('Width: '))
            c = float(input('Height: '))
            answer_volume =  1/3 * (a * b * c)
            limit_volume = round(answer_volume, 2)
            return limit_volume


class Conversion:
    class Temperature:
        @classmethod
        def fahrenheit_to_celsius(cls):
            a = float(input('Fahrenheit (F): '))
            answer_cel = (a - 32) * 5 / 9
            limit_cel = round(answer_cel, 2)
            return limit_cel

        @classmethod
        def celsius_to_fahrenheit(cls):
            a = float(input('Celsius (C): '))
            answer_fah = (a * 9 / 5) + 32
            limit_fah = round(answer_fah, 2)
            return limit_fah

        @classmethod
        def celsius_to_kelvin(cls):
            a = float(input('Celsius (C): '))
            answer_kel = a + 273.15
            limit_kel = round(answer_kel, 2)
            return limit_kel

        @classmethod
        def kelvin_to_celsius(cls):
            a = float(input('Kelvin (K): '))
            answer_cel = (a - 273.15)
            limit_cel = round(answer_cel, 2)
            return limit_cel

    class Metric:
        ## LENGTH ##
        @classmethod
        def inch_to_centi(cls):
            a = float(input('Inch (in): '))
            answer_cm = (a * 2.54)
            limit_cm = round(answer_cm, 4)
            return limit_cm

        @classmethod
        def centimeter_in(cls):
            a = float(input('Centimeter (cm): '))
            answer_in = (a / 2.54)
            limit_in = round(answer_in, 4)
            return limit_in

        @classmethod
        def meters_to_km(cls):
            a = float(input('Meters (m): '))
            answer_km = (a / 1000)
            limit_km = round(answer_km, 4)
            return limit_km

        @classmethod
        def km_to_meters(cls):
            a = float(input('Kilometeres (km): '))
            answer_meters = (a * 1000)
            limit_meters = round(answer_meters, 4)
            return limit_meters

        @classmethod
        def km_to_miles(cls):
            a = float(input('Kilomteres (km): '))
            answer_mi = (a / 1.609)
            limit_mi = round(answer_mi ,4)
            return limit_mi

        @classmethod
        def miles_to_km(cls):
            a = float(input('Miles (mi): '))
            answer_km = (a * 1.609)
            limit_km = round(answer_km, 4)
            return limit_km

        @classmethod
        def yard_to_feet(cls):
            a = float(input('Yards (yd): '))
            answer_feet = (a * 3)
            limit_feet = round(answer_feet, 4)
            return limit_feet

        @classmethod
        def feet_to_yard(cls):
            a = float(input('Feet/Foot (ft): '))
            answer_yard = (a / 3)
            limit_yard = round(answer_yard, 2)
            return limit_yard

        ## VOLUME ##
        @classmethod
        def pint_to_cup(cls):
            a = float(input('pint (pt): '))
            answer_cup = (a * 2)
            limit_cup = round(answer_cup, 2)
            return limit_cup

        @classmethod
        def cup_to_pint(cls):
            a = float(input('Cup (cup): '))
            answer_pint = (a / 2)
            limit_pint = round(answer_pint, 2)
            return limit_pint

        @classmethod
        def quarts_to_pints(cls):
            a = float(input('Quarts (qt): '))
            answer_pint = (a * 2)
            limit_pint = round(answer_pint, 2)
            return limit_pint

        @classmethod
        def pint_to_quarts(cls):
            a = float(input('pint (pt): '))
            answer_quarts = (a / 2)
            limit_quarts = round(answer_quarts, 2)
            return limit_quarts

        @classmethod
        def gallons_to_quarts(cls):
            a = float(input('Gallons (gal): '))
            answer_quarts = (a * 4)
            limit_quarts = round(answer_quarts, 4)
            return limit_quarts

        @classmethod
        def quarts_to_gallons(cls):
            a = float(input('Quarts (qt): '))
            answer_gallons = (a / 4)
            limit_gallons = round(answer_gallons, 4)
            return limit_gallons

        ## WEIGHT ##
        @classmethod
        def gram_to_kg(cls):
            a = float(input('Grams (g): '))
            answer_kg = (a / 1000)
            limit_kg = round(answer_kg, 4)
            return limit_kg

        @classmethod
        def kg_to_grams(cls):
            a = float(input('Kilograms (kg): '))
            answer_g = (a *  1000)
            limit_g = round(answer_g, 4)
            return limit_g

        @classmethod
        def pounds_to_kg(cls):
            a = float(input('Pounds (lb): '))
            answer_kg = (a / 2.205)
            limit_kg = round(answer_kg, 4)
            return limit_kg

        @classmethod
        def kg_to_pounds(cls):
            a = float(input('Kilorams (kg): '))
            answer_lb = (a * 2.205)
            limit_lb = round(answer_lb, 4)
            return limit_lb

        @classmethod
        def kg_to_tons(cls):
            a = float(input('Kilograms (kg): '))
            answer_ton = (a / 907)
            limit_ton = round(answer_ton, 4)
            return limit_ton

        @classmethod
        def tons_to_kg(cls):
            a = float(input('Tons (ton): '))
            answer_kg = (a * 907)
            limit_kg = round(answer_kg, 4)
            return limit_kg


    class SI_units:
    ### POSTITVE ###
        @classmethod
        def deca_to_hecto(cls):
            a = float(input('deka (da): '))
            answer_hecto = (a ** 4)
            return answer_hecto

        @classmethod
        def hecto_to_kilo(cls):
            a = float(input('hecto (h): '))
            answer_kilo = (a ** 4)
            return answer_kilo

        @classmethod
        def kilo_to_mega(cls):
            a = float(input('kilo (k): '))
            answer_mega = (a ** 4)
            return answer_mega

        @classmethod
        def mega_to_giga(cls):
            a = float(input('mega (M): '))
            answer_giga = (a ** 4)
            return answer_giga

        @classmethod
        def giga_to_tera(cls):
            a = float(input('giga (G): '))
            answer_tera = (a ** 12)
            return answer_tera

        ### NEGATIVE ###
        @classmethod
        def deca_to_deci(cls):
            a = float(input('deca (da): '))
            answer_deci = (a ** -1)
            return answer_deci

        @classmethod
        def deci_to_centi(cls):
            a = float(input('deci (d): '))
            answer_centi = (a ** -2)
            return answer_centi

        @classmethod
        def centi_to_mili(cls):
            a = float(input('centi (c): '))
            answer_mili = (a ** -3)
            return answer_mili

        @classmethod
        def mili_to_micro(cls):
            a = float(input('mili (m): '))
            answer_micro = (a ** -6)
            return answer_micro

        @classmethod
        def micro_to_nano(cls):
            a = float(input('micro (µ): '))
            answer_nano = (a ** -9)
            return answer_nano

        @classmethod
        def nano_to_pico(cls):
            a = float(input('nano (n): '))
            answer_pico = (a ** -12)
            return answer_pico



###### CRAIMER'S RULE ###########











