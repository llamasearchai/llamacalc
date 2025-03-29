# Command Line Interface

LlamaCalc provides a powerful command-line interface (CLI) for direct interaction without writing Python code. The CLI offers all core functionality with a user-friendly, colorful interface.

## Installation

The CLI is automatically installed when you install LlamaCalc:

```bash
pip install llamacalc
```

## Basic Usage

### Evaluating Text

To evaluate a candidate text against a reference:

```bash
llamacalc evaluate --candidate "The quick brown fox jumps over the lazy dog." --reference "A brown fox quickly jumped over a dog that was lazy."
```

This will output the evaluation results with colorful formatting:

```
╭────────────── LlamaCalc Evaluation ──────────────╮
│                                                  │
│  Overall Score:     0.89                         │
│                                                  │
│  Component Scores:                               │
│    • Proximity:     0.92                         │
│    • Coverage:      0.95                         │
│    • Conciseness:   0.85                         │
│    • Logical Flow:  0.84                         │
│                                                  │
╰──────────────────────────────────────────────────╯
```

### Interactive Mode

For multiple evaluations in a row, use interactive mode:

```bash
llamacalc interactive
```

This will start an interactive session where you can input candidate and reference texts and see results immediately.

### Reading from Files

To evaluate text from files:

```bash
llamacalc evaluate --candidate-file candidate.txt --reference-file reference.txt
```

### Batch Processing

To process multiple evaluations in batch mode:

```bash
llamacalc batch --input evaluations.json --output results.json
```

Where `evaluations.json` might look like:

```json
[
  {
    "candidate": "The quick brown fox jumps over the lazy dog.",
    "reference": "A brown fox quickly jumped over a dog that was lazy."
  },
  {
    "candidate": "Python is a programming language.",
    "reference": "Python is a high-level, interpreted programming language."
  }
]
```

## Advanced Options

### Customizing Weights

You can customize the weights of different scoring components:

```bash
llamacalc evaluate --candidate "..." --reference "..." \
  --proximity-weight 0.3 \
  --coverage-weight 0.3 \
  --conciseness-weight 0.2 \
  --logical-flow-weight 0.2
```

### Output Formats

LlamaCalc supports various output formats:

```bash
# Pretty human-readable output (default)
llamacalc evaluate --candidate "..." --reference "..." --format pretty

# JSON output
llamacalc evaluate --candidate "..." --reference "..." --format json

# CSV output
llamacalc evaluate --candidate "..." --reference "..." --format csv

# Minimal output (just the overall score)
llamacalc evaluate --candidate "..." --reference "..." --format minimal
```

### Caching

Enable caching to speed up repeated evaluations:

```bash
llamacalc evaluate --candidate "..." --reference "..." --cache

# Specify a cache directory
llamacalc evaluate --candidate "..." --reference "..." --cache --cache-dir "./cache"
```

### Verbosity

Control the verbosity of output:

```bash
# Detailed output with component calculations
llamacalc evaluate --candidate "..." --reference "..." --verbose

# Quieter output with only the final result
llamacalc evaluate --candidate "..." --reference "..." --quiet
```

## Full Command Reference

### Global Options

These options work with all commands:

- `--help`: Show help message
- `--version`: Show version information
- `--quiet`: Reduce output verbosity
- `--verbose`: Increase output verbosity
- `--no-color`: Disable colored output
- `--cache`: Enable caching
- `--cache-dir PATH`: Set cache directory
- `--format FORMAT`: Set output format (pretty, json, csv, minimal)

### Evaluate Command

```bash
llamacalc evaluate [OPTIONS]
```

Options:
- `--candidate TEXT`: Candidate text to evaluate
- `--reference TEXT`: Reference text to compare against
- `--candidate-file PATH`: File containing candidate text
- `--reference-file PATH`: File containing reference text
- `--proximity-weight FLOAT`: Weight for proximity score (default: 0.25)
- `--coverage-weight FLOAT`: Weight for coverage score (default: 0.25)
- `--conciseness-weight FLOAT`: Weight for conciseness score (default: 0.25)
- `--logical-flow-weight FLOAT`: Weight for logical flow score (default: 0.25)
- `--output PATH`: Save results to file

### Batch Command

```bash
llamacalc batch [OPTIONS]
```

Options:
- `--input PATH`: Input JSON file with evaluation pairs
- `--output PATH`: Output file for results
- `--proximity-weight FLOAT`: Weight for proximity score (default: 0.25)
- `--coverage-weight FLOAT`: Weight for coverage score (default: 0.25)
- `--conciseness-weight FLOAT`: Weight for conciseness score (default: 0.25)
- `--logical-flow-weight FLOAT`: Weight for logical flow score (default: 0.25)

### Interactive Command

```bash
llamacalc interactive [OPTIONS]
```

Options:
- `--proximity-weight FLOAT`: Weight for proximity score (default: 0.25)
- `--coverage-weight FLOAT`: Weight for coverage score (default: 0.25)
- `--conciseness-weight FLOAT`: Weight for conciseness score (default: 0.25)
- `--logical-flow-weight FLOAT`: Weight for logical flow score (default: 0.25)
- `--history PATH`: Save/load session history to/from file 