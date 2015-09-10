
from base.engine import Engine


if __name__ == "__main__":

    engine = Engine("names.txt", group_size=4)
    groups = engine.generate_groups()
    engine.nice_print_groups(groups)