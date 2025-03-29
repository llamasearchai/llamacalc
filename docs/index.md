# LlamaCalc

<div align="center">
<img src="assets/logo.png" alt="LlamaCalc Logo" width="200"/>
</div>

**LlamaCalc** is an advanced relevance score calculator optimized for Apple Silicon, designed to evaluate answer quality based on multiple factors including proximity, concept coverage, conciseness, and logical flow.

## Key Features

- **Multi-Factor Scoring**: Comprehensive evaluation of answer relevance based on:
  - **Proximity Score**: How close the answer is to the reference
  - **Coverage Score**: How well all key concepts are covered
  - **Conciseness Score**: How efficiently information is presented
  - **Logical Flow Score**: How well structured and coherent the answer is

- **MLX Acceleration**: Optimized computations on Apple Silicon for blazing-fast performance

- **Interactive CLI**: User-friendly command line interface with colorful output

- **Robust Architecture**: Includes multithreading and efficient caching mechanisms

- **Docker Support**: Easy deployment in containerized environments

## Quick Start

```bash
# Install from PyPI
pip install llamacalc

# Or install from source
git clone https://github.com/llamasearch/llamacalc.git
cd llamacalc
pip install -e .
```

## Basic Usage

```python
from llamacalc import LlamaCalc

calc = LlamaCalc()

reference = "The quick brown fox jumps over the lazy dog."
candidate = "A brown fox quickly jumped over a dog that was lazy."

result = calc.evaluate(candidate, reference)
print(f"Overall Score: {result.overall_score}")
print(f"Proximity: {result.proximity_score}")
print(f"Coverage: {result.coverage_score}")
print(f"Conciseness: {result.conciseness_score}")
print(f"Logical Flow: {result.logical_flow_score}")
```

## Support

- For bug reports and feature requests, please [open an issue](https://github.com/llamasearch/llamacalc/issues)
- For usage questions, check our [FAQ](faq.md) or [discussions](https://github.com/llamasearch/llamacalc/discussions)
- For contributions, see our [contributing guidelines](contributing.md)

## License

LlamaCalc is released under the [MIT License](license.md). 