# Git Minimal

Display a minimal maxim by The Minimalists after each git commit.

## Setup

To use the Python version (created in a Python 3.4 environment)
you will need to install some modules:

    pip install BeautifulSoup4 requests

## Install

Move the script into the hooks directory of the desired repo
and re-initialise:

    mv post-commit.py /path/to/repo/.git/hooks/post-commit
    cd /path/to/repo/
    git init

Note: There is no file extension when planted into the hooks directory.
It is just "post-commit".

### Global install

Set a global store of all the Git hooks like so:

    git config --global init.templatedir '/path/to/global/git_templates'
    mkdir -p /path/to/global/git_templates/hooks
    mv post-commit.py /path/to/global/git_templates/hooks/post-commit

To update existing repos, re-initialise:

    git init

The example command line instructions reference the Python script.
To use the Bash shell script instead, swap out
**post-commit.py** for **post-commit.sh**.

## License

[BSD 3-Clause](http://opensource.org/licenses/BSD-3-Clause)
