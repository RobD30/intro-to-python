def cylinder_volume(heigt, radius):
    pi = 3.14159
    return heigt * pi * (radius ** 2)


def population_density(population, land_area):
    density = (population / land_area)
    return density


def readable_timedelta(days):
    '''For weeks'''
    weeks = days // 7
    '''For Days'''
    remainder = days % 7
    return({} + "week(s) and " + {} + " day(s).").format(weeks, remainder)
