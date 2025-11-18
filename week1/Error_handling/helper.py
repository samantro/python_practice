def clean_name(name):
    """Cleans up a name by stripping whitespace and capitalizing it."""
    if not isinstance(name, str):
        raise TypeError("Name must be a string.")
    return name.strip().title()


def safe_int(value):
    """Converts a value to an integer safely, raising ValueError if conversion fails."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return None