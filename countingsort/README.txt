folder contains countingsort and countingsort_driver python scripts.

countingsort contains functions NumberCountingSort and ABCCountingSort:
- NumberCountingSort sorts a list of negative and non-numbers
- ABCCountingSort sorts a list of strings as inlist

countingsort_driver contains function CountingSortDriver that accepts input parameters for creating a random input list to pass to counting sort function:
- length: length of list
- k: max value (for alphabetic, this is max number of characters)
- type: 'num' or 'str'
