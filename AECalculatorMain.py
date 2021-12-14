import AECalculatorFormulas

# For Text Coloring
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
        # User inputs a feature from the list
        x = int(input(YELLOW + "Enter Feature: "))
        # If statements will be executed depending on the feature chosen by the user
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
                  "\nInput 9 for Cos Function"
                  "\nInput 10 for Tan Function"
                  "\nInput 11 for Arc Sin Function"
                  "\nInput 12 for Arc Cos Function"
                  "\nInput 13 for Arc Tan Function"
                  "\nInput 14 for Hyperbolic Sin Function"
                  "\nInput 15 for Hyperbolic Cos Function"
                  "\nInput 16 for Hyperbolic Tan Function"
                  )
            # User chooses a formula from the list
            y = float(input("Enter Feature: "))
            # If statements will be executed depending on the chosen formula by the user
            if y == 1:
                calc = AECalculatorFormulas.BasicMath(float(input("Enter Value: ")), float(input("Enter Value: ")))
                print(BLUE + "--------------The answer is:", calc.add(), "--------------")
            elif y == 2:
                calc = AECalculatorFormulas.BasicMath(float(input("Enter Value: ")), float(input("Enter Value: ")))
                print(BLUE + "--------------The answer is:", calc.subtract(), "--------------")
            elif y == 3:
                calc = AECalculatorFormulas.BasicMath(float(input("Enter Value: ")), float(input("Enter Value: ")))
                print(BLUE + "--------------The answer is:", calc.multiply(), "--------------")
            elif y == 4:
                calc = AECalculatorFormulas.BasicMath(float(input("Enter Value: ")), float(input("Enter Value: ")))
                print(BLUE + "--------------The answer is:", calc.divide(), "--------------")
            elif y == 5:
                calc = AECalculatorFormulas.BasicMath(float(input("Enter Value: ")), float(input("Enter Value: ")))
                print(BLUE + "--------------The answer is:", calc.exponent(), "--------------")
            elif y == 6:
                calc = AECalculatorFormulas.BasicMath(float(input("Enter Value: ")))
                print(BLUE + "--------------The answer is:", calc.root(), "--------------")
            elif y == 7:
                calc = AECalculatorFormulas.BasicMath(float(input("Enter Value: ")), float(input("Enter Value: ")))
                print(BLUE + "--------------The answer is:", calc.logarithm(), "--------------")
            elif y == 8:
                calc = AECalculatorFormulas.BasicMath(float(input("Enter Value: ")))
                print(BLUE + "--------------The answer is:", calc.sin(), "--------------")
            elif y == 9:
                calc = AECalculatorFormulas.BasicMath(float(input("Enter Value: ")))
                print(BLUE + "--------------The answer is:", calc.cos(), "--------------")
            elif y == 10:
                calc = AECalculatorFormulas.BasicMath(float(input("Enter Value: ")))
                print(BLUE + "--------------The answer is:", calc.tan(), "--------------")
            elif y == 11:
                calc = AECalculatorFormulas.BasicMath(float(input("Enter Value: ")))
                print(BLUE + "--------------The answer is:", calc.arc_sin(), "--------------")
            elif y == 12:
                calc = AECalculatorFormulas.BasicMath(float(input("Enter Value: ")))
                print(BLUE + "--------------The answer is:", calc.arc_cos(), "--------------")
            elif y == 13:
                calc = AECalculatorFormulas.BasicMath(float(input("Enter Value: ")))
                print(BLUE + "--------------The answer is:", calc.arc_tan(), "--------------")
            elif y == 14:
                calc = AECalculatorFormulas.BasicMath(float(input("Enter Value: ")))
                print(BLUE + "--------------The answer is:", calc.hyp_sin(), "--------------")
            elif y == 15:
                calc = AECalculatorFormulas.BasicMath(float(input("Enter Value: ")))
                print(BLUE + "--------------The answer is:", calc.hyp_cos(), "--------------")
            elif y == 16:
                calc = AECalculatorFormulas.BasicMath(float(input("Enter Value: ")))
                print(BLUE + "--------------The answer is:", calc.hyp_tan(), "--------------")
            # Executes when the user inputs an invalid command
            elif y < 1 or y > 16:
                raise ValueError(TRED + "--------------Please enter a valid Command""--------------")
        elif x == 2:
            # Advanced Math Formula List
            print(TGREEN + "       ╔═╗╔╦╗╦  ╦╔═╗╔╗╔╔═╗╔═╗╔╦╗  ╔╦╗╔═╗╔╦╗╦ ╦")
            print("       ╠═╣ ║║╚╗╔╝╠═╣║║║║  ║╣  ║║  ║║║╠═╣ ║ ╠═╣")
            print("       ╩ ╩═╩╝ ╚╝ ╩ ╩╝╚╝╚═╝╚═╝═╩╝  ╩ ╩╩ ╩ ╩ ╩ ╩")
            print(BLUE + "Choose a Formula:", RESET +
                         "\nInput 1 for Physics"
                         "\nInput 2 for Chemistry"
                         "\nInput 3 for Geometry"
                  )
            # User chooses a feature from the list
            y = int(input(YELLOW + "Enter Feature: "))
            # If statements will be executed depending on the feature chosen by the user
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
                # User chooses a formula from the list
                z = int(input(YELLOW + "Enter Feature: "))
                # If statements will be executed depending on the formula chosen by the user
                if z == 1:
                    calc = AECalculatorFormulas.Physics(float(input("Enter Value: ")), float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.speed(), "m/s", "--------------")
                elif z == 2:
                    calc = AECalculatorFormulas.Physics(float(input("Enter Value: ")), float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.velocity(), "m/s", "--------------")
                elif z == 3:
                    calc = AECalculatorFormulas.Physics(float(input("Enter Value: ")), float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.acceleration(), "m/s^2", "--------------")
                elif z == 4:
                    calc = AECalculatorFormulas.Physics(float(input("Enter Value: ")), float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.pressure(), "Pa", "--------------")
                elif z == 5:
                    calc = AECalculatorFormulas.Physics(float(input("Enter Value: ")), float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.force(), "N", "--------------")
                elif z == 6:
                    calc = AECalculatorFormulas.Physics(float(input("Enter Value: ")), float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.momentum(), "kg⋅m/s", "--------------")
                elif z == 7:
                    calc = AECalculatorFormulas.Physics(float(input("Enter Value: ")), float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.power(), "W", "--------------")
                elif z == 8:
                    calc = AECalculatorFormulas.Physics(float(input("Enter Value: ")), float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.volt(), "V", "--------------")
                elif z == 9:
                    calc = AECalculatorFormulas.Physics(float(input("Enter Value: ")), float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.current(), "A", "--------------")
                elif z == 10:
                    calc = AECalculatorFormulas.Physics(float(input("Enter Value: ")), float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.resistance(), "Ω", "--------------")
                elif z == 11:
                    calc = AECalculatorFormulas.Physics(float(input("Enter Value: ")), float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.kinetic_energy(), "J", "--------------")
                elif z == 12:
                    calc = AECalculatorFormulas.Physics(float(input("Enter Value: ")), float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.work(), "J", "--------------")
                elif z == 13:
                    calc = AECalculatorFormulas.Physics(float(input("Enter Value: ")), float(input("Enter Value: ")),
                                                        float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.coulombs_law(), "Ω", "--------------")
                elif z == 14:
                    calc = AECalculatorFormulas.Physics(float(input("Enter Value: ")), float(input("Enter Value: ")),
                                                        float(input("Enter Value: ")), float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.drift_velocity(), "m/s", "--------------")
                # Executes when the user inputs an invalid command
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
                # User chooses a formula from the list
                z = int(input(YELLOW + "Enter Feature: "))
                # If statements will be executed depending on the formula chosen by the user
                if z == 1:
                    calc = AECalculatorFormulas.Chemistry(float(input("Enter Value: ")), float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.density(), "cm^3", "--------------")
                elif z == 2:
                    calc = AECalculatorFormulas.Chemistry(float(input("Enter Value: ")), float(input("Enter Value: ")),
                                                          float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.boyle_p1(), "atm", "--------------")
                elif z == 3:
                    calc = AECalculatorFormulas.Chemistry(float(input("Enter Value: ")), float(input("Enter Value: ")),
                                                          float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.boyle_p2(), "atm", "--------------")
                elif z == 4:
                    calc = AECalculatorFormulas.Chemistry(float(input("Enter Value: ")), float(input("Enter Value: ")),
                                                          float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.boyle_v1(), "cm^3", "--------------")
                elif z == 5:
                    calc = AECalculatorFormulas.Chemistry(float(input("Enter Value: ")), float(input("Enter Value: ")),
                                                          float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.boyle_v2(), "cm^3", "--------------")
                elif z == 6:
                    calc = AECalculatorFormulas.Chemistry(float(input("Enter Value: ")), float(input("Enter Value: ")),
                                                          float(input("Enter Value: ")), float(input("Enter Value: ")),
                                                          float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.combined_gas_law_p1(), "atm", "--------------")
                elif z == 7:
                    calc = AECalculatorFormulas.Chemistry(float(input("Enter Value: ")), float(input("Enter Value: ")),
                                                          float(input("Enter Value: ")), float(input("Enter Value: ")),
                                                          float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.combined_gas_law_p2(), "atm", "--------------")
                elif z == 8:
                    calc = AECalculatorFormulas.Chemistry(float(input("Enter Value: ")), float(input("Enter Value: ")),
                                                          float(input("Enter Value: ")), float(input("Enter Value: ")),
                                                          float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.combined_gas_law_v1(), "cm^3", "--------------")
                elif z == 9:
                    calc = AECalculatorFormulas.Chemistry(float(input("Enter Value: ")), float(input("Enter Value: ")),
                                                          float(input("Enter Value: ")), float(input("Enter Value: ")),
                                                          float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.combined_gas_law_v2(), "cm^3", "--------------")
                elif z == 10:
                    calc = AECalculatorFormulas.Chemistry(float(input("Enter Value: ")), float(input("Enter Value: ")),
                                                          float(input("Enter Value: ")), float(input("Enter Value: ")),
                                                          float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.combined_gas_law_t1(), "K", "--------------")
                elif z == 11:
                    calc = AECalculatorFormulas.Chemistry(float(input("Enter Value: ")), float(input("Enter Value: ")),
                                                          float(input("Enter Value: ")), float(input("Enter Value: ")),
                                                          float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.combined_gas_law_t2(), "K", "--------------")
                # Executes when the user inputs an invalid command
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
                # User chooses a formula from the list
                z = int(input(YELLOW + "Enter Feature: "))
                # If statements will be executed depending on the formula chosen by the user
                if z == 1:
                    calc = AECalculatorFormulas.Geometry(float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.square_area(), "cm^2", "--------------")
                elif z == 2:
                    calc = AECalculatorFormulas.Geometry(float(input("Enter Value: ")), float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.rectangle_area(), "cm^2", "--------------")
                elif z == 3:
                    calc = AECalculatorFormulas.Geometry(float(input("Enter Value: ")), float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.triangle_area(), "cm^2", "--------------")
                elif z == 4:
                    calc = AECalculatorFormulas.Geometry(float(input("Enter Value: ")), float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.circle_area(), "cm^2", "--------------")
                elif z == 5:
                    calc = AECalculatorFormulas.Geometry(float(input("Enter Value: ")), float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.parallelogram_area(), "cm^2", "--------------")
                elif z == 6:
                    calc = AECalculatorFormulas.Geometry(float(input("Enter Value: ")), float(input("Enter Value: ")),
                                                         float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.trapezoid_area(), "cm^2", "--------------")
                elif z == 7:
                    calc = AECalculatorFormulas.Geometry(float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.square_perimeter(), "cm", "--------------")
                elif z == 8:
                    calc = AECalculatorFormulas.Geometry(float(input("Enter Value: ")), float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.rectangle_perimeter(), "cm", "--------------")
                elif z == 9:
                    calc = AECalculatorFormulas.Geometry(float(input("Enter Value: ")), float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.triangle_perimeter(), "cm", "--------------")
                elif z == 10:
                    calc = AECalculatorFormulas.Geometry(float(input("Enter Value: ")), float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.parallelogram_perimeter(), "cm", "--------------")
                elif z == 11:
                    calc = AECalculatorFormulas.Geometry(float(input("Enter Value: ")), float(input("Enter Value: ")),
                                                         float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.trapezoid_perimeter(), "cm", "--------------")
                elif z == 12:
                    calc = AECalculatorFormulas.Geometry(float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.circle_circumference(), "m", "--------------")
                elif z == 13:
                    calc = AECalculatorFormulas.Geometry(float(input("Enter Value: ")), float(input("Enter Value: ")),
                                                         float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.rectangular_prism_surface(), "m^2", "-----------")
                elif z == 14:
                    calc = AECalculatorFormulas.Geometry(float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.cube_sa(), "m^2", "--------------")
                elif z == 15:
                    calc = AECalculatorFormulas.Geometry(float(input("Enter Value: ")), float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.cylinder_sa(), "m^2", "--------------")
                elif z == 16:
                    calc = AECalculatorFormulas.Geometry(float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.sphere_sa(), "m^2", "--------------")
                elif z == 17:
                    calc = AECalculatorFormulas.Geometry(float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.cone_sa(), "m^2", "--------------")
                elif z == 18:
                    calc = AECalculatorFormulas.Geometry(float(input("Enter Value: ")), float(input("Enter Value: ")),
                                                         float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.rectangular_prism_volume(), "cm^3", "-----------")
                elif z == 19:
                    calc = AECalculatorFormulas.Geometry(float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.cube_volume(), "cm^3", "--------------")
                elif z == 20:
                    calc = AECalculatorFormulas.Geometry(float(input("Enter Value: ")), float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.cylinder_volume, "cm^3", "--------------")
                elif z == 21:
                    calc = AECalculatorFormulas.Geometry(float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.sphere_volume(), "cm^3", "--------------")
                elif z == 22:
                    calc = AECalculatorFormulas.Geometry(float(input("Enter Value: ")), float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.cone_volume(), "cm^3", "--------------")
                elif z == 23:
                    calc = AECalculatorFormulas.Geometry(float(input("Enter Value: ")), float(input("Enter Value: ")),
                                                         float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.pyramid_volume(), "cm^3", "--------------")
                # Executes when the user inputs an invalid command
                elif z < 1 or z > 23:
                    raise ValueError(TRED + "--------------Please enter a valid Command""--------------")
            # Executes when the user inputs an invalid command
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
            # User chooses a feature from the list
            y = int(input(YELLOW + "Enter Feature: "))
            # If statements will be executed depending on the feature chosen by the user
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
                # User chooses a formula from the list
                z = int(input(YELLOW + "Enter Feature: "))
                # If statements will be executed depending on the formula chosen by the user
                if z == 1:
                    calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.fahrenheit_to_celsius(), "°C", "--------------")
                elif z == 2:
                    calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.celsius_to_fahrenheit(), "°F", "--------------")
                elif z == 3:
                    calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.celsius_to_kelvin(), "K", "--------------")
                elif z == 4:
                    calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                    print(BLUE + "--------------The answer is:", calc.kelvin_to_celsisus(), "°C", "--------------")
                # Executes when the user inputs an invalid command
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
                # User chooses a feature from the list
                z = int(input(YELLOW + "Enter Feature: "))
                # If statements will be executed depending on the feature chosen by the user
                if z == 1:
                    # Metric Length Formula List
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
                    # User chooses a formula from the list
                    w = int(input(YELLOW + "Enter Feature: "))
                    # If statements will be executed depending on the formula chosen by the user
                    if w == 1:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.inches_to_centimeter(), "cm", "-------------")
                    elif w == 2:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.centimeter_to_inches(), "in", "-------------")
                    elif w == 3:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.meters_to_kilometers(), "km", "-------------")
                    elif w == 4:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.kilometers_to_meters(), "m", "--------------")
                    elif w == 5:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.kilometers_to_miles(), "mi", "--------------")
                    elif w == 6:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.miles_to_kilometers(), "km", "--------------")
                    elif w == 7:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.yard_to_feet(), "ft", "--------------")
                    elif w == 8:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.feet_to_yard(), "yd", "--------------")
                    # Executes when the user inputs an invalid command
                    elif w < 1 or w > 8:
                        raise ValueError(TRED + "--------------Please enter a valid Command""--------------")
                elif z == 2:
                    # Metric Volume Formula List
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
                    # User chooses a formula from the list
                    w = int(input(YELLOW + "Enter Feature: "))
                    # If statements will be executed depending on the formula chosen by the user
                    if w == 1:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.quarts_to_pints(), "pt", "--------------")
                    elif w == 2:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.pints_to_quarts(), "qt", "--------------")
                    elif w == 3:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.gallons_to_quarts(), "qt", "--------------")
                    elif w == 4:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.quarts_to_gallons(), "gal", "--------------")
                    elif w == 5:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.pint_to_cup(), "cup", "--------------")
                    elif w == 6:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.cup_to_pint(), "pt", "--------------")
                    # Executes when the user inputs an invalid command
                    elif w < 1 or w > 6:
                        raise ValueError(TRED + "--------------Please enter a valid Command""--------------")
                elif z == 3:
                    # Metric Weight Formula List
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
                    # User chooses a formula from the list
                    w = int(input(YELLOW + "Enter Feature: "))
                    # If statements will be executed depending on the formula chosen by the user
                    if w == 1:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.gram_to_kilogram(), "kg", "--------------")
                    elif w == 2:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.kilogram_to_grams(), "g", "--------------")
                    elif w == 3:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.pounds_to_kilograms(), "kg", "--------------")
                    elif w == 4:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.kilograms_to_pounds(), "pd", "--------------")
                    elif w == 5:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.kilograms_to_tons(), "ton", "--------------")
                    elif w == 6:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.tons_to_kilograms(), "kg", "--------------")
                    # Executes when the user inputs an invalid command
                    elif w < 1 or w > 6:
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
                # User chooses a feature from the list
                z = int(input(YELLOW + "Enter Feature: "))
                # If statements will be executed depending on the feature chosen by the user
                if z == 1:
                    # SI Positive Units Formula List
                    print(TGREEN + "     ╔═╗╔═╗╔═╗╦╔╦╗╦╦  ╦╔═╗  ╦ ╦╔╗╔╦╔╦╗╔═╗")
                    print("     ╠═╝║ ║╚═╗║ ║ ║╚╗╔╝║╣   ║ ║║║║║ ║ ╚═╗")
                    print("     ╩  ╚═╝╚═╝╩ ╩ ╩ ╚╝ ╚═╝  ╚═╝╝╚╝╩ ╩ ╚═╝")
                    print(BLUE + "Choose a Formula:", RESET +
                          "\nInput 1 for Hecto to Deca"
                          "\nInput 2 for Kilo to Hecto"
                          "\nInput 3 for Mega to Kilo"
                          "\nInput 4 for Giga to Mega"
                          "\nInput 5 for Tera to Giga"
                          )
                    # User chooses a formula from the list
                    w = int(input(YELLOW + "Enter Feature: "))
                    # If statements will be executed depending on the formula chosen by the user
                    if w == 1:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.hecto_to_deca(), "da", "--------------")
                    elif w == 2:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.kilo_to_hecto(), "H", "--------------")
                    elif w == 3:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.mega_to_kilo(), "K", "--------------")
                    elif w == 4:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.giga_to_mega(), "M", "--------------")
                    elif w == 5:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.tera_to_giga(), "G", "--------------")
                    # Executes when the user inputs an invalid command
                    elif w < 1 or w > 5:
                        raise ValueError(TRED + "--------------Please enter a valid Command""--------------")
                elif z == 2:
                    # SI PNegative Units Formula List
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
                    # User chooses a feature from the list
                    w = int(input(YELLOW + "Enter Feature: "))
                    # If statements will be executed depending on the feature chosen by the user
                    if w == 1:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.deca_to_deci(), "d", "--------------")
                    elif w == 2:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.deci_to_centi(), "cm", "--------------")
                    elif w == 3:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.centi_to_mili(), "mm", "--------------")
                    elif w == 4:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.mili_to_micro(), "µ", "--------------")
                    elif w == 5:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.micro_to_nano(), "n", "--------------")
                    elif w == 6:
                        calc = AECalculatorFormulas.Conversion(float(input("Enter Value: ")))
                        print(BLUE + "--------------The answer is:", calc.nano_to_pico(), "p", "--------------")
                    # Executes when the user inputs an invalid command
                    elif w < 1 or w > 6:
                        raise ValueError(TRED + "--------------Please enter a valid Command""--------------")
                # Executes when the user inputs an invalid command
                elif z < 1 or z > 2:
                    raise ValueError(TRED + "--------------Please enter a valid Command""--------------")
            # Executes when the user inputs an invalid command
            elif y < 1 or y > 3:
                raise ValueError(TRED + "--------------Please enter a valid Command""--------------")
        # Ends the program
        elif x == 4:
            print(BLUE + "--------------Thank you for using AECalculator""--------------")
            print(RESET + "If there are any Concerns or insights regarding the program."
                          "\nYou may contact us through the following Emails:"
                          "\njdnepomuceno@donbosco.edu.ph"
                          "\npdcponciano@donbosco.edu.ph")
            break
        # Executes when the user inputs an invalid command
        elif x < 1 or x > 4:
            raise ValueError(TRED + "--------------Please enter a valid Command""--------------")
    # Executes when the user divides by zero
    except ZeroDivisionError:
        print(TRED + "--------------Please enter another value that is not Zero""--------------")
    # Executes when the user inputs an invalid command
    except ValueError:
        print(TRED + "--------------Please enter a valid Command""--------------")
