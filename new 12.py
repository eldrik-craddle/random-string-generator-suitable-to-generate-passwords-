import random

def generate_random_strings(num_loops=10, length=16, allowed_chars=None):
    """
    Generates multiple random strings of characters based on ASCII representation.

    Args:
        num_loops: Number of strings to generate (default: 10).
        length: Desired length of each string (default: 16).
        allowed_chars: A set of allowed characters (e.g., only alphanumeric).
    """

    for i in range(num_loops):
        random_string = generate_random_string(length=length, allowed_chars=allowed_chars)
        print(f"Generated random string ({i + 1} of {num_loops}):", random_string)

def generate_random_string(length=16, allowed_chars=None):
    """
    Generates a single random string of characters based on ASCII representation.

    Args:
        length: Desired length of the string (default: 16).
        allowed_chars: A set of allowed characters (e.g., only alphanumeric).

    Returns:
        A random string of ASCII characters.
    """

    binary_string = "".join([random.choice("01") for _ in range(length * 8)])
    blocks = [binary_string[i:i + 8] for i in range(0, len(binary_string), 8)]
    chars = [chr(int(block, 2)) for block in blocks]

    # Filter characters if allowed_chars is provided
    if allowed_chars:
        chars = [c for c in chars if c in allowed_chars]

    return "".join(chars)

# Example usage
generate_random_strings()  # Generates 10 random strings with default settings

# Example with customization
generate_random_strings(num_loops=5, length=24, allowed_chars="abcXYZ")  # Generates 5 strings with length 24 and limited characters
