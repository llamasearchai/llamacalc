# Contributing to LlamaCalc

Thank you for your interest in contributing to LlamaCalc! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

Please read and follow our [Code of Conduct](https://github.com/llamasearch/llamacalc/blob/main/CODE_OF_CONDUCT.md) to help us maintain a healthy and inclusive community.

## How Can I Contribute?

There are many ways to contribute to LlamaCalc:

1. **Report Bugs**: If you find a bug, please create an issue using the bug report template.
2. **Suggest Features**: If you have an idea for a new feature, please create an issue using the feature request template.
3. **Improve Documentation**: Help us improve our documentation by fixing typos, adding examples, or clarifying explanations.
4. **Submit Pull Requests**: Contribute code to fix bugs or add new features.

## Development Setup

### Prerequisites

- Python 3.8 or higher
- Git

### Setting Up the Development Environment

1. Fork the repository on GitHub.
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/llamacalc.git
   cd llamacalc
   ```

3. Create a virtual environment and install development dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e ".[dev]"
   ```

### Running Tests

We use pytest for testing:

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=llamacalc

# Run specific tests
pytest tests/test_specific_file.py
```

## Pull Request Process

1. **Create a Branch**: Create a branch for your feature or bugfix.
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Changes**: Make your changes to the codebase. Be sure to follow our coding conventions.

3. **Add Tests**: Add tests for any new functionality or to reproduce and fix bugs.

4. **Update Documentation**: Update documentation to reflect any changes.

5. **Format Code**: Ensure your code is formatted according to our style guidelines.
   ```bash
   black src tests
   isort src tests
   flake8 src tests
   ```

6. **Run Tests**: Make sure all tests pass.
   ```bash
   pytest
   ```

7. **Commit Changes**: Commit your changes using a descriptive commit message.
   ```bash
   git commit -m "Add feature: your feature description"
   ```

8. **Push to GitHub**: Push your changes to your fork on GitHub.
   ```bash
   git push origin feature/your-feature-name
   ```

9. **Submit a Pull Request**: Create a pull request from your fork to the main repository.

## Coding Conventions

- Follow PEP 8 style guidelines
- Use descriptive variable and function names
- Write docstrings for all functions, classes, and modules
- Add type hints to function signatures
- Keep functions and methods small and focused on a single task
- Write comprehensive unit tests

## Documentation

We use MkDocs with the Material theme for our documentation. To build and view the documentation locally:

```bash
# Install documentation dependencies
pip install -r requirements-docs.txt

# Build the documentation
mkdocs build

# Serve the documentation locally
mkdocs serve
```

## Release Process

1. Update version number in `pyproject.toml`
2. Update changelog
3. Create a new release on GitHub
4. Publish to PyPI

## Getting Help

If you need help, feel free to:

- Open an issue on GitHub
- Join our community discussions on GitHub
- Contact the maintainers via email

## Thank You!

Thank you for contributing to LlamaCalc! Your time and expertise help make this project better for everyone. 