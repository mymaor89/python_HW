def main():
    print(to_metric(1, 'inch', 'cm'))  # => 2.54
    print(to_metric(1, 'foot', 'm'))  # => 0.3048
    print(to_metric(1, 'mile', 'cm'))  # => 160934
    print(to_metric(1, 'yard', 'mm'))  # => 914.4
#1 inch is 0.0254 meter
#1 foot is 0.3048 meter
#1 mile is 1609.344 meter
#1 yard is 0.9144 meter
def inch_to_m():
    return 0.0254
def foot_to_m():
    return 0.3048
def mile_to_m():
    return 1609.344
def yard_to_m():
    return 0.9144
def to_metric(num,from_units,to_units):
    """
    :param num:length in original units  
    :param from_units: string of original unit system
    :param to_units: string of new unit system
    :return: length in new unit system
    """
    if from_units is 'inch' and to_units is 'm':
        return num*inch_to_m()
    elif from_units is 'inch' and to_units is 'cm':
        return num*inch_to_m()*100
    elif from_units is 'inch' and to_units is 'mm':
        return num * inch_to_m() * 1000
    elif from_units is 'mile' and to_units is 'm':
        return num * mile_to_m()
    elif from_units is 'mile' and to_units is 'cm':
        return num * mile_to_m()*100
    elif from_units is 'mile' and to_units is 'mm':
        return num * mile_to_m()*1000
    elif from_units is 'yard' and to_units is 'm':
        return num * yard_to_m()
    elif from_units is 'yard' and to_units is 'cm':
        return num * yard_to_m()*100
    elif from_units is 'yard' and to_units is 'mm':
        return num * yard_to_m()*1000
    elif from_units is 'foot' and to_units is 'm':
        return num * foot_to_m()
    elif from_units is 'foot' and to_units is 'cm':
        return num * foot_to_m()*100
    elif from_units is 'foot' and to_units is 'cm':
        return num * foot_to_m()*1000
main()
