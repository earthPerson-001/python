
def common_element_lister(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    set3 = set1.intersection(set2)
    list3 = list(set3)
    print("The list consisting of common elements is", list3)


list_1 = [1, 2, 3, "apple", "newton", "einstein"]
list_2 = [1, 3, 5, 7, "relativity", "steve"]

common_element_lister(list_1, list_2)
