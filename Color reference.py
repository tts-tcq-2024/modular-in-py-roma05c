rom ColorUtils import get_color_from_pair_number, MAJOR_COLORS, MINOR_COLORS
def build_color_reference():
    manual = "Color Coding Reference:\n"
    for pair_number in range(1, len(MAJOR_COLORS) * len(MINOR_COLORS) + 1):
        major_color, minor_color = get_color_from_pair_number(pair_number)
        manual += f"Pair Number {pair_number}: {major_color} {minor_color}\n"
    return manual
