# Exercise 3
This exercise will look at write a test to check that our function works as expected.

## Setup
 Install the playground as a developer (`".[dev]"`), in editable (`-e`) mode, by navigating into the `rse-best-practices-playground` folder and running
```bash
pip install -e ".[dev]"
```
In this way you will have installed `pytest` and other useful tools for development.

Checkout a new branch named `add-test` using `git`.

```bash
git checkout -b add-test
```

## Write a test
The next step consists of converting the __main__ part of the code into a unit test.
    i. Create a new file called `test_times.py` in the same directory where `times.py` is.
   ii. Make the `calculate_fastest_time` function accessible to that file. (*Hint*: You need to `import` the file).
  iii. Move the content from the `if __name__ ...` block from `times.py` to a function called `test_given_input` into `test_times.py` and fill the gaps for `result` and `expected`. (For now, you can copy the output of the program as the expected value)
```python
def test_given_input():
    ...
    result = ...
    expected = ...
    assert result == expected
```

## Run the test
Run `pytest` on that directory and see whether the test is picked up by `pytest` and whether it passes. If the test doesn't pass, see if you can find what is going wrong.

## Submit a Pull Request
Once you have completed or made progress on the exercise, commit your changes, push them to your fork and open a pull request and ask for a review.

Create a **pull request (PR)** from your branch to `UCL-bioimage-analysis/rse-best-practices-playground` [using the GitHub web interface](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

Add a meaningful title to that PR and a link to this issue: `UCL-bioimage-analysis/rse-best-practices-playground#3`.

## [Optional 1] Write more tests for `calculate_fastest_time`
Do you see any other ways the method `calculate_fastest_time` could fail?
Try to test the ideas that came up in the Mentimeter discussion.

## [Optional 2] Review a Pull Request
Choose one of the other pull requests listed on this issue, and leave a review. Comment on things you find interesting or don't understand, any problems you think you spot, good solutions, or potential improvements.


## [Optional 3] Write more tests
If you have time, write docstrings for the other methods in `times.py` and submit separate new PR for each of them.

What do you expect the output of `compute_overlap_time` is for time ranges that do not overlap? Write another unit test function `test_no_overlap` that check this. Does `compute_overlap_time` work as expected in this case?
```python
def test_no_overlap():
    ...
    result = ...
    expected = ...
    assert result == expected
```
What other test cases for `compute_overlap_time` can you think of?
