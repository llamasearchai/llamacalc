# LlamaCalc Standardization Plan

This document outlines the steps for standardizing the LlamaCalc repository to align with LlamaSearch.AI best practices.

## Current Status

LlamaCalc is an advanced relevance score calculator for evaluating how well an answer responds to a question. The repository currently has:

- Single Python file implementation (`llamacalc.py`)
- Basic test file (`test_llamacalc.py`)
- README and documentation
- Docker support
- Shell script for running the tool
- Basic GitHub setup

## Standardization Goals

1. **Modern Python Package Structure**: Convert from single-file to a proper package structure
2. **Documentation**: Create comprehensive documentation with MkDocs
3. **CI/CD Pipeline**: Set up GitHub Actions for testing, linting, and building
4. **Code Quality**: Improve code organization, docstrings, and type hints
5. **Package Registry Ready**: Prepare for PyPI publication
6. **Standardized Project Files**: Add or update files like CHANGELOG.md, CODE_OF_CONDUCT.md

## Implementation Plan

### 1. Package Restructuring (1 day)

- [x] Current structure: Single file `llamacalc.py`
- [ ] Create proper Python package structure:
  ```
  llamacalc/
  ├── src/
  │   └── llamacalc/
  │       ├── __init__.py
  │       ├── core.py         # Core calculation functions
  │       ├── ui.py           # UI components
  │       ├── utils.py        # Utility functions
  │       ├── cli.py          # Command-line interface
  │       └── cache.py        # Caching mechanisms
  ├── tests/
  │   ├── __init__.py
  │   ├── test_core.py
  │   ├── test_utils.py
  │   └── test_cache.py
  ├── docs/
  │   ├── index.md
  │   ├── getting-started.md
  │   ├── api-reference.md
  │   └── examples.md
  ├── examples/
  │   ├── basic_usage.py
  │   └── batch_processing.py
  ├── pyproject.toml        # Replace setup.py
  ├── README.md
  ├── CHANGELOG.md
  ├── CONTRIBUTING.md
  ├── CODE_OF_CONDUCT.md
  ├── LICENSE
  └── .gitignore
  ```

### 2. Update Core Dependencies (0.5 day)

- [ ] Create `pyproject.toml` with modern Python packaging
- [ ] Define proper dependencies with version constraints
- [ ] Set up optional dependencies (MLX, Rich)
- [ ] Configure development dependencies

### 3. Documentation Setup (1 day)

- [ ] Set up MkDocs with Material theme
- [ ] Create documentation structure
- [ ] Write comprehensive API documentation
- [ ] Add examples and tutorials
- [ ] Configure automatic documentation generation
- [ ] Update README with badges and links

### 4. CI/CD Pipeline (0.5 day)

- [ ] Create GitHub Actions workflow for:
  - Testing (pytest)
  - Linting (flake8, black, isort)
  - Type checking (mypy)
  - Documentation building
  - Package building
- [ ] Add status badges to README

### 5. Code Quality Improvements (1 day)

- [ ] Refactor functions into appropriate modules
- [ ] Improve code organization and maintainability
- [ ] Enhance docstrings (Google style)
- [ ] Add more comprehensive type hints
- [ ] Add logging
- [ ] Improve error handling
- [ ] Ensure consistent code style

### 6. PyPI Preparation (0.5 day)

- [ ] Verify package metadata in pyproject.toml
- [ ] Create package building script
- [ ] Test installation from built package
- [ ] Prepare for PyPI publishing

### 7. Standard Project Files (0.5 day)

- [ ] Create/update CODE_OF_CONDUCT.md using Contributor Covenant
- [ ] Create detailed CHANGELOG.md following Keep a Changelog format
- [ ] Review and update LICENSE file
- [ ] Review and update CONTRIBUTING.md
- [ ] Create SECURITY.md
- [ ] Update .gitignore

## Timeline

Total estimated time: 5 days

| Day | Tasks |
|-----|-------|
| 1 | Package restructuring, move code to appropriate modules |
| 2 | Update dependencies, set up CI/CD pipeline |
| 3 | Documentation setup, create API docs |
| 4 | Code quality improvements, refactoring |
| 5 | PyPI preparation, standard project files, final review |

## Completion Criteria

The standardization will be considered complete when:

1. Code is organized in a proper package structure
2. Documentation is comprehensive and follows standards
3. CI/CD pipeline successfully runs on all commits
4. All standard project files are in place and complete
5. Package can be installed via pip from PyPI
6. Code meets quality standards (linting, typing, testing)

## Post-Standardization Steps

1. Register package on PyPI
2. Create release notes for the first standardized version
3. Update repository in the standardization tracking documents 