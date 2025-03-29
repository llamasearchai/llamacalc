# Command Line Interface

LlamaCalc provides a powerful command-line interface that allows you to evaluate answer relevance directly from your terminal. This document explains how to use this interface.

## Installation

Make sure LlamaCalc is installed with the UI components:

```bash
pip install llamacalc[ui]
```

The `ui` extra installs the [Rich](https://github.com/Textualize/rich) library, which provides a colorful and interactive terminal interface.

## Basic Usage

The command-line interface can be accessed using the `llamacalc` command:

```bash
# Display help information
llamacalc --help
```

This will show all available options and examples.

## Interactive Mode

The interactive mode provides a user-friendly way to evaluate answers:

```bash
llamacalc --interactive
```

In interactive mode, you'll be prompted to enter:
1. A question
2. An answer to evaluate

LlamaCalc will then calculate the relevance scores and display them in a colorful table, including:
- Total score
- Component scores (proximity, coverage, conciseness, logical flow)
- The contribution of each component to the total score
- Computation time

You can continue entering new question-answer pairs or quit at any time.

## Single Evaluation

To evaluate a single question-answer pair directly from the command line:

```bash
llamacalc --question "What is Python?" --answer "Python is a programming language."
```

You can also read the question and answer from files:

```bash
llamacalc --question-file question.txt --answer-file answer.txt
```

## Batch Processing

LlamaCalc can process multiple question-answer pairs at once using a JSON file:

```bash
llamacalc --batch-file qa_pairs.json
```

The JSON file should contain an array of objects with "question" and "answer" fields:

```json
[
  {
    "question": "What is Python?",
    "answer": "Python is a programming language."
  },
  {
    "question": "How does a neural network work?",
    "answer": "Neural networks process data through interconnected nodes."
  }
]
```

## Output Formats

By default, LlamaCalc outputs results in a human-readable text format. You can also get results in JSON format:

```bash
llamacalc --question "What is Python?" --answer "Python is a programming language." --json
```

To save the output to a file:

```bash
llamacalc --question "What is Python?" --answer "Python is a programming language." --output-file result.txt

# With JSON format
llamacalc --question "What is Python?" --answer "Python is a programming language." --json --output-file result.json
```

## Customizing Weights

You can customize the weights for different scoring components:

```bash
llamacalc --question "What is Python?" --answer "Python is a programming language." \
  --proximity-weight 0.4 \
  --coverage-weight 0.3 \
  --conciseness-weight 0.1 \
  --logical-flow-weight 0.2
```

The weights will be automatically normalized if they don't sum to 1.0.

## Docker Usage

If you have Docker installed, you can use the provided `docker-run.sh` script to run LlamaCalc:

```bash
# Make the script executable
chmod +x docker-run.sh

# Show help
./docker-run.sh --help

# Run in interactive mode
./docker-run.sh -i

# Process a batch file
./docker-run.sh -b ./data/qa_pairs.json
```

This script handles building the Docker image and mounting appropriate volumes.

## All Available Options

Here is a complete list of available command-line options:

### Input Options
- `--question`, `-q`: The question text
- `--answer`, `-a`: The answer text
- `--question-file`, `-qf`: File containing the question
- `--answer-file`, `-af`: File containing the answer
- `--batch-file`, `-bf`: JSON file with array of {question, answer} objects for batch processing

### Output Options
- `--json`, `-j`: Output in JSON format
- `--output-file`, `-o`: Write output to a file

### Mode Options
- `--interactive`, `-i`: Run in interactive mode

### Weight Options
- `--proximity-weight`: Weight for proximity score (default: 0.35)
- `--coverage-weight`: Weight for coverage score (default: 0.30)
- `--conciseness-weight`: Weight for conciseness score (default: 0.15)
- `--logical-flow-weight`: Weight for logical flow score (default: 0.20) 