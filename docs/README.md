# LlamaCalc Documentation

This directory contains the source files for the LlamaCalc documentation. The documentation is built using [MkDocs](https://www.mkdocs.org/) with the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.

## Building the Documentation

To build and view the documentation locally:

1. Install the documentation dependencies:
```bash
pip install -r ../requirements-docs.txt
```

2. Serve the documentation:
```bash
cd .. && mkdocs serve
```

3. Open your web browser and navigate to `http://127.0.0.1:8000/`

## Documentation Structure

- `index.html`: Main landing page
- `getting_started.html`: Quick start guide
- `user_guide/`: Detailed usage instructions
  - `cli.html`: Command-line interface documentation
  - `scoring.html`: Information about scoring methodology
  - `performance.html`: Performance optimization tips
- `api/`: API reference documentation
  - `index.html`: API overview
- `examples/`: Example code and usage patterns
- `faq.html`: Frequently asked questions
- `contributing.html`: Contribution guidelines
- `license.html`: License information

## Adding or Updating Documentation

1. Edit the appropriate Markdown files in this directory
2. If adding a new page, update the `nav` section in `../mkdocs.yml`
3. Preview your changes using `mkdocs serve`
4. Commit your changes and create a pull request

## Documentation Style Guide

- Use clear, concise language
- Include code examples where appropriate
- Use proper Markdown formatting
- Break up large blocks of text with headers, lists, and code blocks
- Include screenshots or diagrams for complex concepts
- Keep code examples up-to-date with the latest API

## Building for Production

To build the documentation for production deployment:

```bash
cd .. && mkdocs build
```

This will generate a `site` directory with static HTML files that can be deployed to any web server.

## Documentation TODOs

- [ ] Add more examples for common use cases
- [ ] Create visualization guide for results
- [ ] Add performance benchmark results
- [ ] Create a troubleshooting section
- [ ] Add compatibility information for different Python versions 