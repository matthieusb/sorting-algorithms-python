# -*- coding: utf-8 -*-

import general_utilities


def bubble_sort(listToSort, operator):
    """Sorts the given list using bubble algorithm and given operator.
    Returns a list

    :param listToSort: The list to sort
    :type listToSort: :class:`list`
    :param operator: operator.le for asc, operator.ge for desc
    :type operator: :class:`operator`
    """
    if listToSort:
        listToReturn = list(listToSort)  # copying the input list
        lengthMinusOne = len(listToReturn) - 1

        swappedFlag = True
        i = 0
        while i < lengthMinusOne and swappedFlag:
            swappedFlag = False
            j = 0
            while j < lengthMinusOne:
                if operator(listToReturn[j + 1], listToReturn[j]):
                    general_utilities.\
                        swap_list_elements(listToReturn, j, j + 1)
                    swappedFlag = True
                j = j + 1
            i = i + 1

        return listToReturn
    else:
        return []


def insertion_sort(listToSort, operator):
    """Sorts the given list using insertion algorithm and given operator.
    Returns a list

    :param listToSort: The list to sort
    :type listToSort: :class:`list`
    :param operator: operator.le for asc, operator.ge for desc
    :type operator: :class:`operator`
    """

    if listToSort:
        listToReturn = list(listToSort)
        listLength = len(listToReturn)
        for i in range(0, listLength):
            valueToInsert = listToReturn[i]
            indexToInsert = i

            while (
                indexToInsert > 0 and
                operator(valueToInsert, listToReturn[indexToInsert - 1])
            ):
                listToReturn[indexToInsert] = \
                    listToReturn[indexToInsert - 1]
                indexToInsert = indexToInsert - 1

            listToReturn[indexToInsert] = valueToInsert

        return listToReturn
    else:
        return []


def selection_sort(listToSort, operator):
    """Sorts the given list using selection algorithm and given operator.
    Returns a list

    :param listToSort: The list to sort
    :type listToSort: :class:`list`
    :param operator: operator.le for asc, operator.ge for desc
    :type operator: :class:`operator`
    """
    if listToSort:
        listToReturn = list(listToSort)
        listLength = len(listToReturn)
        listLengthMinusOne = listLength - 1

        for i in range(0, listLengthMinusOne):
            minIndex = i

            # Checking if the element is minimum of the whole list
            for j in range(i + 1, listLength):
                if operator(listToReturn[j], listToReturn[minIndex]):
                    minIndex = j

            if minIndex != i:
                general_utilities.swap_list_elements(
                    listToReturn, minIndex, i)

        return listToReturn
    else:
        return[]


def merge_sort(listToSort, operator):
    """Sorts the given list using merge algorithm and given operator.
    Returns a list

    :param listToSort: The list to sort
    :type listToSort: :class:`list`
    :param operator: operator.le for asc, operator.ge for desc
    :type operator: :class:`operator`
    """
    if listToSort:
        return merge_do_algo(listToSort, operator)
    else:
        return[]


def merge_do_algo(listToSort, operator):
    """Splits lists into 2 and launch merge algorithm on two list halves
    Returns a list (Recursive function)

    :param listToSort: The list you wish to sort
    :type listToSort: :class:`list`
    :param operator: operator.le for asc, operator.ge for desc
    :type operator: :class:`operator`
    """
    listSize = len(listToSort)

    if listSize == 1:
        return listToSort
    else:
        listFirstHalf = listToSort[:listSize/2]
        listSecondHalf = listToSort[listSize/2:]

        listFirstHalf = merge_do_algo(listFirstHalf, operator)
        listSecondHalf = merge_do_algo(listSecondHalf, operator)

    return merge_list_halves(listFirstHalf, listSecondHalf, operator)


def merge_list_halves(listOne, listTwo, operator):
    """Merges two lists according to operator sorting order
    Returns a list

    :param listOne: The first list to merge
    :type listOne: :class:`list`
    :param listTwo: The sconde list to merge
    :type listTwo: :class:`list`
    :param operator: operator.le for asc, operator.ge for desc
    :type operator: :class:`operator`
    """
    listResult = []

    while (listOne and listTwo):
        if operator(listTwo[0], listOne[0]):
            listResult.append(listTwo[0])
            listTwo.pop(0)
        else:
            listResult.append(listOne[0])
            listOne.pop(0)

    while listOne:
        listResult.append(listOne.pop(0))

    while listTwo:
        listResult.append(listTwo.pop(0))

    return listResult


def shell_sort(listToSort, operator):
    """Sorts the given list using shell algorithm and given operator.
    Returns a list

    :param listToSort: The list to sort
    :type listToSort: :class:`list`
    :param operator: operator.le for asc, operator.ge for desc
    :type operator: :class:`operator`
    """
    if listToSort:
        listResult = list(listToSort)
        interval = 1
        listLength = len(listResult)
        listLengthDiv3 = listLength / 3

        # Initializing knuth's interval
        while interval < listLengthDiv3:
            interval = interval * 3 + 1

        while interval > 0:
            for outer in range(interval, listLength):
                valueToInsert = listResult[outer]
                inner = outer

                while (
                    inner > interval - 1 and
                    operator(valueToInsert, listResult[inner - interval])
                ):
                    listResult[inner] = listResult[inner - interval]
                    inner = inner - interval

                listResult[inner] = valueToInsert
            interval = (interval - 1) / 3
        return listResult
    else:
        return []


def quick_sort(listToSort, operator):
    """Sorts the given list using quicksort algorithm and given operator.
    Returns a list

    :param listToSort: The list to sort
    :type listToSort: :class:`list`
    :param operator: operator.le for asc, operator.ge for desc
    :type operator: :class:`operator`
    """
    if listToSort:
        listResult = list(listToSort)
        return quick_sort_do_algo(listResult, operator, 0, len(listToSort) - 1)
    else:
        return[]


def quick_sort_partition_function(listToSort, operator, left, right, pivot):
    """Partitions and sorts the given list according to operator
    Returns an int
    This does not split the list, its sorts it according to the pivot

    :param listToSort: The list to sort
    :type listToSort: :class:`list`
    :param operator: operator.le for asc, operator.ge for desc
    :type operator: :class:`operator`
    :param left: left boundary to partition
    :type left: :class:`int`
    :param right: right boundary to partition
    :type right: :class:`int`
    :param pivot: the pivot used for comparison
    :type pivot: :class:`int`
    """
    leftPointer = left - 1
    rightPointer = right

    # Determine which strict operator we are dealing with
    operatorStrict = general_utilities.determine_strict_operator(operator)

    while True:
        leftPointer = leftPointer + 1
        while operatorStrict(listToSort[leftPointer], pivot):
            # while listToSort[leftPointer] < pivot:
            leftPointer = leftPointer + 1

        rightPointer = rightPointer - 1
        while (
            (rightPointer + 1) > 0 and
            # listToSort[rightPointer] > pivot
            operatorStrict(pivot, listToSort[rightPointer])
        ):
            rightPointer = rightPointer - 1

        if leftPointer >= rightPointer:
            break
        else:
            general_utilities.swap_list_elements(
                listToSort, leftPointer, rightPointer)

    general_utilities.swap_list_elements(listToSort, leftPointer, right)
    return leftPointer


def quick_sort_do_algo(listToSort, operator, left, right):
    """Launches quicksort parition algorithm for both list sides
    Returns a list

    :param listToSort: The list to sort
    :type listToSort: :class:`list`
    :param operator: operator.le for asc, operator.ge for desc
    :type operator: :class:`operator`
    :param left: left boundary to partition
    :type left: :class:`int`
    :param right: right boundary to partition
    :type right: :class:`int`
    """
    if right - left <= 0:
        return listToSort
    else:
        pivot = listToSort[right]
        partition = quick_sort_partition_function(
            listToSort, operator, left, right, pivot)
        quick_sort_do_algo(listToSort, operator, left, partition - 1)
        quick_sort_do_algo(listToSort, operator, partition + 1, right)

        return listToSort
