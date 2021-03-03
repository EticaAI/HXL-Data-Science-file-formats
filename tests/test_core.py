# import time

# def something(duration=0.001):
#     """
#     Function that needs some serious benchmarking.
#     """
#     time.sleep(duration)
#     # You may return anything you want, like the result of a computation
#     return 123

# def test_my_stuff(benchmark):
#     # benchmark something
#     result = benchmark(something)

#     # Extra code, to verify that the run completed correctly.
#     # Sometimes you may want to check the result, fast functions
#     # are no good if they return incorrect results :-)
#     assert result == 123


# content of test_sample.py
def func(x):
    return x + 1

# def test_answererr():
#     assert func(3) == 5


def test_answer():
    assert func(4) == 5


# def test_answererr3():
#     assert func(3) == 5