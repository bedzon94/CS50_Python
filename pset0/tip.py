def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):

    #Takes str as input and removes $
    df = d.replace("$", "")

    #Converts results to float
    d_t_f = float(df)

    #Formats results to 1 decimal point
    d_final = "{:.1f}".format(d_t_f)
    return float(d_final)


def percent_to_float(p):
    #Takes str as input and removes %
    pf = p.replace("%", "")

    #Converts to float
    p_t_f = float(pf)

    #Converts % input to percent (div by 100)
    p_final = p_t_f / 100
    return float(p_final)



main()
