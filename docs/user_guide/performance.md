# Performance Optimization

LlamaCalc is designed to be efficient, but there are several ways to optimize its performance for your specific use case. This guide covers techniques to make your text evaluation faster and more resource-efficient.

## MLX Acceleration

If you're using an Apple Silicon Mac (M1/M2/M3), LlamaCalc can leverage the MLX framework for significantly improved performance.

### Enabling MLX

MLX is enabled by default if available, but you can explicitly enable or disable it:

```python
# Enable MLX acceleration (default on Apple Silicon)
calc = LlamaCalc(use_mlx=True)

# Disable MLX acceleration
calc = LlamaCalc(use_mlx=False)
```

### Performance Gains

On Apple Silicon, MLX acceleration can result in 2-5x faster computations for embedding generation and similarity calculations compared to NumPy-based calculations.

## Caching Strategies

Caching is one of the most effective ways to improve performance, especially when evaluating the same or similar texts repeatedly.

### Memory Caching

In-memory caching is enabled by default but can be explicitly controlled:

```python
# Enable in-memory caching (default)
calc = LlamaCalc(use_cache=True)

# Disable caching
calc = LlamaCalc(use_cache=False)
```

### Persistent Caching

For longer-running applications or when you want to preserve cache between sessions:

```python
# Enable persistent caching to disk
calc = LlamaCalc(
    use_cache=True,
    cache_dir="./llamacalc_cache"
)
```

The persistent cache will save embeddings and intermediate results to disk, allowing them to be reused across multiple runs of your application.

### Clearing the Cache

If your cache grows too large or you want to free up memory:

```python
# Clear the cache
calc.clear_cache()
```

## Batch Processing

Processing multiple evaluations in batch is much more efficient than processing them individually:

```python
# Inefficient: individual processing
results = []
for cand, ref in zip(candidates, references):
    results.append(calc.evaluate(cand, ref))

# Efficient: batch processing
results = calc.evaluate_batch(candidates, references)
```

Batch processing allows for:
- Reduced overhead from repeated function calls
- More efficient use of hardware resources
- Better parallelization

## Text Preprocessing Optimization

### Lightweight Processing

If you don't need advanced text preprocessing, use a minimal configuration:

```python
from llamacalc import LlamaCalc
from llamacalc.processors import TextProcessor

# Minimal preprocessing
processor = TextProcessor(
    lowercase=True,
    remove_punctuation=False,
    remove_stopwords=False,
    stem_words=False
)

calc = LlamaCalc(text_processor=processor)
```

### Preprocessing Once

If you need to evaluate the same texts against multiple references, preprocess them once:

```python
from llamacalc.processors import TextProcessor

processor = TextProcessor()
processed_text = processor.process(long_text)

# Now use the processed text in multiple evaluations
```

## Resource Usage Management

### Controlling Memory Usage

For large texts or batch processing, you might need to manage memory usage:

```python
import gc

# Process in smaller batches
batch_size = 100
for i in range(0, len(candidates), batch_size):
    batch_results = calc.evaluate_batch(
        candidates[i:i+batch_size],
        references[i:i+batch_size]
    )
    # Process batch results...
    
    # Force garbage collection
    gc.collect()
```

### Reducing Component Calculations

If you only need specific scoring components, you can optimize by using those directly:

```python
from llamacalc.scorers import ProximityScorer, CoverageScorer

# Just calculate proximity
proximity_scorer = ProximityScorer()
proximity = proximity_scorer.calculate(candidate, reference)

# Just calculate coverage
coverage_scorer = CoverageScorer()
coverage = coverage_scorer.calculate(candidate, reference)
```

## Docker Deployment

For consistent performance across environments, consider using the Docker container:

```bash
docker run --name llamacalc -v /path/to/data:/data llamasearch/llamacalc:latest
```

The Docker container includes all optimizations and dependencies pre-configured.

## Performance Benchmarking

To understand the performance of LlamaCalc in your specific environment, you can use the built-in benchmarking tools:

```python
from llamacalc.benchmarks import benchmark_performance

results = benchmark_performance(
    text_pairs=your_text_pairs,
    use_mlx=True,
    use_cache=True,
    iterations=10
)

print(f"Average time per evaluation: {results['avg_time_ms']:.2f} ms")
print(f"Cache hit rate: {results['cache_hit_rate']:.2%}")
```

## Performance Recommendations

For best performance:

1. **Use MLX on Apple Silicon**: Enable MLX acceleration if you're on an M1/M2/M3 Mac
2. **Enable Caching**: Use persistent caching for repeated evaluations
3. **Process in Batches**: Use batch processing for multiple evaluations
4. **Optimize Text Length**: Consider summarizing or chunking very long texts
5. **Use Docker**: For consistent performance in production environments

By following these optimization strategies, you can achieve significant performance improvements in your LlamaCalc evaluations. 