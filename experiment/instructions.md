# Exercise: Caching Simulation

This exercise asks you to explore the results of applying caching
strategies.

In the first exercise, you should have implemented two different
strategies for caching: Cyclic and Least Recently Used.

For this exercise, your task is to run some experiments against
implementations of caching and report the results as a ```Jupyter```
notebook.

After the submission deadline for Exercise 1, a model solution for the
caching will be released (which includes an additional Random
strategy).

The caching code in this exercise uses a similar interface to that
defined in Exercise 1. If you would like to begin designing and
testing your experiment before the release of the implementation code,
you can either use your own implementations, or the stubs provided in
this project. Do be aware though: the initial code given in this
project is a ***stub***: there are no implementations of the
strategies and the classes will all return identical results.

You have the following files:

```memory.py``` This is a python file that defines several different
simulations of memory and caching. 

```Memory``` Access without caching. Objects of this class provide a
method ```lookup(location)``` that returns the results of a memory
lookup. There is also a method ```get_hit_count()``` that returns the
number of times the actual memory has been accessed.

There are three subclasses of ```Memory``` that should each redefine the
lookup function:

```CyclicCache``` A cache using cyclic eviction  
```LRUCache``` A cache using least recently used eviction  
```RandomCache``` A cache using random eviction  

As an example of usage:

```
from memory import Memory, CyclicCache, LRUCache, RandomCache
mem = Memory()
print(mem.lookup(1))
print(mem.lookup(1))
print(mem.lookup(1))
print(mem.get_hit_count())
```

This code creates a new memory simulation that uses the default
implementation. It then prints the results of three memory accesses
followed by the number of times that the actually memory has been
accessed. This should be ```3``` as the location is read from memory
each time (no caching).

If we contrast with the following:

```
from memory import Memory, CyclicCache, LRUCache, RandomCache
mem = CyclicCache()
print(mem.lookup(1))
print(mem.lookup(1))
print(mem.lookup(1))
print(mem.get_hit_count())
```

The final result should be ```3``` as the ```CyclicCache```
implementation will read once from memory and then cache the
result. Recall the caveat above that this will only be the case when
you have the complete implementation (as opposed to the stub). 

## The Task

Your task is to write a Jupyter notebook that runs a series of
experiments against these implementations and compares the
results. The questions that you will be looking to answer are

* How often does a lookup result in memory access?
* Are there differences between the behaviour of the strategies?

To answer these questions you will need to develop some test data
(lists of memory allocations to access) and then report on the results
of passing this test data to the objects.

A sample note book is given in ```Sample.ipynb```. This is not an
example of good practice, and would be given a low mark. 

### Stretch Goals

The implementations of the caches have an extension to those provided
in the first exercise. An additional parameter ```size=N``` can be
passed into the constructor (the default is 4). You can experiment
with changing this and see what impact it has.

You may also want to look at presenting the results in a nice way, for
example using graphs or histograms.

## Submission

Code should be submitted through ```git``` as usual. You should tag
the version that you would like to be marked with the tag
```ex2-experiment```. We expect to see a trail of commits in your
log. Submissions appearing fully formed in one commit will attract suspicions
of academic malpractice.



