==============
Advanced Usage
==============

Using Pre/Post-Generate Hooks (0.7.0+)
--------------------------------------

You can have Python or Shell scripts that run before and/or after your project
is generated.

Put them in `hooks/` like this::

    cookiecutter-something/
    ├── {{cookiecutter.repo_name}}/
    ├── hooks
    │   ├── pre_gen_project.py
    │   └── post_gen_project.py
    └── cookiecutter.json

Shell scripts work similarly::

    cookiecutter-something/
    ├── {{cookiecutter.repo_name}}/
    ├── hooks
    │   ├── pre_gen_project.sh
    │   └── post_gen_project.sh
    └── cookiecutter.json

It shouldn't be too hard to extend Cookiecutter to work with other types of
scripts too. Pull requests are welcome.

For portability, you should use Python scripts (with extension `.py`) for your
hooks, as these can be run on any platform. However, if you intend for your
template to only be run on a single platform, a shell script (or `.bat` file
on Windows) can be a quicker alternative.

User Config (0.7.0+)
----------------------

If you use Cookiecutter a lot, you'll find it useful to have a
`.cookiecutterrc` file in your home directory like this:

.. code-block:: yaml

    default_context:
        full_name: "Audrey Roy"
        email: "audreyr@gmail.com"
        github_username: "audreyr"
    cookiecutters_dir: "/home/audreyr/my-custom-cookiecutters-dir/"
    abbreviations:
        pp: https://github.com/audreyr/cookiecutter-pypackage.git
        gh: https://github.com/{0}.git
        bb: https://bitbucket.org/{0}

Possible settings are:

* default_context: A list of key/value pairs that you want injected as context
  whenever you generate a project with Cookiecutter. These values are treated
  like the defaults in `cookiecutter.json`, upon generation of any project.
* cookiecutters_dir: Directory where your cookiecutters are cloned to when you
  use Cookiecutter with a repo argument.
* abbreviations: A list of abbreviations for cookiecutters. Abbreviations can
  be simple aliases for a repo name, or can be used as a prefix, in the form
  `abbr:suffix`. Any suffix will be inserted into the expansion in place of
  the text `{0}`, using standard Python string formatting.  With the above
  aliases, you could use the `cookiecutter-pypackage` template simply by saying
  `cookiecutter pp`, or `cookiecutter gh:audreyr/cookiecutter-pypackage`.
  The `gh` (github) and `bb` (bitbucket) abbreviations shown above are actually
  built in, and can be used without defining them yourself.

Calling Cookiecutter Functions From Python
------------------------------------------

You can use Cookiecutter from Python::

    from cookiecutter.main import cookiecutter

    # Create project from the cookiecutter-pypackage/ template
    cookiecutter('cookiecutter-pypackage/')

    # Create project from the cookiecutter-pypackage.git repo template
    cookiecutter('https://github.com/audreyr/cookiecutter-pypackage.git')

This is useful if, for example, you're writing a web framework and need to
provide developers with a tool similar to `django-admin.py startproject` or
`npm init`.

Injecting Extra Context
-----------------------

You can specify an `extra_context` dictionary that will override values from `cookiecutter.json` or `.cookiecutterrc`::

    cookiecutter('cookiecutter-pypackage/',
                 extra_context={'project_name': 'TheGreatest'})

Example: Injecting a Timestamp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a sample Python script that dynamically injects a timestamp value
as a project is generated::

    from cookiecutter.main import cookiecutter

    from datetime import datetime

    cookiecutter(
        'cookiecutter-django',
        extra_context={'timestamp': datetime.utcnow().isoformat()}
    )

How this works:

1. The script uses `datetime` to get the current UTC time in ISO format.
2. To generate the project, `cookiecutter()` is called, passing the timestamp
   in as context via the `extra_context` dict.

Suppressing Command-Line Prompts
--------------------------------

To suppress the prompts asking for input, use `no_input`.

Basic Example: Using the Defaults
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TODO: document `no_input`:

* As command-line argument
* As parameter of `cookiecutter()`

TODO: document where context values come from in this example (`cookiecutter.json` and `.cookiecutterrc`)

Advanced Example: Defaults + Extra Context
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you combine an `extra_context` dict with the `no_input` argument, you can programmatically create the project with a set list of context parameters and without any command line prompts::

    cookiecutter('cookiecutter-pypackage/',
                 no_input=True,
                 extra_context={'project_name': 'TheGreatest'})

See the :ref:`API Reference <apiref>` for more details.

Templates in Context Values
--------------------------------

The values (but not the keys!) of `cookiecutter.json` are also Jinja2 templates.
Values from user prompts are added to the context immediately, such that one
context value can be derived from previous values. This approach can potentially
save your user a lot of keystrokes by providing more sensible defaults.

Basic Example: Templates in Context
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python packages show some patterns for their naming conventions:

* a human-readable project name
* a lowercase, dashed repository name
* an importable, dash-less package name

Here is a `cookiecuttter.json` with templated values for this pattern::

    {
      "project_name": "My New Project",
      "repo_name": "{{ cookiecutter.project_name|lower|replace(' ', '-') }}",
      "pkg_name": "{{ cookiecutter.repo_name|replace('-', '') }}"
    }

If the user takes the defaults, or uses `no_input`, the templated values will 
be:

* `my-new-project`
* `mynewproject`

Or, if the user gives `Yet Another New Project`, the values will be:

* `yet-another-new-project`
* `yetanothernewproject`

Copy without Render
-------------------

*New in Cookiecutter 1.1*

To avoid rendering directories and files of a cookiecutter mould, the `_copy_without_render` key can be used in the `cookiecutter.json`. The value of this key accepts a list of Unix shell-style wildcards::

    {
        "repo_name": "sample",
        "_copy_without_render": [
            "*.html",
            "*not_rendered_dir",
            "rendered_dir/not_rendered_file.ini"
        ]
    }

.. _command_line_options:

Command Line Options
--------------------

.. cc-command-line-options::


