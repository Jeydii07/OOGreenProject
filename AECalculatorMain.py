from AECalcFormulas import BasicMath
from AECalcFormulas import AdvancedMath
from AECalcFormulas import Conversion

TRED = '\033[31;1m'  # Red Bold Text
TGREEN = '\033[32m'  # Green Text
YELLOW = '\033[93m'  # Yellow Text
BLUE = '\033[94m'    # Blue Text
RESET = '\033[0m'    # White Reset

while True:
    try:
        # Choosing a Feature
        print(TGREEN + "        ╔═╗╔═╗  ╔═╗╔═╗╦  ╔═╗╦ ╦╦  ╔═╗╔╦╗╔═╗╦═╗")
        print("        ╠═╣║╣   ║  ╠═╣║  ║  ║ ║║  ╠═╣ ║ ║ ║╠╦╝")
        print("        ╩ ╩╚═╝  ╚═╝╩ ╩╩═╝╚═╝╚═╝╩═╝╩ ╩ ╩ ╚═╝╩╚═")
        print(BLUE + "Choose a Feature:", RESET +
              "\nInput 1 for Basic Math"
              "\nInput 2 for Advanced Math"
              "\nInput 3 for Conversions"
              "\nInput 4 to End the Program"
              )
        x = int(input(YELLOW+"Enter Feature: "))

        if x == 1:
            # Basic Math Formula List
            print(TGREEN + "           ╔╗ ╔═╗╔═╗╦╔═╗  ╔╦╗╔═╗╔╦╗╦ ╦")
            print("           ╠╩╗╠═╣╚═╗║║    ║║║╠═╣ ║ ╠═╣")
            print("           ╚═╝╩ ╩╚═╝╩╚═╝  ╩ ╩╩ ╩ ╩ ╩ ╩ ")
            print(BLUE + "Choose a Formula:", RESET +
                  "\nInput 1 for Addition"
                  "\nInput 2 for Subtraction"
                  "\nInput 3 for Multiplication"
                  "\nInput 4 for Division"
                  "\nInput 5 for Exponent"
                  "\nInput 6 for Roots"
                  "\nInput 7 for Logarithm"
                  "\nInput 8 for Sin Function"
                  )

            y = int(input(YELLOW + "Enter Feature: "))
            if y == 1:
                add = BasicMath.add()
                print(BLUE + "--------------The answer is:", add, "--------------")
            elif y == 2:
                sub = BasicMath.subtract()
                print(BLUE + "--------------The answer is: ", sub, "--------------")
            elif y == 3:
                mul = BasicMath.multiply()
                print(BLUE + "--------------The answer is: ", mul, "--------------")
            elif y == 4:
                div = BasicMath.divide()
                print(BLUE + "--------------The answer is: ", div, "--------------")
            elif y == 5:
                exp = BasicMath.exponent()
                print(BLUE + "--------------The answer is: ", exp, "--------------")
            elif y == 6:
                roo = BasicMath.root()
                print(BLUE + "--------------The answer is: ", roo, "--------------")
            elif y == 7:
                log = BasicMath.logarithm()
                print(BLUE + "--------------The answer is: ", log, "--------------")
            elif y == 8:
                sin = BasicMath.sin()
                print(BLUE + "--------------The answer is: ", sin, "--------------")
            elif y == 9:
                cos = BasicMath.cos()
                print(BLUE + "--------------The answer is: ", cos, "--------------")
            elif y == 10:
                tan = BasicMath.tan()
                print(BLUE + "--------------The answer is: ", tan, "--------------")
            elif y == 11:
                asi = BasicMath.arc_sin()
                print(BLUE + "--------------The answer is: ", asi, "--------------")
            elif y < 1 or y > 11:
                raise ValueError(TRED + "--------------Please enter a valid Command""--------------")
        elif x == 2:
            # Advanced Math Formula List
            print(TGREEN + "       ╔═╗╔╦╗╦  ╦╔═╗╔╗╔╔═╗╔═╗╔╦╗  ╔╦╗╔═╗╔╦╗╦ ╦")
            print("       ╠═╣ ║║╚╗╔╝╠═╣║║║║  ║╣  ║║  ║║║╠═╣ ║ ╠═╣")
            print("       ╩ ╩═╩╝ ╚╝ ╩ ╩╝╚╝╚═╝╚═╝═╩╝  ╩ ╩╩ ╩ ╩ ╩ ╩")
            print(BLUE + "Choose a Formula:", RESET +
                  "\nInput 1 for Physics"
                  "\nInput 2 for Chemistry"
                  "\nInput 3 for Geometry")
            y = int(input(YELLOW + "Enter Feature: "))

            if y == 1:
                # Physics Formula List
                print(TGREEN + "             ╔═╗╦ ╦╦ ╦╔═╗╦╔═╗╔═╗")
                print("             ╠═╝╠═╣╚╦╝╚═╗║║  ╚═╗")
                print("             ╩  ╩ ╩ ╩ ╚═╝╩╚═╝╚═╝")
                print(BLUE + "Choose a Formula:", RESET +
                      "\nInput 1 for Speed"
                      "\nInput 2 for Velocity"
                      "\nInput 3 for Acceleration"
                      "\nInput 4 for Pressure"
                      "\nInput 5 for Force"
                      "\nInput 6 for Momentum"
                      "\nInput 7 for Power"
                      "\nInput 8 for Voltage"
                      "\nInput 9 for Current"
                      "\nInput 10 for Resistance"
                      "\nInput 11 for Kinetic Energy"
                      "\nInput 12 for Work"
                      "\nInput 13 for Coulomb's Law"
                      "\nInput 14 for Drift Velocity"
                      )
                z = int(input(YELLOW + "Enter Feature: "))

                if z == 1:
                    spd = AdvancedMath.Physics.speed()
                    print(BLUE + "--------------The speed is: ", spd, "--------------")
                elif z == 2:
                    vel = AdvancedMath.Physics.velocity()
                    print(BLUE + "--------------The velocity is: ", vel, "--------------")
                elif z == 3:
                    acc = AdvancedMath.Physics.acc()
                    print(BLUE + "--------------The acceleration is: ", acc, "--------------")
                elif z == 4:
                    pre = AdvancedMath.Physics.pressure()
                    print(BLUE + "--------------The pressure is: ", pre, "--------------")
                elif z == 5:
                    forc = AdvancedMath.Physics.force()
                    print(BLUE + "--------------The force is: ", forc, "--------------")
                elif z == 6:
                    mom = AdvancedMath.Physics.momen()
                    print(BLUE + "--------------The momentum is: ", mom, "--------------")
                elif z == 7:
                    pow = AdvancedMath.Physics.power()
                    print(BLUE + "--------------The power is: ", pow, "--------------")
                elif z == 8:
                    vol = AdvancedMath.Physics.volt()
                    print(BLUE + "--------------The voltage is: ", vol, "--------------")
                elif z == 9:
                    cur = AdvancedMath.Physics.current()
                    print(BLUE + "--------------The current is: ", cur, "--------------")
                elif z == 10:
                    res = AdvancedMath.Physics.resistance()
                    print(BLUE + "--------------The resistance is: ", res, "--------------")
                elif z == 11:
                    ke = AdvancedMath.Physics.ke()
                    print(BLUE + "--------------The kinetic energy is: ", ke, "--------------")
                elif z == 12:
                    wor = AdvancedMath.Physics.work()
                    print(BLUE + "--------------The work is: ", wor, "--------------")
                elif z == 13:
                    col = AdvancedMath.Physics.coulombslaw()
                    print(BLUE + "--------------The electric force is: ", col, "--------------")
                elif z == 14:
                    drv = AdvancedMath.Physics.driftv()
                    print(BLUE + "--------------The drift velocity is: ", drv, "--------------")
                elif z < 1 or z > 14:
                    raise ValueError(TRED + "--------------Please enter a valid Command""--------------")
            elif y == 2:
                # Chemistry Formula List
                print(TGREEN + "           ╔═╗╦ ╦╔═╗╔╦╗╦╔═╗╔╦╗╦═╗╦ ╦")
                print("           ║  ╠═╣║╣ ║║║║╚═╗ ║ ╠╦╝╚╦╝")
                print("           ╚═╝╩ ╩╚═╝╩ ╩╩╚═╝ ╩ ╩╚═ ╩ ")
                print(BLUE + "Choose a Formula:", RESET +
                      "\nInput 1 for Density"
                      "\nInput 2 for Boyle's Law(P1)"
                      "\nInput 3 for Boyle's Law(P2)"
                      "\nInput 4 for Boyle's Law(V1)"
                      "\nInput 5 for Boyle's Law(V2)"
                      "\nInput 6 for Combined Gas Law(P1)"
                      "\nInput 7 for Combined Gas Law(P2)"
                      "\nInput 8 for Combined Gas Law(V1)"
                      "\nInput 9 for Combined Gas Law(V2)"
                      "\nInput 10 for Combined Gas Law(T1)"
                      "\nInput 11 for Combined Gas Law(T2)"
                      )
                z = int(input(YELLOW + "Enter Feature: "))
                if z == 1:
                    den = AdvancedMath.Chemistry.density()
                    print(BLUE + "--------------The density is: ", den, "--------------")
                elif z == 2:
                    bp1 = AdvancedMath.Chemistry.boyle_p1()
                    print(BLUE + "--------------The P1 value is: ", bp1, "--------------")
                elif z == 3:
                    bp2 = AdvancedMath.Chemistry.boyle_p2()
                    print(BLUE + "--------------The P2 value is: ", bp2, "--------------")
                elif z == 4:
                    bv1 = AdvancedMath.Chemistry.boyle_v1()
                    print(BLUE + "--------------The V1 value is: ", bv1, "--------------")
                elif z == 5:
                    bv2 = AdvancedMath.Chemistry.boyle_v2()
                    print(BLUE + "--------------The V2 value is: ", bv2, "--------------")
                elif z == 6:
                    cp1 = AdvancedMath.Chemistry.combined_gas_law_p1()
                    print(BLUE + "--------------The P1 value is: ", cp1, "--------------")
                elif z == 7:
                    cp2 = AdvancedMath.Chemistry.combined_gas_law_p2()
                    print(BLUE + "--------------The P2 value is: ", cp2, "--------------")
                elif z == 8:
                    cv1 = AdvancedMath.Chemistry.combined_gas_law_v1()
                    print(BLUE + "--------------The V1 value is: ", cv1, "--------------")
                elif z == 9:
                    cv2 = AdvancedMath.Chemistry.combined_gas_law_v2()
                    print(BLUE + "--------------The V2 value is: ", cv2, "--------------")
                elif z == 10:
                    ct1 = AdvancedMath.Chemistry.combined_gas_law_t1()
                    print(BLUE + "--------------The T1 value is: ", ct1, "--------------")
                elif z == 11:
                    ct2 = AdvancedMath.Chemistry.combined_gas_law_t2()
                    print(BLUE + "--------------The T2 value is: ", ct2, "--------------")
                elif z < 1 or z > 11:
                    raise ValueError(TRED + "--------------Please enter a valid Command""--------------")
            elif y == 3:
                # Geometry Formula List
                print(TGREEN + "           ╔═╗╔═╗╔═╗╔╦╗╔═╗╔╦╗╦═╗╦ ╦")
                print("           ║ ╦║╣ ║ ║║║║║╣  ║ ╠╦╝╚╦╝")
                print("           ╚═╝╚═╝╚═╝╩ ╩╚═╝ ╩ ╩╚═ ╩ ")
                print(BLUE + "Choose a Formula:", RESET +
                      BLUE + "\nAREA: ", RESET +
                      "\nInput 1 for Square"
                      "\nInput 2 for Rectangle"
                      "\nInput 3 for Triangle"
                      "\nInput 4 for Circle"
                      "\nInput 5 for Parallelogram"
                      "\nInput 6 for Trapezoid",
                      BLUE + "\nPERIMETER: ", RESET +
                      "\nInput 7 for Square"
                      "\nInput 8 for Rectangle"
                      "\nInput 9 for Triangle"
                      "\nInput 10 for Parallelogram"
                      "\nInput 11 for Trapezoid",
                      BLUE + "\nCIRCUMFERENCE: ", RESET +
                      "\nInput 12 for Circle",
                      BLUE + "\nSURFACE AREA: ", RESET +
                      "\nInput 13 for Rectangular Prism"
                      "\nInput 14 for Cube"
                      "\nInput 15 for Cylinder"
                      "\nInput 16 for Sphere"
                      "\nInput 17 for Cone",
                      BLUE + "\nVOLUME: ", RESET +
                      "\nInput 18 for Rectangular Prism"
                      "\nInput 19 for Cube"
                      "\nInput 20 for Cylinder"
                      "\nInput 21 for Sphere"
                      "\nInput 22 for Cone"
                      "\nInput 23 for Pyramid"
                      )

                z = int(input(YELLOW + "Enter Feature: "))
                if z == 1:
                    sqa = AdvancedMath.Geometry.square_area()
                    print(BLUE + "--------------The area is: ", sqa, "--------------")
                elif z == 2:
                    rea = AdvancedMath.Geometry.rectangle_area()
                    print(BLUE + "--------------The area is: ", rea, "--------------")
                elif z == 3:
                    tra = AdvancedMath.Geometry.triangle_area()
                    print(BLUE + "--------------The area is: ", tra, "--------------")
                elif z == 4:
                    cia = AdvancedMath.Geometry.circle_area()
                    print(BLUE + "--------------The area is: ", cia, "--------------")
                elif z == 5:
                    paa = AdvancedMath.Geometry.parallelogram_area()
                    print(BLUE + "--------------The area is: ", paa, "--------------")
                elif z == 6:
                    tra = AdvancedMath.Geometry.trapezoid_area()
                    print(BLUE + "--------------The area is: ", tra, "--------------")
                elif z == 7:
                    sqp = AdvancedMath.Geometry.square_perimeter()
                    print(BLUE + "--------------The perimeter is: ", sqp, "--------------")
                elif z == 8:
                    rep = AdvancedMath.Geometry.rectangle_perimeter()
                    print(BLUE + "--------------The perimeter is: ", rep, "--------------")
                elif z == 9:
                    trp = AdvancedMath.Geometry.triangle_perimeter()
                    print(BLUE + "--------------The perimeter is: ", trp, "--------------")
                elif z == 10:
                    pap = AdvancedMath.Geometry.parallelogram_perimeter()
                    print(BLUE + "--------------The perimeter is: ", pap, "--------------")
                elif z == 11:
                    trp = AdvancedMath.Geometry.trapezoid_perimeter()
                    print(BLUE + "--------------The perimeter is: ", trp, "--------------")
                elif z == 12:
                    cic = AdvancedMath.Geometry.circle_circumference()
                    print(BLUE + "--------------The circumference is: ", cic, "--------------")
                elif z == 13:
                    rpa = AdvancedMath.Geometry.rectangular_prism_surface()
                    print(BLUE + "--------------The surface area is: ", rpa, "--------------")
                elif z == 14:
                    cua = AdvancedMath.Geometry.cube_sa()
                    print(BLUE + "--------------The surface area is: ", cua, "--------------")
                elif z == 15:
                    cya = AdvancedMath.Geometry.cylinder_sa()
                    print(BLUE + "--------------The surface area is: ", cya, "--------------")
                elif z == 16:
                    spa = AdvancedMath.Geometry.sphere_sa()
                    print(BLUE + "--------------The surface area is: ", spa, "--------------")
                elif z == 17:
                    coa = AdvancedMath.Geometry.cone_sa()
                    print(BLUE + "--------------The surface area is: ", coa, "--------------")
                elif z == 18:
                    rpv = AdvancedMath.Geometry.rectangular_prism_volume()
                    print(BLUE + "--------------The volume is: ", rpv, "--------------")
                elif z == 19:
                    cuv = AdvancedMath.Geometry.cube_volume()
                    print(BLUE + "--------------The volume is: ", cuv, "--------------")
                elif z == 20:
                    cyv = AdvancedMath.Geometry.cylinder_volume()
                    print(BLUE + "--------------The volume is: ", cyv, "--------------")
                elif z == 21:
                    spv = AdvancedMath.Geometry.sphere_volume()
                    print(BLUE + "--------------The volume is: ", spv, "--------------")
                elif z == 22:
                    cov = AdvancedMath.Geometry.cone_volume()
                    print(BLUE + "--------------The volume is: ", cov, "--------------")
                elif z == 23:
                    pyv = AdvancedMath.Geometry.pyramid_volume()
                    print(BLUE + "--------------The volume is: ", pyv, "--------------")
                elif z < 1 or z > 23:
                    raise ValueError(TRED + "--------------Please enter a valid Command""--------------")
            elif y < 1 or y > 3:
                raise ValueError(TRED + "--------------Please enter a valid Command""--------------")
        elif x == 3:
            # Conversions Formula List
            print(TGREEN + "         ╔═╗╔═╗╔╗╔╦  ╦╔═╗╦═╗╔═╗╦╔═╗╔╗╔╔═╗")
            print("         ║  ║ ║║║║╚╗╔╝║╣ ╠╦╝╚═╗║║ ║║║║╚═╗")
            print("         ╚═╝╚═╝╝╚╝ ╚╝ ╚═╝╩╚═╚═╝╩╚═╝╝╚╝╚═╝")
            print(BLUE + "Choose a Formula:", RESET +
                  "\nInput 1 for Temperature"
                  "\nInput 2 for Metric"
                  "\nInput 3 for SI Units"
                  )
            y = int(input(YELLOW + "Enter Feature: "))

            if y == 1:
                # Temperature Formula List
                print(TGREEN + "         ╔╦╗╔═╗╔╦╗╔═╗╔═╗╦═╗╔═╗╔╦╗╦ ╦╦═╗╔═╗")
                print("          ║ ║╣ ║║║╠═╝║╣ ╠╦╝╠═╣ ║ ║ ║╠╦╝║╣ ")
                print("          ╩ ╚═╝╩ ╩╩  ╚═╝╩╚═╩ ╩ ╩ ╚═╝╩╚═╚═╝")
                print(BLUE + "Choose a Formula:", RESET +
                      "\nInput 1 for Fahrenheit to Celsius"
                      "\nInput 2 for Celsius to Fahrenheit"
                      "\nInput 3 for Celsius to Kelvin"
                      "\nInput 4 for Kelvin to Celsius"
                      )
                z = int(input(YELLOW + "Enter Feature: "))
                if z == 1:
                    ftc = Conversion.Temperature.fahrenheit_to_celsius()
                    print(BLUE + "--------------The temperature is: ", ftc, "--------------")
                elif z == 2:
                    ctf = Conversion.Temperature.celsius_to_fahrenheit()
                    print(BLUE + "--------------The temperature is: ", ctf, "--------------")
                elif z == 3:
                    ctk = Conversion.Temperature.celsius_to_kelvin()
                    print(BLUE + "--------------The temperature is: ", ctk, "--------------")
                elif z == 4:
                    ktc = Conversion.Temperature.kelvin_to_celsius()
                    print(BLUE + "--------------The temperature is: ", ktc, "--------------")
                elif z < 1 or z > 4:
                    raise ValueError(TRED + "--------------Please enter a valid Command""--------------")
            elif y == 2:
                # Metric Formula List
                print(TGREEN + "        ╔╦╗╔═╗╔╦╗╦═╗╦╔═╗  ╦ ╦╔╗╔╦╔╦╗╔═╗")
                print("        ║║║║╣  ║ ╠╦╝║║    ║ ║║║║║ ║ ╚═╗")
                print("        ╩ ╩╚═╝ ╩ ╩╚═╩╚═╝  ╚═╝╝╚╝╩ ╩ ╚═╝")
                print(BLUE + "Choose a Formula:", RESET +
                      "\nInput 1 for Length"
                      "\nInput 2 for Volume"
                      "\nInput 3 for Weight"
                      )
                z = int(input(YELLOW + "Enter Feature: "))

                if z == 1:
                    print(TGREEN + "    ╔╦╗╔═╗╔╦╗╦═╗╦╔═╗  ╦  ╔═╗╔╗╔╔═╗╔╦╗╦ ╦")
                    print("    ║║║║╣  ║ ╠╦╝║║    ║  ║╣ ║║║║ ╦ ║ ╠═╣")
                    print("    ╩ ╩╚═╝ ╩ ╩╚═╩╚═╝  ╩═╝╚═╝╝╚╝╚═╝ ╩ ╩ ╩")
                    print(BLUE + "Choose a Formula:", RESET +
                          "\nInput 1 for Inch to Centimeters"
                          "\nInput 2 for Centimeter to Inch"
                          "\nInput 3 for Meters to Kilometers"
                          "\nInput 4 for Kilometers to Meters"
                          "\nInput 5 for Kilometers to Miles"
                          "\nInput 6 for Miles to Kilometers"
                          "\nInput 7 for Yard to Feet"
                          "\nInput 8 for Feet to Yard"
                          )
                    w = int(input(YELLOW + "Enter Feature: "))
                    if w == 1:
                        itc = Conversion.Metric.inch_to_centi()
                        print(BLUE + "--------------The measurement is: ", itc, "--------------")
                    elif w == 2:
                        cti = Conversion.Metric.centimeter_in()
                        print(BLUE + "--------------The measurement is: ", cti, "--------------")
                    elif w == 3:
                        mtk = Conversion.Metric.meters_to_km()
                        print(BLUE + "--------------The measurement is: ", mtk, "--------------")
                    elif w == 4:
                        ktm = Conversion.Metric.km_to_meters()
                        print(BLUE + "--------------The measurement is: ", ktm, "--------------")
                    elif w == 5:
                        kmi = Conversion.Metric.km_to_miles()
                        print(BLUE + "--------------The measurement is: ", kmi, "--------------")
                    elif w == 6:
                        mik = Conversion.Metric.miles_to_km()
                        print(BLUE + "--------------The measurement is: ", mik, "--------------")
                    elif w == 7:
                        ytf = Conversion.Metric.yard_to_feet()
                        print(BLUE + "--------------The measurement is: ", ytf, "--------------")
                    elif w == 8:
                        fty = Conversion.Metric.feet_to_yard()
                        print(BLUE + "--------------The measurement is: ", fty, "--------------")
                    elif w < 1 or w > 6:
                        raise ValueError(TRED + "--------------Please enter a valid Command""--------------")

                elif z == 2:
                    print(TGREEN + "   ╔╦╗╔═╗╔╦╗╦═╗╦╔═╗  ╦  ╦╔═╗╦  ╦ ╦╔╦╗╔═╗")
                    print("   ║║║║╣  ║ ╠╦╝║║    ╚╗╔╝║ ║║  ║ ║║║║║╣ ")
                    print("   ╩ ╩╚═╝ ╩ ╩╚═╩╚═╝   ╚╝ ╚═╝╩═╝╚═╝╩ ╩╚═╝")
                    print(BLUE + "Choose a Formula:", RESET +
                          "\nInput 1 for Quarts to Pints"
                          "\nInput 2 for Pints to Quarts"
                          "\nInput 3 for Gallon to Quarts"
                          "\nInput 4 for Quarts to Gallon"
                          "\nInput 5 for Pint to Cup"
                          "\nInput 6 for Cup to Pint"
                          )
                    w = int(input(YELLOW + "Enter Feature: "))
                    if w == 1:
                        qtp = Conversion.Metric.quarts_to_pints()
                        print(BLUE + "--------------The measurement is: ", qtp, "--------------")
                    elif w == 2:
                        ptq = Conversion.Metric.pint_to_quarts()
                        print(BLUE + "--------------The measurement is: ", ptq, "--------------")
                    elif w == 3:
                        gtq = Conversion.Metric.gallons_to_quarts()
                        print(BLUE + "--------------The measurement is: ", gtq, "--------------")
                    elif w == 4:
                        qtg = Conversion.Metric.quarts_to_gallons()
                        print(BLUE + "--------------The measurement is: ", qtg, "--------------")
                    elif w == 5:
                        ptc = Conversion.Metric.pint_to_cup()
                        print(BLUE + "--------------The measurement is: ", ptc, "--------------")
                    elif w == 6:
                        ctp = Conversion.Metric.cup_to_pint()
                        print(BLUE + "--------------The measurement is: ", ctp, "--------------")
                    elif w < 1 or w > 6:
                        raise ValueError(TRED + "--------------Please enter a valid Command""--------------")

                elif z == 3:
                    print(TGREEN + "   ╔╦╗╔═╗╔╦╗╦═╗╦╔═╗  ╦ ╦╔═╗╦╔═╗╦ ╦╔╦╗╔═╗")
                    print("   ║║║║╣  ║ ╠╦╝║║    ║║║║╣ ║║ ╦╠═╣ ║ ╚═╗")
                    print("   ╩ ╩╚═╝ ╩ ╩╚═╩╚═╝  ╚╩╝╚═╝╩╚═╝╩ ╩ ╩ ╚═╝")
                    print(BLUE + "Choose a Formula:", RESET +
                          "\nInput 1 for Gram to Kilogram"
                          "\nInput 2 for Kilogram to Gram"
                          "\nInput 3 for Pounds to Kilogram"
                          "\nInput 4 for Kilogram to Pounds"
                          "\nInput 5 for Kilogram to Tons"
                          "\nInput 6 for Tons to Kilograms"
                          )
                    w = int(input(YELLOW + "Enter Feature: "))
                    if w == 1:
                        gtk = Conversion.Metric.gram_to_kg()
                        print(BLUE + "--------------The measurement is: ", gtk, "--------------")
                    elif w == 2:
                        ktg = Conversion.Metric.kg_to_grams()
                        print(BLUE + "--------------The measurement is: ", ktg, "--------------")
                    elif w == 3:
                        ptk = Conversion.Metric.pounds_to_kg()
                        print(BLUE + "--------------The measurement is: ", ptk, "--------------")
                    elif w == 4:
                        ktp = Conversion.Metric.kg_to_pounds()
                        print(BLUE + "--------------The measurement is: ", ktp, "--------------")
                    elif w == 5:
                        ktt = Conversion.Metric.kg_to_tons()
                        print(BLUE + "--------------The measurement is: ", ktt, "--------------")
                    elif w == 6:
                        ttk = Conversion.Metric.tons_to_kg()
                        print(BLUE + "--------------The measurement is: ", ttk, "--------------")
                    elif w < 1 or w > 6:
                        raise ValueError(TRED + "--------------Please enter a valid Command""--------------")
                elif z < 1 or z > 3:
                    raise ValueError(TRED + "--------------Please enter a valid Command""--------------")
            elif y == 3:
                # SI Units Formula List
                print(TGREEN + "             ╔═╗╦  ╦ ╦╔╗╔╦╔╦╗╔═╗")
                print("             ╚═╗║  ║ ║║║║║ ║ ╚═╗")
                print("             ╚═╝╩  ╚═╝╝╚╝╩ ╩ ╚═╝")
                print(BLUE + "Choose a Feature:", RESET +
                      "\nInput 1 for Positive Units"
                      "\nInput 2 for Negative Units"
                      )
                z = int(input(YELLOW + "Enter Feature: "))
                if z == 1:
                    print(TGREEN + "     ╔═╗╔═╗╔═╗╦╔╦╗╦╦  ╦╔═╗  ╦ ╦╔╗╔╦╔╦╗╔═╗")
                    print("     ╠═╝║ ║╚═╗║ ║ ║╚╗╔╝║╣   ║ ║║║║║ ║ ╚═╗")
                    print("     ╩  ╚═╝╚═╝╩ ╩ ╩ ╚╝ ╚═╝  ╚═╝╝╚╝╩ ╩ ╚═╝")
                    print(BLUE + "Choose a Formula:", RESET +
                          "\nInput 1 for Deca to Hecto"
                          "\nInput 2 for Hecto to Kilo"
                          "\nInput 3 for Kilo to Mega"
                          "\nInput 4 for Mega to Giga"
                          "\nInput 5 for Giga to Tera"
                          )
                    w = int(input(YELLOW + "Enter Feature: "))
                    if w == 1:
                        dth = Conversion.SI_units.deca_to_hecto()
                        print(BLUE + "--------------The measurement is: ", dth, "--------------")
                    elif w == 2:
                        htk = Conversion.SI_units.hecto_to_kilo()
                        print(BLUE + "--------------The measurement is: ", htk, "--------------")
                    elif w == 3:
                        ktm = Conversion.SI_units.kilo_to_mega()
                        print(BLUE + "--------------The measurement is: ", ktm, "--------------")
                    elif w == 4:
                        mtg = Conversion.SI_units.mega_to_giga()
                        print(BLUE + "--------------The measurement is: ", mtg, "--------------")
                    elif w == 5:
                        gtt = Conversion.SI_units.giga_to_tera()
                        print(BLUE + "--------------The measurement is: ", gtt, "--------------")
                    elif w < 1 or w > 5:
                        raise ValueError(TRED + "--------------Please enter a valid Command""--------------")
                elif z == 2:
                    print(TGREEN + "╔╗╔╔═╗╔═╗╔═╗╔╦╗╦╦  ╦╔═╗  ╦ ╦╔╗╔╦╔╦╗╔═╗")
                    print("║║║║╣ ║ ╦╠═╣ ║ ║╚╗╔╝║╣   ║ ║║║║║ ║ ╚═╗")
                    print("╝╚╝╚═╝╚═╝╩ ╩ ╩ ╩ ╚╝ ╚═╝  ╚═╝╝╚╝╩ ╩ ╚═╝")
                    print(BLUE + "Choose a Formula:", RESET +
                          "\nInput 1 for Deca to Deci"
                          "\nInput 2 for Deci to Centi"
                          "\nInput 3 for Centi to Mili"
                          "\nInput 4 for Mili to Micro"
                          "\nInput 5 for Micro to Nano"
                          "\nInput 6 for Nano to Pico"
                          )
                    w = int(input(YELLOW + "Enter Feature: "))
                    if w == 1:
                        dtd = Conversion.SI_units.deca_to_deci()
                        print(BLUE + "--------------The measurement is: ", dtd, "--------------")
                    elif w == 2:
                        dtc = Conversion.SI_units.deci_to_centi()
                        print(BLUE + "--------------The measurement is: ", dtc, "--------------")
                    elif w == 3:
                        ctm = Conversion.SI_units.centi_to_mili()
                        print(BLUE + "--------------The measurement is: ", ctm, "--------------")
                    elif w == 4:
                        mtm = Conversion.SI_units.mili_to_micro()
                        print(BLUE + "--------------The measurement is: ", mtm, "--------------")
                    elif w == 5:
                        mtn = Conversion.SI_units.micro_to_nano()
                        print(BLUE + "--------------The measurement is: ", mtn, "--------------")
                    elif w == 6:
                        ntp = Conversion.SI_units.nano_to_pico()
                        print(BLUE + "--------------The measurement is: ", ntp, "--------------")
                    elif w < 1 or w > 5:
                        raise ValueError(TRED + "--------------Please enter a valid Command""--------------")
                elif z < 1 or z > 2:
                    raise ValueError(TRED + "--------------Please enter a valid Command""--------------")
            elif y < 1 or y > 3:
                raise ValueError(TRED + "--------------Please enter a valid Command""--------------")
        elif x == 4:
            print(BLUE + "--------------Thank you for using AECalculator""--------------")
            print(RESET + "If there are any problems or insights regarding the program."
                  "\nYou may contact us through the following Emails:"
                  "\njdnepomuceno@donbosco.edu.ph"
                  "\npdcponciano@donbosco.edu.ph")
            break
        elif x < 1 or x > 4:
            raise ValueError(TRED + "--------------Please enter a valid Command""--------------")
    except ZeroDivisionError:
        print(TRED + "--------------Please enter another value that is not Zero""--------------")
    except ValueError:
        print(TRED + "--------------Please enter a valid Command""--------------")
