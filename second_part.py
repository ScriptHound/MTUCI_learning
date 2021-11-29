from math import tan, pi


def calculate_area(side_len, sides_count):
    numerator = sides_count * side_len**2
    denominator = 4 * tan(pi/sides_count)
    area = numerator / denominator
    return area


def arithmetic_progression(n):
    result = n * (n + 1) / 2
    return result


if __name__ == '__main__':
    print("===FIRST ASSIGNMENT===")
    side_lenght = int(input("Enter side length\n"))
    sides_count = int(input("Enter sides count\n"))

    area = calculate_area(side_lenght, sides_count)
    print(f"Polygon area equals {area}")

    print("===SECOND ASSIGNMENT===")
    n = int(input("Enter length of arithmetic progression\n"))
    result = arithmetic_progression(n)
    print(f"Arithmetic progression is {result}")
