from AECalcFormulas import BasicMath
from AECalcFormulas import AdvancedMath

while True:
    # Choosing a Feature
    print("<AECalculator Main>")
    print("Choose a Feature:"
          "\nInput 1 for Basic Math"
          "\nInput 2 Advanced Math"
          "\nInput 3 for Conversions"
          )
    x = int(input("Enter Feature: "))

    if x == 1:
        # Basic Math Formula List
        print("<AECalculator Basic Math>")
        print("Choose a Formula:"
              "\nInput 1 for Addition"
              "\nInput 2 for Subtraction"
              "\nInput 3 for Multiplication"
              "\nInput 4 for Division"
              "\nInput 5 for Exponent"
              "\nInput 6 for Roots"
              "\nInput 7 for Logarithm"
              "\nInput 8 for Sin Function"
              )

        y = int(input("Enter Feature: "))
        if y == 1:
            add = BasicMath.add()
            print("The answer is: ", add)
        elif y == 2:
            sub = BasicMath.subtract()
            print("The answer is: ", sub)
        elif y == 3:
            mul = BasicMath.multiply()
            print("The answer is: ", mul)
        elif y == 4:
            div = BasicMath.divide()
            print("The answer is: ", div)
        elif y == 5:
            exp = BasicMath.exponent()
            print("The answer is: ", exp)
        elif y == 6:
            roo = BasicMath.root()
            print("The answer is: ", roo)
        elif y == 7:
            log = BasicMath.logarithm()
            print("The answer is: ", log)
        elif y == 8:
            sin = BasicMath.sin()
            print("The answer is: ", sin)
        elif y == 9:
            cos = BasicMath.cos()
            print("The answer is: ", cos)
        elif y == 10:
            tan = BasicMath.tan()
            print("The answer is: ", tan)
        elif y == 11:
            asi = BasicMath.arc_sin()
            print("The answer is: ", asi)

    elif x == 2:
        # Advanced Math Formula List
        print("<AECalculator Advanced Math>")
        print("Choose a Formula:"
              "\nInput 1 for Physics"
              "\nInput 2 for Chemistry"
              "\nInput 3 for Geometry")
        y = int(input("Enter Feature: "))

        if y == 1:
            # Physics Formula List
            print("<AECalculator Advanced Math Physics>")
            print("Choose a Formula:"
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
            z = int(input("Enter Feature: "))

            if z == 1:
                spd = AdvancedMath.Physics.speed()
                print("The speed is: ", spd)
            elif z == 2:
                vel = AdvancedMath.Physics.velocity()
                print("The velocity is: ", vel)
            elif z == 3:
                acc = AdvancedMath.Physics.acc()
                print("The acceleration is: ", acc)
            elif z == 4:
                pre = AdvancedMath.Physics.pressure()
                print("The pressure is: ", pre)
            elif z == 5:
                forc = AdvancedMath.Physics.force()
                print("The force is: ", forc)
            elif z == 6:
                mom = AdvancedMath.Physics.momen()
                print("The momentum is: ", mom)
            elif z == 7:
                pow = AdvancedMath.Physics.power()
                print("The power is: ", pow)
            elif z == 8:
                vol = AdvancedMath.Physics.volt()
                print("The voltage is: ", vol)
            elif z == 9:
                cur = AdvancedMath.Physics.current()
                print("The current is: ", cur)
            elif z == 10:
                res = AdvancedMath.Physics.resistance()
                print("The resistance is: ", res)
            elif z == 11:
                ke = AdvancedMath.Physics.ke()
                print("The kinetic energy is: ", ke)
            elif z == 12:
                wor = AdvancedMath.Physics.work()
                print("The work is: ", wor)
            elif z == 13:
                col = AdvancedMath.Physics.coulombslaw()
                print("The electric force is: ", col)
            elif z == 14:
                drv = AdvancedMath.Physics.driftv()
                print("The drift velocity is: ", drv)

        elif y == 2:
            # Chemistry Formula List
            print("<AECalculator Advanced Math Chemistry>")
            print("Choose a Formula:"
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
            z = int(input("Enter Feature: "))
            if z == 1:
                den = AdvancedMath.Chemistry.density()
                print("The density is: ", den)
            elif z == 2:
                bp1 = AdvancedMath.Chemistry.boyle_p1()
                print("The P1 value is: ", bp1)
            elif z == 3:
                bp2 = AdvancedMath.Chemistry.boyle_p2()
                print("The P2 value is: ", bp2)
            elif z == 4:
                bv1 = AdvancedMath.Chemistry.boyle_v1()
                print("The V1 value is: ", bv1)
            elif z == 5:
                bv2 = AdvancedMath.Chemistry.boyle_v2()
                print("The V2 value is: ", bv2)
            elif z == 6:
                cp1 = AdvancedMath.Chemistry.combined_gas_law_p1()
                print("The P1 value is: ", cp1)
            elif z == 7:
                cp2 = AdvancedMath.Chemistry.combined_gas_law_p2()
                print("The P2 value is: ", cp2)
            elif z == 8:
                cv1 = AdvancedMath.Chemistry.combined_gas_law_v1()
                print("The V1 value is: ", cv1)
            elif z == 9:
                cv2 = AdvancedMath.Chemistry.combined_gas_law_v2()
                print("The V2 value is: ", cv2)
            elif z == 10:
                ct1 = AdvancedMath.Chemistry.combined_gas_law_t1()
                print("The T1 value is: ", ct1)
            elif z == 11:
                ct2 = AdvancedMath.Chemistry.combined_gas_law_t2()
                print("The T2 value is: ", ct2)
        elif y == 3:
            # Geometry Formula List
            print("<AECalculator Advanced Math Geometry>")
            print("Choose a Formula:"
                  "\nInput 1 for Square(A)"
                  "\nInput 2 for Square(P)"
                  "\nInput 3 for Rectangle(A)"
                  "\nInput 4 for Rectangle(P)"
                  "\nInput 5 for Triangle(A)"
                  "\nInput 6 for Triangle(P)"
                  "\nInput 7 for Circle(A)"
                  "\nInput 8 for Circle(C)"
                  "\nInput 9 for Parallelogram(A)"
                  "\nInput 10 for Parallelogram(P)"
                  "\nInput 11 for Trapezoid(A)"
                  "\nInput 12 for Trapezoid(P)"
                  "\nInput 13 for Rectangular Prism(V)"
                  "\nInput 14 for Rectangular Prism(A)"
                  "\nInput 15 for Cube(V)"
                  "\nInput 16 for Cube(A)"
                  "\nInput 17 for Cylinder(V)"
                  "\nInput 18 for Cylinder(A)"
                  "\nInput 19 for Sphere(V)"
                  "\nInput 20 for Sphere(A)"
                  "\nInput 21 for Cone(V)"
                  "\nInput 22 for Cone(A)"
                  "\nInput 23 for Pyramid(V)"
                  )

            z = int(input("Enter Feature: "))
            if z == 1:
                sqa = AdvancedMath.Geometry.square_area()
                print("The area is: ", sqa)
            elif z == 2:
                sqp = AdvancedMath.Geometry.square_perimeter()
                print("The perimeter is: ", sqp)
            elif z == 3:
                rea = AdvancedMath.Geometry.rectangle_area()
                print("The area is: ", rea)
            elif z == 4:
                rep = AdvancedMath.Geometry.rectangle_perimeter()
                print("The perimeter is: ", rep)
            elif z == 5:
                tra = AdvancedMath.Geometry.triangle_area()
                print("The area is: ", tra)
            elif z == 6:
                trp = AdvancedMath.Geometry.triangle_perimeter()
                print("The perimeter is: ", trp)
            elif z == 7:
                cia = AdvancedMath.Geometry.circle_area()
                print("The area is: ", cia)
            elif z == 8:
                cic = AdvancedMath.Geometry.circle_circumference()
                print("The circumference is: ", cic)
            elif z == 9:
                paa = AdvancedMath.Geometry.parallelogram_area()
                print("The area is: ", paa)
            elif z == 10:
                pap = AdvancedMath.Geometry.parallelogram_perimeter()
                print("The perimeter is: ", pap)
            elif z == 11:
                tra = AdvancedMath.Geometry.trapezoid_area()
                print("The area is: ", tra)
            elif z == 12:
                trp = AdvancedMath.Geometry.trapezoid_perimeter()
                print("The perimeter is: ", trp)
            elif z == 13:
                rpv = AdvancedMath.Geometry.rectangular_prism_volume()
                print("The volume is: ", rpv)
            elif z == 14:
                rpa = AdvancedMath.Geometry.rectangular_prism_surface()
                print("The surface area is: ", rpa)
            elif z == 15:
                cuv = AdvancedMath.Geometry.cube_volume()
                print("The volume is: ", cuv)
            elif z == 16:
                cua = AdvancedMath.Geometry.cube_sa()
                print("The surface area is: ", cua)
            elif z == 17:
                cyv = AdvancedMath.Geometry.cylinder_volume()
                print("The volume is: ", cyv)
            elif z == 18:
                cya = AdvancedMath.Geometry.cylinder_sa()
                print("The surface area is: ", cya)
            elif z == 19:
                spv = AdvancedMath.Geometry.sphere_volume()
                print("The volume is: ", spv)
            elif z == 20:
                spa = AdvancedMath.Geometry.sphere_sa()
                print("The surface area is: ", spa)
            elif z == 21:
                cov = AdvancedMath.Geometry.cone_volume()
                print("The volume is: ", cov)
            elif z == 22:
                coa = AdvancedMath.Geometry.cone_sa()
                print("The surface area is: ", coa)
            elif z == 23:
                pyv = AdvancedMath.Geometry.pyramid_volume()
                print("The volume is: ", pyv)
    elif x == 3:
        # Conversions Formula List
        print("<AECalculator Conversions>")
        print("Choose a Formula:"
              "\nInput 1 for Temperature"
              "\nInput 2 for Metric"
              )
        y = int(input("Enter Feature: "))

        if y == 1:
            # Temperature Formula List
            print("<AECalculator Temperature>")
            print("Choose a Formula:"
                  "\nInput 1 for Fahrenheit to Celsius"
                  "\nInput 2 for Celsius to Fahrenheit"
                  "\nInput 3 for Celsius to Kelvin"
                  "\nInput 4 for Kelvin to Celsius"
                  )
            z = int(input("Enter Feature: "))

        elif y == 2:
            # Metric Formula List
            print("<AECalculator Metric Units>")
            print("Choose a Formula:"
                  "\nInput 1 for Length"
                  "\nInput 2 for Volume"
                  "\nInput 3 for Weight"
                  )
            z = int(input("Enter Feature: "))

            if z == 1:
                print("<AECalculator Metric Length Units>")
                print("Choose a Formula:"
                      "\nInput 1 for Inch to Centimeters"
                      "\nInput 2 for Centimeter to Inch"
                      "\nInput 3 for Meters to Kilometers"
                      "\nInput 4 for Kilometers to Meters"
                      "\nInput 5 for Kilometers to Miles"
                      "\nInput 6 for Miles to Kilometers"
                      "\nInput 7 for Yard to Feet"
                      "\nInput 8 for Feet to Yard"
                      )

            elif z == 2:
                print("<AECalculator Metric Volume Units>")
                print("Choose a Formula:"
                      "\nInput 1 for Quarts to Pints"
                      "\nInput 2 for Pints to Quarts"
                      "\nInput 3 for Gallon to Quarts"
                      "\nInput 4 for Quarts to Gallon"
                      )

            elif z == 3:
                print("<AECalculator Metric Weight Units>")
                print("Choose a Formula:"
                      "\nInput 1 for Gram to Kilogram"
                      "\nInput 2 for Kilogram to Gram"
                      "\nInput 3 for Pounds to Kilogram"
                      "\nInput 4 for Kilogram to Pounds"
                      "\nInput 1 for Kilogram to Tons"
                      "\nInput 2 for Tons to Kilograms"
                      )





