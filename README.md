# Advent Of Code ~ Python toolkit

Python Toolkit dedicated to the [Advent Of Code yearly challenge (AOC)](https://adventofcode.com/2024/about), to retrieve daily puzzles and run your solutions. Contains also my solutions for previous years.

## 1. Usage

### 1.1. Virtual environment

In order to use this toolkit, you will need to retrieve the dependencies of the project. The latter is using the dependencies manager [*uv*](https://docs.astral.sh/uv/guides/install-python/). It is also possible to retrieve the dependencies manually by using the [requirements.txt file](./requirements.txt).

```shell
pip3 install uv
```

### 1.2. Retrieve the daily problem

```shell
uv run main.py collect -d 1 -y 2025
# -d , --day : selected day
# -y, --year : selected year
```

allows to retrieve all the content associated to day 1 of year 2025 : 
* *README.md* : explanation of the given day problem
* *test_input.txt* : test input to validate your solution
* *real_input.txt* : final input to produce your final submission
* *solution.py* : python script template to fill with the solution

During your first query, the script will ask for your session token in order to download the input file (it will then be stored in the file named *.aoc_session* for the future commands). To get your session token, follow this procedure :
* Go to AOC official website (https://adventofcode.com/) and login to your personnal account                                              │
* Inspect the webpage using your browser (e.g Firefox, Google)                                                                            │
* Go to section 'Network', then refresh the page                                                                                          │
* Check the first 'GET' item and the argument 'Cookie' (must be the pattern :session=<your_session_token>) 

Example of expected output : 
```bash
──────────────────────────────────────────────────────── Advent of Code (AOC) Toolkit ────────────────────────────────────────────────────────
─────────────────────────────────────────────────────────── Collect Day 1 – 2025 ────────────────────────────────────────────────────────────
README → problems/2025/day_1/README.md
Test input → problems/2025/day_1/test_input.txt
Real input → problems/2025/day_1/real_input.txt
✔ Collect done !
```
### 1.3. Run your solution 

```shell
uv run main.py run -d 1 -y 2025 -p 1 -t true
# -d , --day : selected day
# -y, --year : selected year
# -p, --part : part 1 or 2
# -t, --test : test (True) or real (False) input
```

will run you **solution.py** and collect the answer for the provided part and input type (test input or real input). For example, the provided command will run the solution of **part 1** (third argument) for **test mode set to true** (fourth argument) for puzzle day 1 of 2025. 

Example of expected output : 

```bash
──────────────────────────────────────────────────────── Advent of Code (AOC) Toolkit ────────────────────────────────────────────────────────
 Year :2025
 Day :1
 Part :2
 Output : 123 
Result copied in clipboard ✔
```

## 2. Useful ressources for AOC

### 2.1. Basic tools
- **logical operations** : *all(c for c in conditions)*, *any(c for c in conditions)* to check multiple conditions
- **numpy tools** : *np.flipud*, *np.fliplr* to get vertically/horizontally mirrored array
- **text files** : *.splitlines()*, *.read()*, *.readlines()*
- **list operations** : *map(function,list)* and *list.sort(key=lambda ...)*, *sorted()*, *reversed()*
- **string sequences** : *.split()*, *.lstrip()*, *.rstrip()*, *.replace()*, *.zfill()*
- **regular expressions** : find patterns with *re.findall*, *re.search* and *re.match*, *str.__contains__(expr)*, *.group()*
- **set** object : useful to deal with *intersections*, *unions*, *difference*
- **tuple** : handle coordinates
- **iterables** : *enumerate*, *zip*
- **eval** : evaluate operations written as strings *eval(1+2)*

### 2.2. Python Packages 
- **[copy](https://docs.python.org/fr/3/library/copy.html)** : module *deepcopy* that allows to make a copy of an element completely detached from the original one (in terms of operations).
- **[heapq](https://docs.python.org/fr/3/library/heapq.html)** : combination of heap data type ("branch type") and deque (queue type operations). *heappop* to get the first element of the queue+ remove it from the queue at the same time. *heappush* to push a new element at the end of the queue. 
- **[collections](https://docs.python.org/fr/3/library/collections.html)** : modules such as *defaultdict* (dictionnary with enforced type), *Counter* (unique occurences,counts) *deque* (queue solving prolems with popleft, )
- **[itertools](https://docs.python.org/fr/3/library/itertools.html)** : *combinations*, *product*, *cache* (keep results in cache for recursion)
- **[simpy](https://simpy.readthedocs.io/en/latest/)** : implement/solve list of equations
- **[networkx](https://networkx.org)** : graph construction, minimal cut problems, connections

### 2.3. Algorithmic Methods
- **[Cache results](https://docs.python.org/3/library/functools.html)** : possibility to cache results, either in a list of using a decorator, in order to skip operations if already done in the past (very useful in recursion)
- **[Recursion](https://www.programiz.com/python-programming/recursion)** is the process of defining a function in terms of itself. Helpful for branching/path searching problems.
- **[Shoelace formula](https://en.wikipedia.org/wiki/Shoelace_formula)** allows to compute the area of a polygon given the list of its edges.
- **[Pick's Theorem](https://en.wikipedia.org/wiki/Pick%27s_theorem)** provides formula for the area of a polygon given the number of interior points and points on its boundary.
- **[Depth First Search (DFS)](https://en.wikipedia.org/wiki/Depth-first_search)** is an algorithm for traversing or searching tree or graph data structures. DFS is a traversal approach in which the traverse begins at the root node and proceeds through the nodes as far as possible until we reach the node with no unvisited nearby nodes.
- **[Breadth First Search (BFS)](https://en.wikipedia.org/wiki/Breadth-first_search)** is an algorithm for traversing or searching tree or graph data structures. BFS is a traversal approach in which we first walk through all nodes on the same level before moving on to the next level.  
\
***Image of the 2023 AOC Calendar***
![img](doc/img.png)
