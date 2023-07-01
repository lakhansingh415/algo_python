from icecream import ic
def divde_array_median(array_size, unbalanced_array):
    median = array_size // 2
    ic(median)
    left_array_sub_set = unbalanced_array[:median]
    ic(left_array_sub_set)
    right_array_sub_set = unbalanced_array[median:]
    ic(right_array_sub_set)
    return left_array_sub_set, right_array_sub_set


def sum_of_array(left_array_sub_set, right_array_sub_set):
    left_array_summation = sum(left_array_sub_set)
    right_array_summation = sum(right_array_sub_set)
    return left_array_summation, right_array_summation


def find_element_to_add(left_candidate, right_candidate):
    return abs(left_candidate - right_candidate)


def make_balanced_array(unbalanced_array):
    array_size = len(unbalanced_array)
    left_array_sub_set, right_array_sub_set = divde_array_median(array_size, unbalanced_array)
    sum_left_array, sum_right_array = sum_of_array(left_array_sub_set, right_array_sub_set)
    return find_element_to_add(sum_left_array, sum_right_array)



if __name__ == "__main__":
    #unbalanced_array = input("Enter the list of numbers by comma separated: ").split(",")
    unbalanced_array = [1, 2, 1, 2, 1, 3]
    ic("the number to be added to make it balanced ",make_balanced_array(unbalanced_array))