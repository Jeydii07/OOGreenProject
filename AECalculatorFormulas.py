import math


class BasicMath:
    def __init__(self, a=0, b=0, c=0, d=0, e=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.k = 9000000000

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return round(self.a / self.b, 2)

    def exponent(self):
        return round(self.a**self.b, 2)

    def root(self):
        return round(math.sqrt(self.a), 2)

    def logarithm(self):
        return round(math.log(self.a, self.b), 2)

    def sin(self):
        return round(math.sin(self.a), 2)

    def cos(self):
        return round(math.cos(self.a), 2)

    def tan(self):
        return round(math.tan(self.a), 2)

    def arc_sin(self):
        return round(math.asin(self.a), 2)

    def arc_cos(self):
        return round(math.acos(self.a), 2)

    def arc_tan(self):
        return round(math.atan(self.a), 2)

    def hyp_sin(self):
        return round(math.sinh(self.a), 2)

    def hyp_cos(self):
        return round(math.cosh(self.a), 2)

    def hyp_tan(self):
        return round(math.tanh(self.a), 2)


class Physics(BasicMath):

    def speed(self):
        return round(self.a / self.b, 2)

    def velocity(self):
        return round(self.a / self.b, 2)

    def acceleration(self):
        return round(self.a / self.b, 2)

    def pressure(self):
        return round(self.a / self.b, 2)

    def force(self):
        return round(self.a * self.b, 2)

    def momentum(self):
        return round(self.a * self.b, 2)

    def power(self):
        return round(self.a / self.b, 2)

    def volt(self):
        return round(self.a * self.b, 2)

    def current(self):
        return round(self.a / self.b, 2)

    def resistance(self):
        return round(self.a / self.b, 2)

    def kinetic_energy(self):
        return round(1/2 * self.a * self.b ** 2)

    def work(self):
        return round(self.a * self.b, 2)

    def coulombs_law(self):
        return round((self.k * self.a * self.b) / (self.c ** 2), 2)

    def drift_velocity(self):
        return round(self.a / (self.b * self.c * self.d), 5)


class Chemistry(BasicMath):

    def density(self):
        return round(self.a * self.b, 2)

    def boyle_p1(self):
        return round((self.c * self.b) / self.a, 4)

    def boyle_v1(self):
        return round((self.b * self.c) / self.a, 4)

    def boyle_p2(self):
        return round((self.c * self.a) / self.b, 4)

    def boyle_v2(self):
        return round((self.a * self.c) / self.b, 4)

    def combined_gas_law_v1(self):
        return round((self.d * self.b * self.c) / (self.a / self.e), 4)

    def combined_gas_law_v2(self):
        return round((self.a * self.c * self.e) / (self.d / self.b), 4)

    def combined_gas_law_p1(self):
        return round((self.d * self.b * self.a) / (self.c / self.e), 4)

    def combined_gas_law_p2(self):
        return round((self.a * self.b * self.c) / (self.d / self.e), 4)

    def combined_gas_law_t1(self):
        return round((self.a * self.b * self.c) / (self.d / self.e), 4)

    def combined_gas_law_t2(self):
        return round((self.d * self.e * self.c) / (self.a / self.b), 4)


class Geometry(BasicMath):

    def square_area(self):
        return round(self.a * self.a, 2)

    def square_perimeter(self):
        return round(self.a * 4, 2)

    def rectangle_area(self):
        return round(self.a * self.b, 2)

    def rectangle_perimeter(self):
        return round(2 * (self.a + self.b), 2)

    def parallelogram_area(self):
        return round(self.a * self.b, 2)

    def parallelogram_perimeter(self):
        return round(2 * (self.a + self.b), 2)

    def trapezoid_area(self):
        return round(1 / 2 * self.a * (self.b + self.c), 2)

    def trapezoid_perimeter(self):
        return round(self.a + self.b + self.c + self.d, 2)

    def triangle_area(self):
        return round(1 / 2 * (self.a * self.b), 2)

    def triangle_perimeter(self):
        return round(self.a + self.b + self.c, 2)

    def circle_area(self):
        return round(math.pi * self.a ** 2, 2)

    def circle_circumference(self):
        return round(2 * math.pi * self.a, 2)

    def rectangular_prism_volume(self):
        return round(self.a * self.b * self.c, 2)

    def rectangular_prism_surface(self):
        return round(2 * (self.b * self.c + self.c * self.a + self.b * self.c), 2)

    def cube_volume(self):
        return round(self.a ** 3, 2)

    def cube_sa(self):
        return round(6 * (self.a ** 2), 2)

    def cylinder_volume(self):
        return round(math.pi * (self.a ** 2 * self.b), 2)

    def cylinder_sa(self):
        return round(2 * math.pi * (self.a * self.b) + 2 * math.pi * (self.a ** 2), 2)

    def sphere_volume(self):
        return round(4 / 3 * (math.pi * (self.a ** 3)), 2)

    def sphere_sa(self):
        return round(4 * (math.pi * (self.a ** 2)), 2)

    def cone_volume(self):
        return round(1 / 3 * math.pi * (self.a ** 2 * self.b), 2)

    def cone_sa(self):
        return round(math.pi * self.a * (self.a + math.sqrt(self.a ** 2 + self.b ** 2)), 2)

    def pyramid_volume(self):
        return round(1 / 3 * (self.a * self.b * self.c), 2)


class Conversion(BasicMath):
    # TEMPERATURE
    def fahrenheit_to_celsius(self):
        return round((self.a - 32) * 5/9, 2)

    def celsius_to_fahrenheit(self):
        return round((self.a * 9/5) + 32, 2)

    def celsius_to_kelvin(self):
        return round((self.a + 273.15), 2)

    def kelvin_to_celsisus(self):
        return round((self.a - 273.15), 2)

    # METRIC
    #  ---------------- LENGTH -----------------
    def inches_to_centimeter(self):
        return round((self.a * 2.54), 4)

    def centimeter_to_inches(self):
        return round((self.a / 2.54), 4)

    def meters_to_kilometers(self):
        return round((self.a / 1000), 4)

    def kilometers_to_meters(self):
        return round((self.a * 1000), 4)

    def kilometers_to_miles(self):
        return round((self.a / 1.609), 4)

    def miles_to_kilometers(self):
        return round((self.a * 1.609), 4)

    def yard_to_feet(self):
        return round((self.a * 3), 4)

    def feet_to_yard(self):
        return round((self.a / 3), 4)

    #  ---------------- VOLUME -----------------
    def pint_to_cup(self):
        return round((self.a * 2), 2)

    def cup_to_pint(self):
        return round((self.a / 2), 2)

    def quarts_to_pints(self):
        return round((self.a * 2), 2)

    def pints_to_quarts(self):
        return round((self.a / 2), 2)

    def gallons_to_quarts(self):
        return round((self.a * 4), 2)

    def quarts_to_gallons(self):
        return round((self.a / 4), 2)

    #  ---------------- WEIGHTS -----------------
    def gram_to_kilogram(self):
        return round((self.a * 1000), 4)

    def kilogram_to_grams(self):
        return round((self.a / 1000), 4)

    def pounds_to_kilograms(self):
        return round((self.a / 2.205), 4)

    def kilograms_to_pounds(self):
        return round((self.a * 2.205), 4)

    def kilograms_to_tons(self):
        return round((self.a / 907), 4)

    def tons_to_kilograms(self):
        return round((self.a * 907), 4)

    # SI UNITS
    # ----------- POSITIVE -----------
    def tera_to_giga(self):
        return round((self.a * 1000))

    def giga_to_mega(self):
        return round((self.a * 1000))

    def mega_to_kilo(self):
        return round((self.a * 1000))

    def kilo_to_hecto(self):
        return round((self.a * 1000))

    def hecto_to_deca(self):
        return round((self.a * 1000))

    # ----------- NEGATIVE -----------
    def deca_to_deci(self):
        return round((self.a * 100))

    def deci_to_centi(self):
        return round((self.a * 10))

    def centi_to_mili(self):
        return round((self.a * 10))

    def mili_to_micro(self):
        return round((self.a * 1000))

    def micro_to_nano(self):
        return round((self.a * 1000))

    def nano_to_pico(self):
        return round((self.a * 1000))
