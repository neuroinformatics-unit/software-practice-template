# Exercise 2
This exercise will show why it is important to keep documentation accurate, and how to do this automatically using docstrings and doctests.

## Setup
Make sure you've had a look at the course notes on [documentation](http://github-pages.ucl.ac.uk/rsd-engineeringcourse/ch04packaging/04documentation.html) so that you understand some of the background around docstrings and doctests. There you can also find how to use Sphinx to generate your website containing the docstrings of your methods. If you want more information you can find it in the [Sphinx docs](https://www.sphinx-doc.org/en/master/usage/quickstart.html).
We suggest using [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html), i.e. the Numpy style guide for docstrings.

## Exercises
### Write docstrings
The methods in `times.py` don't have a complete docstring. Based on your understanding of the methods, write a docstring using Numpy formatting. Describe what the method does, what are the inputs and the outputs.
You can change the examples later.

### Run doctests
Use the `doctest` module to see whether the documentation of the code is accurate: `python -m doctest times.py`.
Try to understand the structure of the output - what errors are reported, are they what you expected from looking at the code in the previous steps?

### Correct the examples in the docstrings
If there are errors, try to figure out where the mismatch between the documentation (intended behaviour) and the actual behaviour of the function exists.
Correct usage examples in the `times.py` function that are incorrect.
Do your example cover all the functionality described in the docstring?
Run again `python -m doctest times.py` to evaluate your new examples.

## Make your docs website
Thanks to the NIU `cookiecutter`, this repo contains the `docs/` folder the resources required to build a website using Sphinx.
Install the dev dependencies of the package to be able to run `sphinx-build`.
Update the `api_index.rst` file to include the methods in `times.py`.
Build the website using `sphinx-build docs/source docs/build`. The build folder contains the generated artefacts necessary for the website. By opening `index.html` you can navigate the website.
Does the website look as you expected?
Remember to delete the previous build folder before running again `shphinx-build`.

## Submit a Pull Request
Once you have completed or made progress on the exercises, open a pull request and ask for a review.

Create a pull request (PR) from your branch to the upstream repository. Add a meaningful title to that PR and a link to this issue: `Answers neuroinformatics-unit/rse-best-practices-playground#2`.
