#AI-Generated Code Snippet

def sort_dicts_by_key(dict_list, sort_key):
    """
    Sorts a list of dictionaries by a specific key.

    Args:
        dict_list (list): List of dictionaries to sort.
        sort_key (str): The key to sort the dictionaries by.

    Returns:
        list: Sorted list of dictionaries.
    """
    return sorted(dict_list, key=lambda x: x.get(sort_key))

# Example usage:
# data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
# sorted_data = sort_dicts_by_key(data, 'age')
# print(sorted_data)




#Manual code Snippet 
# Bubble Sort Implementation for Sorting a List of Dictionaries by a Key
def sort_dict_list(dict_list, sort_key):
    """
    Sorts a list of dictionaries by the specified key using bubble sort.

    Parameters:
        dict_list (list): A list of dictionaries.
        sort_key (str): The key to sort the dictionaries by.

    Returns:
        list: The sorted list of dictionaries.
    """
    n = len(dict_list)

    for i in range(n):
        for j in range(0, n - i - 1):
            # Handle missing keys by treating them as lower than any present key
            a = dict_list[j].get(sort_key, float('-inf'))
            b = dict_list[j + 1].get(sort_key, float('-inf'))

            if a > b:
                # Swap the dictionaries
                dict_list[j], dict_list[j + 1] = dict_list[j + 1], dict_list[j]

    return dict_list


#Manual code Snippet
# Selection Sort Implementation for Sorting a List of Dictionaries by a Key
def manual_sort_dicts_by_key(data, key):
    """
    Sorts a list of dictionaries based on a specified key manually (selection sort style).

    Parameters:
        data (list): List of dictionaries to be sorted.
        key (str): The dictionary key to sort by.

    Returns:
        list: A new list sorted by the specified key.
    """
    # Make a copy of the list to avoid modifying the original
    sorted_list = data[:]
    length = len(sorted_list)

    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            a = sorted_list[j].get(key, float('-inf'))
            b = sorted_list[min_index].get(key, float('-inf'))
            if a < b:
                min_index = j
        # Swap the smallest found with the current index
        sorted_list[i], sorted_list[min_index] = sorted_list[min_index], sorted_list[i]

    return sorted_list
    
    #Example usage:
    students = [
    {"name": "Liam", "score": 82},
    {"name": "Olivia", "score": 91},
    {"name": "Noah", "score": 75}
]

sorted_students = manual_sort_dicts_by_key(students, "score")

for student in sorted_students:
    print(student)

