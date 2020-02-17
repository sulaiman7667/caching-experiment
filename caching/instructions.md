# Exercise: Caching Simulation

This exercise asks you to explore different caching strategies. 

You are given the following files:

* ```caching.py``` Main program/test harness
* ```memory.py``` Memory simulation. Within this file there are three
  classes defined: ```Memory```, ```CyclicCache``` and ```LRUCache```

A test harness is given, which will read a sequence of integers from
the command line and outputs the results read from memory, along with
a record of memory accesses. Different caching strategies can be
employed, and an argument to the test harness specifies
which particular strategy should be used. 

The test harness will read data from standard input and write the
results to standard output, where each line of input consists of a
single integer representing a memory location. It will then write some
summary information.

For example, try running:

```
user@computer> python3 caching.py < in-10.txt
```

This will use the default Memory implementation and should result in
something like the following:

```
user@computer> python3 caching.py < in-10.txt 
001, 2, Memory Access c4ca4238
002, 8, Memory Access 6512bd43
003, 7, Memory Access a87ff679
004, 8, Memory Access 6512bd43
005, 4, Memory Access 8f14e45f
006, 7, Memory Access a87ff679
007, 3, Memory Access cfcd2084
008, 5, Memory Access 1679091c
009, 6, Memory Access e4da3b7f
010, 9, Memory Access d3d94468

Model: Memory
010 Accesses
010 Memory Hits
```

To use an alternative strategy, try:

```
user@computer> python3 caching.py -s LRU < in-10.txt
```

This will use the LRU implementation. Note that in the skeleton code
given, this will give the ***same answers*** as using the ```Memory```
strategy as the method has not (yet) been overridden. That's your
task!

Some sample test data is provided in the files ```in-*.txt```. 

## The Task

The task is to override the implementation of the
```lookup(address)``` operation which takes an address ```n``` and
returns the value at address ```n```. The operation should use the
approprate caching strategy to minimise memory accesses.

The cache should be of size ***4***.

Implement solutions using:

1. a Cyclic strategy.
   * Assume slots ```1,...,N``` in the cache.
   * Keep track of the next slot in the cache to be used (starting
     with ```1```).
   * When an value is cached, we increment our count to use the next
   slot.
   * Once all slots have been filled, go back to slot ```1``` and
     cycle round. 
2. an LRU strategy.
   * Assume ```N``` slots.
   * Keep track of how recently each slot has been used (
   access or stored).
   * If the cache is full and a new value needs to be stored, we
     remove the entry from the slot that was least recently used and replace with
     the new value.

Each of these strategies should be implemented in the appropriate
class.

Your code should conform to
[PEP8](https://www.python.org/dev/peps/pep-0008/) guidelines. We will
use [pycodestyle](https://pypi.org/project/pycodestyle/) to check
this. 

## Submission

Code should be submitted through ```git``` as usual. You should tag
the version that you would like to be marked with the tag
```ex1-caching```. We expect to see a trail of commits in your
log. Submissions appearing fully formed in one commit will attract suspicions
of academic malpractice. 

### Output

You should only change the implementation of the appropriate classes
in ```memory.py```. Also take care that your submitted solution doesn't
include additional unnecessary ```print``` statements or changes the
way the results are reported in ```caching.py```. 
