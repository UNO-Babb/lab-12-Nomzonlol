# The purpose of this lab is to see the speed of different sorting techniques.
# Use the same random seed to create the same random list of nubmers for each run.
# You can change the number of elements in the arrays
# We will test 3 arrays, one that is already in order, one that is sorted in reverse order, and one that it random.

import time
import random
import os
import copy

# Your current working directory needs to see the AllSorts.py
# If you have issues you should comment out this line.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import AllSorts

def run_sorting_test(sort_function, lists, sort_name):
    """Run a sorting test with the specified function and lists"""
    print(f"\n===== Testing {sort_name} =====")
    
    # Make deep copies of the lists to avoid modifying the originals
    ordered = copy.deepcopy(lists['ordered'])
    reversed_list = copy.deepcopy(lists['reversed'])
    random_list = copy.deepcopy(lists['random'])
    
    # Test ordered list
    start_time = time.time()
    sort_function(ordered)
    elapsed_time = time.time() - start_time
    print(f"Ordered list time: {elapsed_time:.5f} seconds")
    
    # Test reversed list
    start_time = time.time()
    sort_function(reversed_list)
    elapsed_time = time.time() - start_time
    print(f"Reversed list time: {elapsed_time:.5f} seconds")
    
    # Test random list
    start_time = time.time()
    sort_function(random_list)
    elapsed_time = time.time() - start_time
    print(f"Random list time: {elapsed_time:.5f} seconds")

def main():
    # Adjust this number to make tests run faster or slower
    # For slow sorts like bubble sort, you might want to use a smaller number
    number_terms = 10000
    
    # For slower algorithms, you might want to reduce the size for those specific tests
    bubble_sort_size = min(10000, number_terms)  # Limit bubble sort to 10,000 elements max
    
    print(f"Preparing lists with {number_terms} elements...")
    
    # Set random seed for reproducible results
    random.seed(2020)
    
    # Create the lists
    lists = {
        'ordered': list(range(number_terms)),
        'reversed': list(range(number_terms))[::-1],
        'random': [random.randint(1, 10000) for _ in range(number_terms)]
    }
    
    # Create smaller lists for potentially slower algorithms
    small_lists = {
        'ordered': list(range(bubble_sort_size)),
        'reversed': list(range(bubble_sort_size))[::-1],
        'random': [random.randint(1, 10000) for _ in range(bubble_sort_size)]
    }
    
    # Run tests for each sorting algorithm
    print(f"\nTesting with {bubble_sort_size} elements for potentially slower algorithms...")
    run_sorting_test(AllSorts.bubbleSort, small_lists, "Bubble Sort")
    run_sorting_test(AllSorts.bubbleSortEarlyExit, small_lists, "Bubble Sort with Early Exit")
    run_sorting_test(AllSorts.selectionSort, small_lists, "Selection Sort")
    run_sorting_test(AllSorts.insertionSort, small_lists, "Insertion Sort")
    
    # MergeSort is faster, so we can use the full-sized lists
    print(f"\nTesting with {number_terms} elements for faster algorithms...")
    run_sorting_test(AllSorts.mergeSort, lists, "Merge Sort")
    
    print("\nSorting tests complete!")

if __name__ == '__main__':
    main()
