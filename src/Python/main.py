from sorting import quicksort
from sorting import mergesort
from sorting import heapsort
from sorting import countingsort
from sorting import bucketsort
from sorting import bubblesort
from sorting import selectionsort
from sorting import insertionsort

from search import binsearch
from search import quickselect

from graph import articulation_point
from graph import bfs
from graph import dfs
from graph import eulercycle
from graph import topsort
from graph import strong
from graph import bridges

def sorting():
    print("------------ Sorting Algorithms ---------------")
    quicksort.test()
    mergesort.test()
    heapsort.test()
    countingsort.test()
    bucketsort.test()
    bubblesort.test()
    selectionsort.test()
    insertionsort.test()

def dynamic():
    print("------------ Dynamic Algorithms ---------------")

def graph():
    print("------------ Graph Algorithms -----------------")
    dfs.test()
    bfs.test()
    eulercycle.test()
    bridges.test()
    strong.test()
    topsort.test()
    articulation_point.test()



def weighted_graph():
    print("------------ Weighted Graph Algorithms --------")

def search():
    print("------------ Search Algorithms ----------------")
    quickselect.test()
    binsearch.test()

if __name__ == "__main__":
    print("Algorithms")
    #sorting()
    #dynamic()
    graph()
    #weighted_graph()
    #search()


