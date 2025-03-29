# Contributing to LlamaCalc

Thank you for your interest in contributing to LlamaCalc! This document provides guidelines and instructions for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Feature Requests](#feature-requests)
  - [Code Contributions](#code-contributions)
- [Development Workflow](#development-workflow)
  - [Setting Up Your Environment](#setting-up-your-environment)
  - [Running Tests](#running-tests)
  - [Style Guidelines](#style-guidelines)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md) to keep our community welcoming, respectful, and productive.

## Getting Started

1. **Fork the repository** on GitHub.
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/llamacalc.git
   cd llamacalc
   ```
3. **Set up the development environment**:
   ```bash
   # Create a virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install development dependencies
   pip install -e ".[dev]"
   ```

## How to Contribute

### Reporting Bugs

Before submitting a bug report:
- Check the issue tracker to avoid duplicates
- Try the latest version to see if the issue has been fixed

When reporting bugs, please include:
- A clear and descriptive title
- Steps to reproduce the behavior
- Expected behavior
- Actual behavior
- Environment information (OS, Python version, package versions)
- Any relevant logs or screenshots

### Feature Requests

When suggesting a new feature, please:
- Provide a clear and detailed explanation of the feature
- Explain why this feature would be useful to LlamaCalc users
- Consider how it fits into the existing architecture
- If possible, suggest an implementation approach

### Code Contributions

1. Make sure there's an issue for what you're working on
2. Discuss your approach in the issue before starting significant work
3. Follow the coding style of the project
4. Write tests for your changes
5. Document any new functionality

## Development Workflow

### Setting Up Your Environment

We recommend using a virtual environment for development:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt  # For development dependencies
```

### Running Tests

Before submitting a pull request, run the test suite:

```bash
python -m unittest discover
```

### Style Guidelines

- Follow PEP 8 style guidelines
- Use docstrings for all functions, classes, and modules
- Keep line length to 100 characters or less
- Use type annotations where appropriate

## Commit Message Guidelines

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `style:` for formatting changes
- `refactor:` for code refactoring
- `test:` for tests
- `chore:` for routine tasks, maintenance, etc.

Example: `feat: Add caching for relevance calculations`

## Pull Request Process

1. Ensure your PR addresses a specific issue. If no issue exists, create one first.
2. Update documentation if your changes require it.
3. Add tests for new features or bug fixes.
4. Make sure all tests, linters, and type checkers pass.
5. Fill out the PR template completely.
6. Request a review from one of the maintainers.

## Reporting Bugs

When reporting bugs, please include:

- A clear and descriptive title
- Steps to reproduce the behavior
- Expected behavior
- Actual behavior
- Environment information (OS, Python version, package versions)
- Any relevant logs or screenshots

## Feature Requests

When suggesting a new feature, please:

- Provide a clear and detailed explanation of the feature
- Explain why this feature would be useful to LlamaCalc users
- Consider how it fits into the existing architecture
- If possible, suggest an implementation approach

## Code Style Guidelines

We follow these code style guidelines:

- Use [Black](https://black.readthedocs.io/) for code formatting with a line length of 88 characters
- Use [isort](https://pycqa.github.io/isort/) for sorting imports
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Use [Google style docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
- Use type hints according to [PEP 484](https://www.python.org/dev/peps/pep-0484/)

## Testing Guidelines

- Write unit tests for all new functionality
- Ensure tests are isolated and don't depend on external services
- Use pytest for testing
- Aim for high test coverage, especially for complex logic

## Git Commit Guidelines

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification for commit messages:

```
<type>(<scope>): <short description>

<optional body>

<optional footer>
```

Types include:
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

Example:
```
feat(scoring): add support for custom weighting profiles

Add the ability to create and save named weighting profiles for different 
evaluation scenarios.

Closes #42
```

## Release Process

LlamaCalc follows [Semantic Versioning](https://semver.org/):

- MAJOR version for incompatible API changes
- MINOR version for backwards-compatible new functionality
- PATCH version for backwards-compatible bug fixes

The release process is as follows:

1. Update version number in `src/llamacalc/__init__.py`
2. Update CHANGELOG.md with the changes since last release
3. Create a pull request for the version bump
4. Once merged, create a new release tag in GitHub
5. CI will automatically publish the package to PyPI

## Documentation

- Update documentation for any public API changes
- Use clear, concise language
- Include examples for new features
- Keep the README.md up to date

## Questions?

If you have any questions, feel free to open an issue or contact the maintainers directly.

Thank you for contributing to LlamaCalc! 🦙 