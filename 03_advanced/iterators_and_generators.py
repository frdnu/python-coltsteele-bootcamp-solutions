"""
Custom Iterable Class: FibonacciSequence
Implements the iterator protocol (__iter__ and __next__).
Takes a maximum limit (limit: int) or generates infinite terms if limit is None.
Defensive check: raise ValueError if limit is provided and < 0.
Stops iteration via StopIteration once the sequence reaches the limit.
Stateful Generator Function: infinite_prime_generator()
Generates prime numbers infinitely using yield.
Must include internal state tracking to evaluate potential primes efficiently (e.g., trial division up to sqrt(n)).
Memory & Performance Profiler: measure_memory_footprint(limit: int)
Compares a list comprehension returning N items vs. a generator expression producing the same sequence.
Uses sys.getsizeof() to capture and return the byte sizes of both objects.
Prints structured system metrics comparing memory consumption.
Execution Block (if __name__ == "__main__":)
Instantiate FibonacciSequence and iterate through a bounded sequence.
Consume the first N primes from infinite_prime_generator() using next().
Run measure_memory_footprint(1_000_000) and log realistic system diagnostics.
"""


class FibonacciSequence:
    def __init__(self, limit: int):
        if limit <= 0:
            raise ValueError("Limit cant be in negative or zero!")
        else:
            self.limit = limit
            self.count = 0
            self.first = 0
            self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count != self.limit:
            current = self.first

            self.first, self.second = self.second, self.first + self.second
            self.count += 1
            return current

        raise StopIteration("Iteration Complete")


seq1 = FibonacciSequence(5)
