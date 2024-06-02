def is_subset(set1, set2):
    return set1.issubset(set2) and set1 != set2
set1 = set(map(int, input("Enter the elements of the first request separated by a space: ").split()))
set2 = set(map(int, input("Enter the elements of the second set separated by spaces: ").split()))
print(is_subset(set1, set2))