# Exercise 1
This exercise will look at understanding what a given python function (`times.py`) does, and writing a test to check that it works as expected.

1. Fork this repository repository and clone it on your computer.
2. Make sure you have read the note chapters on [Testing basics](https://github-pages.ucl.ac.uk/rsd-engineeringcourse/ch03tests/01testingbasics.html), [The Fields of Saskatchewan](https://github-pages.ucl.ac.uk/rsd-engineeringcourse/ch03tests/02SaskatchewanFields.html) and [Test frameworks](https://github-pages.ucl.ac.uk/rsd-engineeringcourse/ch03tests/03pytest.html).
3. Start by reading the code in `times.py`, understanding what it does, and running it (before making any modifications to it).
	i. Have you seen [`datetime`](https://docs.python.org/3.7/library/datetime.html) before?
   ii. Play using your favourite tool (notebook, terminal, scripts) with the functions and objects used in `times.py`.
5. The next step consists of converting the __main__ part of the code into a unit test.
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
7. Run `pytest` on that directory and see whether the test is picked up by `pytest` and whether it passes. If the test doesn't pass, see if you can find what is going wrong.
8. When you are happy with your solution (or want some feedback!):
	  i. Push your new code to your own fork.
     ii. On GitHub, open a pull request from your fork to the original repository.
    iii. In the description, include the text `Answers neuroinformatics-unit/rse-best-practices-playground#1`. This will list your PR to this issue.
    iv. On the PR text, comment on what you found difficult or interesting, or something you learned.
9. Choose one of the other pull requests listed on this issue, and leave a review. Comment on things you find interesting or don't understand, any problems you think you spot, good solutions, or potential improvements.
10. Mark the assignment on Moodle as complete.
11. Think about what other aspects of `times.py` should be tested and report them on the Moodle questionnaire.

If you have questions or get stuck, ask on Moodle or book an office hours slot!
