

def delete_diamond(data):
    """
    Deletes a diamond entry from the dataset.

    Args:
        data (list of dict): The current dataset.

    Returns:
        None
    """
    try:
        index = int(input("Enter the index of the diamond to delete: "))
        if 0 <= index < len(data):
            del data[index]
            print("Diamond entry deleted.")
        else:
            print("Invalid index. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred while deleting a diamond: {e}")