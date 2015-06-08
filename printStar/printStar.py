def print_star(star_number):
    space_begin=star_number/2
    star_begin=1
    str = ''
    for line in range(star_number):
        for space in range(space_begin):
            str = str + ' '
        for star in range(star_begin):
            str = str + '*'
        if line < star_number/2:
            space_begin = space_begin - 1
            star_begin = star_begin + 2
        else:
            space_begin = space_begin + 1
            star_begin = star_begin - 2
        print str
        str = ''