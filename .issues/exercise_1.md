# Exercise 1
This exercise will look at write a test to check that it works as expected.

1. Install the playground as a developer (`".[dev]"`), in editable (`-e`) mode, by navigating into the `rse-best-practices-playground` folder and running
```bash
pip install -e ".[dev]"
```

2. The next step consists of converting the __main__ part of the code into a unit test.
    i. Create a new file called `test_times.py` in the same directory where `times.py` is.
   ii. Make the `overlap_time` function accessible to that file. (*Hint*: You need to `import` the file).
  iii. Move the content from the `if __name__ ...` block from `times.py` to a function called `test_given_input` into `test_times.py` and fill the gaps for `result` and `expected`. (For now, you can copy the output of the program as the expected value)
```python
def test_given_input():
    ...
    result = ...
    expected = ...
    assert result == expected
```
3. Run `pytest` on that directory and see whether the test is picked up by `pytest` and whether it passes. If the test doesn't pass, see if you can find what is going wrong.
4. When you are happy with your solution (or want some feedback!):
	  i. Push your new code to your own fork.
     ii. On GitHub, open a pull request from your fork to the original repository.
    iii. In the description, include the text `Answers neuroinformatics-unit/rse-best-practices-playground#1`. This will list your PR to this issue.
    iv. On the PR text, comment on what you found difficult or interesting, or something you learned.
5. Choose one of the other pull requests listed on this issue, and leave a review. Comment on things you find interesting or don't understand, any problems you think you spot, good solutions, or potential improvements.

6. (Optional) What do you expect the output of `compute_overlap_time` is for time ranges that do not overlap? Write another unit test function `test_no_overlap` that check this. Does `compute_overlap_time` work as expected in this case? 
```python
def test_no_overlap():
    ...
    result = ...
    expected = ...
    assert result == expected
```

7. (Optional) What other test cases for `compute_overlap_time` can you think of?