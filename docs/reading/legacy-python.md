# Advanced Python handout

[Chapter index](index.md) · [Source coverage](sources.md)

**Reading is for you; page completion is optional.** If you can explain the concepts and answer the mentor's questions yourself, that is enough. Use these pages and the course videos to deepen understanding during the exercises with your approved agent. [Learning route and manual-work boundaries](index.md).

<details>
<summary>On this page</summary>

- [Advanced Python Training](#advanced-python-training)

- [Type Hints](#type-hints)

- [Decorators](#decorators)

- [Enums](#enums)

- [Multiprocessing](#multiprocessing)

- [Streamlit](#streamlit)

</details>

**Historical handout, preserved in full.** This records the older learner text; historical schedules and instructions to complete every reading or old assignment are superseded by the stage syllabus above. Reading links now point to local explanations. Video links retain their source destinations. The current required exercises are linked from the stage syllabus.

## Advanced Python Training

In this training episode you will learn some more advanced stuff that will come in handy later on.

Specifically, you will learn the following:

Type Hints

Decorators

Dataclasses 😍

Pydantic

Enums

Multiprocessing/multithreading

Streamlit

You are expected to learn stuff on your own (by googling etc), but feel free to ask for help if you need it.

## Type Hints

As you know, python is a dynamically typed language. Therefore, you are not required to specify your variables’ types. Nevertheless, specifying the expected types of your variables in your code can help a lot - it improves readability, lets your IDE auto-complete and analyze your code better, and makes it easier to spot bad code or possible bugs.

Start learning what type hints are and how to use them by going through the following blog-post: [https://towardsdatascience.com/type-hints-in-python-everything-you-need-to-know-in-5-minutes-24e0bad06d0b](python-tools.md).

Continue by skimming through the official docs just so you know what’s available: [https://docs.python.org/3/library/typing.html](python-tools.md).

If you need it, here is a nice cheat-sheet: [https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html](python-tools.md).

From now on, write type hints in all of your code throughout the training program, and follow the following guidelines.

### Our guidelines for using type hints

Each function should be 100% type-hinted - all parameters and the return value.

If the return value is None, you can omit the return value’s type hint.

Use composite type hints; `d: Dict` is not enough, write `d: Dict[KeyType, ValueType]` (e.g. Dict[str, int])

When initializing an empty composite variable (e.g. my_dict = {}), add a type hint so that the reader will know what to expect (e.g. my_dict: Dict[str, int] = {}).

If a variable's type is obvious from its declaration, don’t add a type hint. For example:

i = 3  # obviously the type is int, i: int = 3 doesn’t help anybody

j = i + 1  # we know i’s type is int, so j’s type is easily inferred

ret_val = some_func()  # if some_func is annotated, then the return type is known from its declaration. If it is not, adding ret_val: SomeType = some_func() might be helpful.

Whenever you feel a type hint would add clarity to your code - add it! It takes about a second.

## Decorators

learn what a python decorator is: [https://www.programiz.com/python-programming/decorator](python-tools.md). You can look in other places if you find them to explain better.

Implement your own decorator: you can choose whatever you want to do (but keep it simple)

A decent default is to implement a decorator that tracks how long it took for a method to run.

Learn about useful decorators (some also appear here:https://medium.com/data-science/10-fabulous-python-decorators-ab674a732871):

Lru_cache ([https://docs.python.org/3/library/functools.html#functools.lru_cache](python-tools.md))

Functools is great, you can take a look at other stuff as well

Property ([https://www.programiz.com/python-programming/property](python-tools.md))

Dataclasses ([https://docs.python.org/3/library/dataclasses.html](python-tools.md))

Singledispatch ([https://docs.python.org/3/library/functools.html#functools.singledispatch](python-tools.md))

classmethod & staticmethod ([https://stackoverflow.com/a/12179752](python-tools.md))

For each decorator, understand what it is good for and use it in a minimal example.

## Enums

Just read the official tutorial: [https://docs.python.org/3.11/howto/enum.html](python-tools.md). Then explain to your supervisor why and when using an Enum is advised.

## Multiprocessing

Implement every part below using all of these methods, and compare the execution times:

Using simple for-loops/list comprehension

Using map()

Using a multiprocessing.pool.Pool or concurrent.futures.Executor object

Using a concurrent.futures.ThreadPoolExecutor object

Make sure to set the hyperparameters of the experiments in a way that makes the experiment minteresting but not too time consuming.

Given a list of N values, calculate a list of the square values (x^2)

Perform some compute-heavy operation N times

Here is an example for a function you can use as the compute-heavy operation. It approximates 𝞹. The higher the approximation order, the better it is (and the longer it takes to compute).

def pi_approximation(order: int) -> float:

return (4 / order) * sum(1 / (1 + ((i - 0.5) / order) ** 2) for i in range(order))

Perform some IO-heavy operation N times, e.g. reading/writing a lot of files to disk or performing DB / web requests.

Here is an example for a function you can use as the IO-heavy operation. It just writes boring text to a temporary file (no need to delete them manually).

import tempfile

def write_text_to_tmp_file(text_length: int):

base_text = 'bla'

text = base_text * (text_length // len(base_text))

with tempfile.TemporaryFile() as fp:

fp.write(text.encode())

Explain - which multiprocessing method is better for which scenario, and why?

Read about the python Queue ([https://docs.python.org/3/library/queue.html](python-tools.md))

## Streamlit

First, learn about Streamlit - what it is and why it is needed ([https://docs.streamlit.io/](python-tools.md)). Get familiar with the basics (start here: [https://docs.streamlit.io/library/get-started](python-tools.md)).

### Your first streamlit app

Implement an app that presents the experiments you did in the multiprocessing exercise. You should provide the following:

Let the user decide which functionality (from sections 1-3 in the multiprocessing exercise) he wants to check

Let the user insert the parameters to the function he is benchmarking

Present the results to the user in a nice way.
