from find_similar_years import *

if __name__ == '__main__':
    base_year = int(input("Enter the base year: "))
    similar_years = find_similar_years(base_year, 2100)

    print(f"The years similar to {base_year} are: {', '.join(map(str, similar_years))}")
