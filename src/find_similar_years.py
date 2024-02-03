def find_similar_years(base_year, end_year):
    similar_years = []
    remainder = base_year % 4

    if remainder == 0:
        repeat_year = base_year + 28
    elif remainder == 1:
        repeat_year = base_year + 6
    else:
        repeat_year = base_year + 11

    while repeat_year <= end_year:
        similar_years.append(repeat_year)
        
        if (repeat_year % 4 == 0 and repeat_year % 100 != 0) or repeat_year % 400 == 0:
            repeat_year += 28
        else:
            remainder = repeat_year % 4
            if remainder == 0:
                repeat_year += 28
            elif remainder == 1:
                repeat_year += 6
            else:
                repeat_year += 11

    return similar_years
