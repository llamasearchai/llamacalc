# API Reference

This section provides detailed documentation for LlamaCalc's Python API. LlamaCalc is designed to be simple to use while offering flexibility for advanced use cases.

## Core Classes

### LlamaCalc

The main class for evaluating text relevance.

```python
from llamacalc import LlamaCalc

calc = LlamaCalc(
    proximity_weight=0.25,
    coverage_weight=0.25,
    conciseness_weight=0.25,
    logical_flow_weight=0.25,
    use_cache=True,
    cache_dir=None,
    use_mlx=True,
    verbose=False
)
```

**Parameters:**

- `proximity_weight` (float, default=0.25): Weight for the proximity score component
- `coverage_weight` (float, default=0.25): Weight for the coverage score component
- `conciseness_weight` (float, default=0.25): Weight for the conciseness score component
- `logical_flow_weight` (float, default=0.25): Weight for the logical flow score component
- `use_cache` (bool, default=True): Whether to cache results to speed up repeated evaluations
- `cache_dir` (str, optional): Directory to store persistent cache (if None, uses in-memory cache only)
- `use_mlx` (bool, default=True): Whether to use MLX acceleration on Apple Silicon (falls back to NumPy if unavailable)
- `verbose` (bool, default=False): Whether to print verbose output during evaluation

**Methods:**

- `evaluate(candidate, reference)`: Evaluate a single candidate text against a reference
- `evaluate_batch(candidates, references)`: Evaluate multiple candidate texts against multiple references
- `clear_cache()`: Clear the evaluation cache

### RelevanceResult

Class containing the results of a relevance evaluation.

**Attributes:**

- `overall_score` (float): Combined weighted score from all components
- `proximity_score` (float): Score measuring how closely the candidate matches the reference
- `coverage_score` (float): Score measuring how well the candidate covers key concepts
- `conciseness_score` (float): Score measuring how efficiently information is presented
- `logical_flow_score` (float): Score measuring structure and coherence
- `metadata` (dict): Additional information about the evaluation

**Methods:**

- `to_dict()`: Convert the result to a dictionary
- `__str__()`: String representation of the results
- `__repr__()`: Detailed string representation of the results

## Utility Classes

### LlamaCache

Handles caching of evaluation results.

```python
from llamacalc.cache import LlamaCache

cache = LlamaCache(persistent=True, cache_dir="./cache")
```

**Parameters:**

- `persistent` (bool, default=False): Whether to store cache on disk
- `cache_dir` (str, optional): Directory for persistent cache storage

**Methods:**

- `get(key)`: Get a cached value by key
- `set(key, value)`: Set a cached value by key
- `clear()`: Clear all cached values
- `contains(key)`: Check if key exists in cache

### TextProcessor

Handles text preprocessing for evaluation.

```python
from llamacalc.processors import TextProcessor

processor = TextProcessor(lowercase=True, remove_punctuation=True)
processed_text = processor.process("Example text.")
```

**Parameters:**

- `lowercase` (bool, default=True): Whether to convert text to lowercase
- `remove_punctuation` (bool, default=True): Whether to remove punctuation
- `remove_stopwords` (bool, default=False): Whether to remove stop words
- `stem_words` (bool, default=False): Whether to apply stemming

## Scoring Modules

### ProximityScorer

Calculates how closely a candidate text matches a reference.

```python
from llamacalc.scorers import ProximityScorer

scorer = ProximityScorer()
score = scorer.calculate(candidate_text, reference_text)
```

### CoverageScorer

Calculates how well a candidate text covers key concepts from the reference.

```python
from llamacalc.scorers import CoverageScorer

scorer = CoverageScorer()
score = scorer.calculate(candidate_text, reference_text)
```

### ConcisenessScorer

Calculates how efficiently information is presented in the candidate text.

```python
from llamacalc.scorers import ConcisenessScorer

scorer = ConcisenessScorer()
score = scorer.calculate(candidate_text, reference_text)
```

### LogicalFlowScorer

Calculates the structure and coherence of the candidate text.

```python
from llamacalc.scorers import LogicalFlowScorer

scorer = LogicalFlowScorer()
score = scorer.calculate(candidate_text, reference_text)
```

## Command Line Interface

LlamaCalc also provides a command-line interface for quick evaluations.

```bash
llamacalc evaluate --candidate "Example candidate text" --reference "Example reference text"
```

For more details on the CLI, see the [Command Line Interface](../user_guide/cli.md) documentation. 