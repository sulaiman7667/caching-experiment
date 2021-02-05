# Exercise: Caching Simulation

This exercise asks you to explore different caching strategies. 

You are given the following files:

* ```harness.py``` Main program/test harness.
* ```memory.py``` Memory simulation. Defines a class ```Memory```.
* ```cache.py``` Within this file there are two classes defined: ```CyclicCache``` and ```LRUCache```.

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
user@computer> python3 harness.py < in-10.txt
```

This will use the default Memory implementation and should result in
something like the following:

```
user@computer> python3 harness.py < in-10.txt 
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
user@computer> python3 harness.py -s LRU < in-10.txt
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

Your implementation of the caches should ***not*** make assumptions
about the implementation of ```lookup()``` in the ```memory.py```
class. Nor should it copy code from the implementation of
```lookup()```. If your implementation needs to call the lookup method
on the ```Memory``` class (for example because a value is not found in
the cache), it should do this through a call to
```super().lookup```. Your code may be tested against a **different**
implementation of ```memory.py```, so copying the code could then
result in errors. In order to simplify the exercise,
there is no need to check if the cache has been invalidated or worry
about flushing the cache -- you can assume that calls to the memory
lookup will always return the same answer (and thus if it's in the
cache it's safe to use the cached value). 

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
   * Keep track of how recently each slot has been used (accessed or stored).
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

Your submitted code will be run agains a number of test cases which
compare output with expected results. You should only change the
implementation of the appropriate classes in ```cache.py```. Take care
that your submitted solution does not include additional ```print```
statements or changes the way the results are reported in
```harness.py```.
