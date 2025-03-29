# Getting Started with LlamaCalc

This guide will help you get up and running with LlamaCalc quickly. We'll cover installation, basic usage, and some common patterns.

## Installation

### Basic Installation

Install LlamaCalc from PyPI:

```bash
pip install llamacalc
```

### Installation with Optional Dependencies

For the best experience, especially on Apple Silicon Macs, install with all optional dependencies:

```bash
pip install "llamacalc[all]"
```

Or select specific optional dependencies:

```bash
# For UI enhancements (colorful CLI output)
pip install "llamacalc[ui]"

# For MLX acceleration on Apple Silicon
pip install "llamacalc[mlx]"

# For development tools
pip install "llamacalc[dev]"
```

### Using Docker

If you prefer Docker, pull and run the LlamaCalc image:

```bash
docker pull llamasearch/llamacalc:latest
docker run -it llamasearch/llamacalc
```

## Basic Usage

### Python API

The most common way to use LlamaCalc is through its Python API:

```python
from llamacalc import LlamaCalc

# Initialize with default settings
calc = LlamaCalc()

# Define reference and candidate texts
reference = "The quick brown fox jumps over the lazy dog."
candidate = "A brown fox quickly jumped over a dog that was lazy."

# Evaluate the candidate against the reference
result = calc.evaluate(candidate, reference)

# Print the results
print(f"Overall Score: {result.overall_score:.2f}")
print(f"Proximity Score: {result.proximity_score:.2f}")
print(f"Coverage Score: {result.coverage_score:.2f}")
print(f"Conciseness Score: {result.conciseness_score:.2f}")
print(f"Logical Flow Score: {result.logical_flow_score:.2f}")
```

### Command Line Interface

LlamaCalc also provides a user-friendly command-line interface:

```bash
llamacalc evaluate --candidate "A brown fox quickly jumped over a dog that was lazy." --reference "The quick brown fox jumps over the lazy dog."
```

Or use the interactive mode for multiple evaluations:

```bash
llamacalc interactive
```

## Customizing Evaluation

### Adjusting Component Weights

You can customize how much each scoring component contributes to the overall score:

```python
calc = LlamaCalc(
    proximity_weight=0.4,    # Emphasize semantic similarity
    coverage_weight=0.3,     # Moderate emphasis on concept coverage
    conciseness_weight=0.2,  # Some emphasis on brevity
    logical_flow_weight=0.1  # Less emphasis on structure
)
```

### Enabling Caching

For repeated evaluations of the same text, caching can significantly improve performance:

```python
# In-memory caching only
calc = LlamaCalc(use_cache=True)

# Persistent caching to disk
calc = LlamaCalc(use_cache=True, cache_dir="./llamacalc_cache")
```

### MLX Acceleration

On Apple Silicon (M1/M2/M3) Macs, LlamaCalc can use MLX for faster computation:

```python
# Explicitly enable MLX (enabled by default on Apple Silicon)
calc = LlamaCalc(use_mlx=True)

# Disable MLX if you encounter issues
calc = LlamaCalc(use_mlx=False)
```

## Batch Processing

For evaluating multiple text pairs at once:

```python
references = [
    "The Earth is the third planet from the Sun.",
    "Python is a high-level programming language."
]

candidates = [
    "Earth is positioned as the third planet in our solar system, counting from the Sun.",
    "Python refers to a programming language that is high-level and interpreted."
]

# Process multiple evaluations at once
results = calc.evaluate_batch(candidates, references)

# Print results
for i, result in enumerate(results):
    print(f"Example {i+1} Score: {result.overall_score:.2f}")
```

## Next Steps

Now that you're familiar with the basics of LlamaCalc, explore these topics to learn more:

- [Scoring Methodology](user_guide/scoring.md) - Learn how the different scores are calculated
- [Command Line Interface](user_guide/cli.md) - Detailed CLI usage
- [Advanced API](api/index.md) - Complete API reference
- [Examples](examples/index.md) - Example use cases and code samples
- [Performance Optimization](user_guide/performance.md) - Tips for optimal performance 