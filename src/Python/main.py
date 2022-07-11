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

from weightedgraphs import belmanford
from weightedgraphs import prim
from weightedgraphs import kruskal
from weightedgraphs import FloydWarshall
from weightedgraphs import EdmondsKarp
from weightedgraphs import djikstra

from dynamic import cut_rod
from dynamic import hassum
from dynamic import knapsack
from dynamic import longest_subsequence
from dynamic import longest_common_subsequence
from dynamic import matrix_chain_order

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
    cut_rod.test()
    hassum.test()
    knapsack.test()
    longest_subsequence.test()
    longest_common_subsequence.test()
    matrix_chain_order.test()

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
    belmanford.test()
    prim.test()
    kruskal.test()
    FloydWarshall.test()
    EdmondsKarp.test()
    djikstra.test()

def search():
    print("------------ Search Algorithms ----------------")
    quickselect.test()
    binsearch.test()

if __name__ == "__main__":
    print("Algorithms")
    sorting()
    dynamic()
    graph()
    weighted_graph()
    search()


