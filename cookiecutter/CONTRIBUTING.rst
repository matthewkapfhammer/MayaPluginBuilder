============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given. 

.. toctree::
   :numbered:
   :maxdepth: 2

   types_of_contributions
   contributor_setup
   contributor_guidelines
   contributor_testing
   core_committer_guide

Types of Contributions
----------------------

You can contribute in many ways:

Create Cookiecutter Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some other Cookiecutter templates to list in the :ref:`README <readme>` would
be great.

If you create a Cookiecutter template, submit a pull request adding it to
README.rst.

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/audreyr/cookiecutter/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* If you can, provide detailed steps to reproduce the bug.
* If you don't have steps to reproduce the bug, just note your observations in
  as much detail as you can. Questions to start a discussion about the issue
  are welcome.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
is open to whoever wants to implement it.

Please do not combine multiple feature enhancements into a single pull request.

Note: this project is a bit conservative, so new features might not get into core.
If possible, it's best to try and implement feature ideas as separate projects
outside of the core codebase.

Write Documentation
~~~~~~~~~~~~~~~~~~~

Cookiecutter could always use more documentation, whether as part of the
official Cookiecutter docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at
https://github.com/audreyr/cookiecutter/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Setting Up the Code for Local Development
-----------------------------------------

Here's how to set up `cookiecutter` for local development.

1. Fork the `cookiecutter` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/cookiecutter.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv cookiecutter
    $ cd cookiecutter/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

Now you can make your changes locally.

5. When you're done making changes, check that your changes pass the tests and flake8::

    $ flake8 cookiecutter tests
    $ python setup.py test
    $ tox

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Check that the test coverage hasn't dropped::

    coverage run --source cookiecutter setup.py test
    coverage report -m
    coverage html

8. Submit a pull request through the GitHub website.
Contributor Guidelines
-----------------------

Pull Request Guidelines
~~~~~~~~~~~~~~~~~~~~~~~~

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 2.6, 2.7, 3.3, and PyPy on Appveyor and Travis CI.
4. Check https://travis-ci.org/audreyr/cookiecutter/pull_requests and 
   https://ci.appveyor.com/project/audreyr/cookiecutter/history to ensure the tests pass for all supported Python versions and platforms.

Coding Standards
~~~~~~~~~~~~~~~~

* PEP8
* Functions over classes except in tests
* Prefer single quotes (unless inconvenient) http://stackoverflow.com/a/56190/5549

Testing
-------

To run a particular test::

    $ python -m unittest tests.test_find.TestFind.test_find_template

To run a subset of tests::

    $ python -m unittest tests.test_find

Testing with py.test
--------------------

To run a particular test class with py.test::

    $ py.test -k TestGetConfig

To run some tests with names matching a string expression::

    $ py.test -k generate

Will run all tests matching "generate", test_generate_files for example.

To run just one method::

    $ py.test -k TestGetConfig::test_get_config


To run all tests using various versions of python in virtualenvs defined in tox.ini, just run tox.::

    $ tox

This configuration file setup the pytest-cov plugin and it is an additional
dependency. It generate a coverage report after the tests.

It is possible to tests with some versions of python, to do this the command
is::

    $ tox -e py27,py34,pypy

Will run py.test with the python2.7, python3.4 and pypy interpreters, for
example.

Troubleshooting for Contributors
---------------------------------

Python 3.3 tests fail locally
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Try upgrading Tox to the latest version. I noticed that they were failing
locally with Tox 1.5 but succeeding when I upgraded to Tox 1.7.1.


Core Committer Guide
====================

Vision and Scope
-----------------

Core committers, use this section to:

* Guide your instinct and decisions as a core committer
* Limit the codebase from growing infinitely

Command-Line Accessible
~~~~~~~~~~~~~~~~~~~~~~~

* Provides a command-line utility that creates projects from cookiecutters
* Extremely easy to use without having to think too hard
* Flexible for more complex use via optional arguments

API Accessible
~~~~~~~~~~~~~~

* Entirely function-based and stateless (Class-free by intentional design)
* Usable in pieces for developers of template generation tools

Being Jinja2-specific
~~~~~~~~~~~~~~~~~~~~~

* Sets a standard baseline for project template creators, facilitating reuse
* Minimizes the learning curve for those who already use Flask or Django
* Minimizes scope of Cookiecutter codebase

Extensible
~~~~~~~~~~

Being extendable by people with different ideas for Jinja2-based project template tools.

* Entirely function-based
* Aim for statelessness
* Lets anyone write more opinionated tools

Freedom for Cookiecutter users to build and extend.

* No officially-maintained cookiecutter templates, only ones by individuals
* Commercial project-friendly licensing, allowing for private cookiecutters and private Cookiecutter-based tools

Fast and Focused
~~~~~~~~~~~~~~~~

Cookiecutter is designed to do one thing, and do that one thing very well.

* Cover the use cases that the core committers need, and as little as possible beyond that :)
* Generates project templates from the command-line or API, nothing more
* Minimize internal line of code (LOC) count
* Ultra-fast project generation for high performance downstream tools

Inclusive
~~~~~~~~~

* Cross-platform and cross-version support are more important than features/functionality
* Fixing Windows bugs even if it's a pain, to allow for use by more beginner coders

Stable
~~~~~~

* Aim for 100% test coverage and covering corner cases
* No pull requests will be accepted that drop test coverage on any platform, including Windows
* Conservative decisions patterned after CPython's conservative decisions with stability in mind
* Stable APIs that tool builders can rely on
* New features require a +1 from 3 core committers

VCS-Hosted Templates
~~~~~~~~~~~~~~~~~~~~~

Cookiecutter project templates are intentionally hosted VCS repos as-is.

* They are easily forkable
* It's easy for users to browse forks and files
* They are searchable via standard Github/Bitbucket/other search interface
* Minimizes the need for packaging-related cruft files
* Easy to create a public project template and host it for free
* Easy to collaborate

Process: Pull Requests
------------------------

If a pull request is untriaged:

* Look at the roadmap
* Set it for the milestone where it makes the most sense
* Add it to the roadmap

How to prioritize pull requests, from most to least important:

#. Fixes for broken tests. Broken means broken on any supported platform or Python version.
#. Extra tests to cover corner cases.
#. Minor edits to docs.
#. Bug fixes.
#. Major edits to docs.
#. Features.

Ensure that each pull request meets all requirements in this checklist:
https://gist.github.com/audreyr/4feef90445b9680475f2

Process: Issues
----------------

If an issue is a bug that needs an urgent fix, mark it for the next patch release.
Then either fix it or mark as please-help.

For other issues: encourage friendly discussion, moderate debate, offer your thoughts.

New features require a +1 from 2 other core committers (besides yourself).

Process: Roadmap
-----------------

The roadmap is https://github.com/audreyr/cookiecutter/milestones?direction=desc&sort=due_date&state=open

Due dates are flexible. Core committers can change them as needed. Note that GitHub sort on them is buggy.

How to number milestones:

* Follow semantic versioning. See http://semver.org

Milestone size:

* If a milestone contains too much, move some to the next milestone.
* Err on the side of more frequent patch releases.

Process: Generating CONTRIBUTING.rst
-------------------------------------

From the `cookiecutter` project root::

    $ make contributing

This will generate the following message::

    rm CONTRIBUTING.rst
    touch CONTRIBUTING.rst
    cat docs/contributing.rst >> CONTRIBUTING.rst
    echo "\r\r" >> CONTRIBUTING.rst
    cat docs/types_of_contributions.rst >> CONTRIBUTING.rst
    echo "\r\r" >> CONTRIBUTING.rst
    cat docs/contributor_setup.rst >> CONTRIBUTING.rst
    echo "\r\r" >> CONTRIBUTING.rst
    cat docs/contributor_guidelines.rst >> CONTRIBUTING.rst
    echo "\r\r" >> CONTRIBUTING.rst
    cat docs/contributor_tips.rst >> CONTRIBUTING.rst
    echo "\r\r" >> CONTRIBUTING.rst
    cat docs/core_committer_guide.rst >> CONTRIBUTING.rst
    echo "\r\rAutogenerated from the docs via \`make contributing\`" >> CONTRIBUTING.rst
    echo "WARNING: Don't forget to replace any :ref: statements with literal names"
    WARNING: Don't forget to replace any :ref: statements with literal names

Process: Your own code changes
-------------------------------

All code changes, regardless of who does them, need to be reviewed and merged by someone else.
This rule applies to all the core committers.

Exceptions:

* Minor corrections and fixes to pull requests submitted by others.
* While making a formal release, the release manager can make necessary, appropriate changes.
* Small documentation changes that reinforce existing subject matter. Most commonly being, but not limited to spelling and grammar corrections.

Responsibilities
-----------------

#. Ensure cross-platform compatibility for every change that's accepted. Windows, Mac, Debian & Ubuntu Linux.
#. Ensure that code that goes into core meets all requirements in this checklist: https://gist.github.com/audreyr/4feef90445b9680475f2
#. Create issues for any major changes and enhancements that you wish to make. Discuss things transparently and get community feedback.
#. Don't add any classes to the codebase unless absolutely needed. Err on the side of using functions.
#. Keep feature versions as small as possible, preferably one new feature per version.
#. Be welcoming to newcomers and encourage diverse new contributors from all backgrounds. See the Python Community Code of Conduct (https://www.python.org/psf/codeofconduct/).

Becoming a Core Committer
--------------------------

Contributors may be given core commit privileges. Preference will be given to those with:

A. Past contributions to Cookiecutter and other open-source projects. Contributions to Cookiecutter include both code (both accepted and pending) and friendly participation in the issue tracker. Quantity and quality are considered.
B. A coding style that the other core committers find simple, minimal, and clean.
C. Access to resources for cross-platform development and testing.
D. Time to devote to the project regularly.
Autogenerated from the docs via `make contributing`
