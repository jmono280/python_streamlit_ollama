def print_in_color(any, color="red"):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "purple": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
    }
    print(f"{colors[color]}", end="")
    print(any, end="")
    print("\033[00m", end="")
