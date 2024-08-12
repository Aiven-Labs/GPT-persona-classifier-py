# Contributing

<!--toc:start-->

- [Contributing](#contributing)
  - [How to contribute to the project](#how-to-contribute-to-the-project)
    - [Issues](#issues)
      - [Things to include in your issue:](#things-to-include-in-your-issue)
    - [Discussions](#discussions)
  - [Updating the Codebase](#updating-the-codebase)
    - [Your Development Environment](#your-development-environment)
      - [DevContainers and GitHub Codespaces](#devcontainers-and-github-codespaces)
      - [Local Development](#local-development)
    - [Linting, Formatting, and Testing](#linting-formatting-and-testing)
      - [Linting and Formatting](#linting-and-formatting)
      - [Testing](#testing)
  - [PRs](#prs)
  <!--toc:end-->

## How to contribute to the project

### Issues

If you have a bug or an idea for a feature, it's best to file an issue. For your convenience, there are Issue templates available to help you provide the necessary information.

If you don't see a template that fits your issue, please select "Open blank issue".

#### Things to include in your issue:

- A clear and descriptive title
- A detailed description of the issue, feature, or bug
- Steps to reproduce the bug, or implement the feature
- System information (OS, Python Version, etc)
- Error Message (if applicable)

Don't let the list above intimidate you. The more information you provide, the easier it is for the maintainers to help you. If you don't have or know the information, that's okay too. Just provide as much as you can.

### Discussions

In most cases you won't need to start a discussion but an issue that requires a lot of conversation can be moved to a discussion. A new issue referencing the discussion will be created once a course of action is decided.

Discussions will also be the home where release updates will be posted.

## Updating the Codebase

This project uses the standard GitHub flow. To contribute, you will need to fork the repository, create a new branch, make your changes, and submit a pull request.

### Your Development Environment

#### DevContainers and GitHub Codespaces

For the best experience, we recommend the [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers) included in the project. This allows you to develop in a consistent environment with all the necessary tools and dependencies. It also allows you to use [GitHub Codespaces](https://code.visualstudio.com/docs/devcontainers/containers).

#### Local Development

If developing locally, you will need to do the following.

- [Install Python](https://www.python.org/downloads/) (preferrably the latest version but at least 3.10)
- Create a virtual environment (optional but recommended)

```sh
python -m venv .venv # .venv is the name of the virtual environment
```

- [activate the virtual environment](https://docs.python.org/3/library/venv.html) (instructions vary by OS)
- Install the dependencies

```sh
python -m pip install -r requirements.txt
```

Your environment is now set up and you can start developing.

### Linting, Formatting, and Testing

Before you can submit your PR, you will need to make sure that your code is properly formatted and passes the tests.

#### Linting and Formatting

This project uses [Ruff](ruff -i) to lint and format the code. The configuration for ruff is included in the `pyproject.toml`, so there is no need to make any configuration changes.

Many different editors support ruff but to run from the command line, you can use the following commands:

```sh
ruff check .
```

This will check for any formatting and linting issues. If you want to fix them, you can run:

```sh
ruff format .
```

#### Testing

This project uses [pytest](https://docs.pytest.org/en/stable/) for testing. To run the tests, you can use the following command:

```sh
python m pytest tests
```

## PRs

For your convenience, a PR template has been provided. That said if you are pushing your changes from outside the GH web interface, you will need to provide the following information:

- The issue number(s) this issue solves
- A summary of your changes:
  - What was added
  - What was removed
  - What was changed

Before submitting your PR make sure of the following:

- Your code is formatted with precommit
- Your code passes the tests
- New tests have been added
- New functions, classes, and modules have been documented with docstrings and type hints
