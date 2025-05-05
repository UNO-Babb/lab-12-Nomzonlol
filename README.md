[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=19423955)
# Lab 12 - Searching & Sorting

In this lab we will be investigating the relative speed of the different sorting algorithms we had discussed in our lecture. You'll need to run each of them and record the time in the text document and respond to the questions. Finally, you will upload the responses to your GitHub repo.

## The lists
We are looking at three lists:
- in order
- reversed order
- random

You can change the size of the lists but some of the sorting techniques will take a lot longer as the size gets larger. This makes since when we remember that the efficiency of the sort is **O(n<sup>2</sup>)** means that for 10,000 elements the list is making ~ 100,000,000 comparisons.

I have set the initial number to 10,000. On my computer the slower sorting methods will be around 30 seconds. This could be higher on your computer. If you let a sort go for more than a minute without result, knock the value down to 1,000 items.

## The sorts
All of the sorting methods have been written in the file AllSorts.py. You will need to run each of them by calling the package name first.
Ex: **AllSorts.mergeSort(list)**
- bubbleSort
- bubbleSortEarlyExit
- selectionSort
- insertionSort
- mergeSort

## Report.txt
This is where you should record the numbers that you get for each of the elements. There are also several reflection questions in this document.
