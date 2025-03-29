# Frequently Asked Questions

## General Questions

### What is LlamaCalc?

LlamaCalc is an advanced relevance score calculator designed to evaluate the quality of answers based on multiple factors including proximity to reference answers, concept coverage, conciseness, and logical flow. It's particularly useful for benchmarking and evaluating LLM outputs.

### Why should I use LlamaCalc?

LlamaCalc provides a more nuanced evaluation of text quality than simple metrics like BLEU or ROUGE. It analyzes multiple dimensions of quality and combines them into a meaningful score that aligns better with human judgment.

### Is LlamaCalc free to use?

Yes, LlamaCalc is open-source software released under the MIT License, making it free to use, modify, and distribute.

## Technical Questions

### What platforms does LlamaCalc support?

LlamaCalc is written in Python and supports all major operating systems including Windows, macOS, and Linux. It has special optimizations for Apple Silicon (M1/M2/M3) Macs using the MLX framework.

### Does LlamaCalc require a GPU?

No, LlamaCalc does not require a GPU to run. It uses efficient CPU-based computations by default. On Apple Silicon Macs, it leverages the specialized ML hardware through MLX for better performance.

### How accurate is LlamaCalc's scoring?

LlamaCalc's scoring has been validated against human evaluations and shows strong correlation with human judgment. However, no automated metric is perfect, and the scores should be used as a helpful guide rather than an absolute measure of quality.

### Can I customize the scoring weights?

Yes, you can customize the relative importance of different scoring factors (proximity, coverage, conciseness, and logical flow) by adjusting the weights when initializing the `LlamaCalc` class:

```python
from llamacalc import LlamaCalc

calc = LlamaCalc(
    proximity_weight=0.3,
    coverage_weight=0.4,
    conciseness_weight=0.2,
    logical_flow_weight=0.1
)
```

## Installation Questions

### Why am I getting an MLX import error?

If you see an error related to MLX, it's likely because you're using a non-Apple Silicon Mac or a different operating system. MLX is only supported on Apple Silicon (M1/M2/M3) Macs. LlamaCalc will automatically fall back to NumPy-based calculations on other platforms.

### How do I install LlamaCalc with all optional dependencies?

To install LlamaCalc with all optional dependencies, use:

```bash
pip install "llamacalc[all]"
```

### Can I use LlamaCalc in Docker?

Yes, LlamaCalc provides a Docker image that includes all dependencies. To use it:

```bash
docker pull llamasearch/llamacalc:latest
docker run -it llamasearch/llamacalc
```

## Usage Questions

### How do I evaluate multiple answers at once?

You can use the batch evaluation feature:

```python
from llamacalc import LlamaCalc

calc = LlamaCalc()

references = [
    "The Earth orbits the Sun.",
    "Water boils at 100 degrees Celsius at sea level."
]

candidates = [
    "Our planet revolves around the Sun.",
    "At sea level, water begins to boil when it reaches 100°C."
]

results = calc.evaluate_batch(candidates, references)
for i, result in enumerate(results):
    print(f"Example {i+1} Overall Score: {result.overall_score}")
```

### Can I save evaluation results to a file?

Yes, evaluation results can be exported to JSON:

```python
import json
from llamacalc import LlamaCalc

calc = LlamaCalc()
result = calc.evaluate(candidate="Example answer", reference="Reference answer")

# Convert to dict and save as JSON
result_dict = result.to_dict()
with open("evaluation_result.json", "w") as f:
    json.dump(result_dict, f, indent=2)
```

### How can I analyze the scoring components?

Each evaluation result includes detailed scores for each component:

```python
result = calc.evaluate(candidate, reference)
print(f"Overall: {result.overall_score}")
print(f"Proximity: {result.proximity_score}")
print(f"Coverage: {result.coverage_score}")
print(f"Conciseness: {result.conciseness_score}")
print(f"Logical Flow: {result.logical_flow_score}")
```

## Troubleshooting

### Why is my evaluation taking a long time?

For very long texts, evaluation can take longer. Consider:
1. Enabling caching: `calc = LlamaCalc(use_cache=True)`
2. Using MLX acceleration if you have Apple Silicon
3. Splitting very long texts into smaller chunks

### How do I report bugs or request features?

Please open an issue on our [GitHub repository](https://github.com/llamasearch/llamacalc/issues) with detailed information about the bug or feature request. For bugs, include the error message, steps to reproduce, and your environment details. 