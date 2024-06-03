def add_diamond(data):
    """
    Adds a new diamond entry to the dataset.

    Args:
        data (list of dict): The current dataset.

    Returns:
        None
    """
    try:
        new_entry = {}
        new_entry['carat'] = input("Enter carat: ")
        new_entry['cut'] = input("Enter cut: ")
        new_entry['color'] = input("Enter color: ")
        new_entry['clarity'] = input("Enter clarity: ")
        new_entry['depth'] = input("Enter depth: ")
        new_entry['table'] = input("Enter table: ")
        new_entry['price'] = input("Enter price: ")
        new_entry['x'] = input("Enter x: ")
        new_entry['y'] = input("Enter y: ")
        new_entry['z'] = input("Enter z: ")
        data.append(new_entry)
        print("New diamond entry added.")
    except Exception as e:
        print(f"An error occurred while adding a diamond: {e}")
