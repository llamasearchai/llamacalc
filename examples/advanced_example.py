#!/usr/bin/env python3
"""
Advanced Example for LlamaCalc

This example demonstrates more advanced features of LlamaCalc,
including batch processing, caching, custom preprocessing, and
integration with other libraries.
"""

import json
import time
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from llamacalc import LlamaCalc
from llamacalc.processors import TextProcessor

def benchmark_performance(calc, texts, iterations=5):
    """Benchmark LlamaCalc performance with and without caching."""
    print("Benchmarking Performance")
    print("-----------------------")
    
    # First run (no cache)
    start_time = time.time()
    for _ in range(iterations):
        for ref, cand in texts:
            calc.evaluate(cand, ref)
    
    first_run_time = time.time() - start_time
    print(f"First run (no cache): {first_run_time:.4f} seconds")
    
    # Second run (with cache)
    start_time = time.time()
    for _ in range(iterations):
        for ref, cand in texts:
            calc.evaluate(cand, ref)
    
    second_run_time = time.time() - start_time
    print(f"Second run (with cache): {second_run_time:.4f} seconds")
    print(f"Speed improvement: {first_run_time / second_run_time:.2f}x faster")
    
    return first_run_time, second_run_time

def batch_processing_example(calc, texts):
    """Demonstrate batch processing capabilities."""
    print("\nBatch Processing Example")
    print("-----------------------")
    
    references = [text[0] for text in texts]
    candidates = [text[1] for text in texts]
    
    print(f"Processing {len(texts)} text pairs in batch...")
    results = calc.evaluate_batch(candidates, references)
    
    # Create a pandas DataFrame for easier analysis
    df = pd.DataFrame([
        {
            "reference": ref,
            "candidate": cand,
            "overall": result.overall_score,
            "proximity": result.proximity_score,
            "coverage": result.coverage_score,
            "conciseness": result.conciseness_score,
            "logical_flow": result.logical_flow_score
        }
        for ref, cand, result in zip(references, candidates, results)
    ])
    
    print("\nResults summary:")
    print(df.describe())
    
    return df

def visualize_results(df):
    """Visualize evaluation results."""
    print("\nVisualizing Results")
    print("------------------")
    
    # Create a figure with multiple subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle("LlamaCalc Evaluation Results", fontsize=16)
    
    # Score distribution histogram
    axes[0, 0].hist(df['overall'], bins=10, alpha=0.7, color='blue')
    axes[0, 0].set_title("Overall Score Distribution")
    axes[0, 0].set_xlabel("Score")
    axes[0, 0].set_ylabel("Frequency")
    
    # Component score comparison
    component_means = [
        df['proximity'].mean(),
        df['coverage'].mean(),
        df['conciseness'].mean(),
        df['logical_flow'].mean()
    ]
    components = ['Proximity', 'Coverage', 'Conciseness', 'Logical Flow']
    axes[0, 1].bar(components, component_means, color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
    axes[0, 1].set_title("Average Component Scores")
    axes[0, 1].set_ylabel("Score")
    axes[0, 1].set_ylim(0, 1)
    
    # Scatter plot of overall vs. component scores
    for i, component in enumerate(['proximity', 'coverage', 'conciseness', 'logical_flow']):
        axes[1, 0].scatter(df[component], df['overall'], label=components[i], alpha=0.7)
    axes[1, 0].set_title("Overall Score vs. Component Scores")
    axes[1, 0].set_xlabel("Component Score")
    axes[1, 0].set_ylabel("Overall Score")
    axes[1, 0].legend()
    
    # Text length vs. scores
    df['ref_length'] = df['reference'].apply(len)
    df['cand_length'] = df['candidate'].apply(len)
    df['length_ratio'] = df['cand_length'] / df['ref_length']
    
    axes[1, 1].scatter(df['length_ratio'], df['overall'], color='purple', alpha=0.7)
    axes[1, 1].set_title("Score vs. Length Ratio")
    axes[1, 1].set_xlabel("Candidate/Reference Length Ratio")
    axes[1, 1].set_ylabel("Overall Score")
    
    # Adjust layout and save
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    plt.savefig(output_dir / "evaluation_results.png")
    print(f"Visualization saved to {output_dir/'evaluation_results.png'}")
    
    # Also save the data to JSON for further analysis
    df.to_json(output_dir / "evaluation_data.json", orient="records", indent=2)
    print(f"Data saved to {output_dir/'evaluation_data.json'}")

def custom_text_processing_example():
    """Demonstrate custom text preprocessing options."""
    print("\nCustom Text Processing Example")
    print("----------------------------")
    
    # Create a processor with custom settings
    processor = TextProcessor(
        lowercase=True,
        remove_punctuation=True,
        remove_stopwords=True,
        stem_words=True
    )
    
    # Initialize calculator with custom processor
    calc = LlamaCalc(text_processor=processor)
    
    # Example text pair
    reference = "The quick brown fox jumps over the lazy dog."
    candidate = "A brown fox quickly jumped over a dog that was lazy."
    
    # Process and print the processed text
    processed_ref = processor.process(reference)
    processed_cand = processor.process(candidate)
    
    print("Original reference:", reference)
    print("Processed reference:", processed_ref)
    print("Original candidate:", candidate)
    print("Processed candidate:", processed_cand)
    
    # Evaluate with custom processing
    result = calc.evaluate(candidate, reference)
    print(f"Overall Score with custom processing: {result.overall_score:.2f}")
    
    # Compare with default processing
    default_calc = LlamaCalc()
    default_result = default_calc.evaluate(candidate, reference)
    print(f"Overall Score with default processing: {default_result.overall_score:.2f}")
    print(f"Difference: {abs(result.overall_score - default_result.overall_score):.4f}")

def export_results_example(calc, reference, candidate):
    """Demonstrate exporting and formatting results."""
    print("\nExporting Results Example")
    print("-----------------------")
    
    result = calc.evaluate(candidate, reference)
    
    # Convert to dictionary
    result_dict = {
        "overall_score": result.overall_score,
        "component_scores": {
            "proximity": result.proximity_score,
            "coverage": result.coverage_score,
            "conciseness": result.conciseness_score,
            "logical_flow": result.logical_flow_score
        },
        "texts": {
            "reference": reference,
            "candidate": candidate
        },
        "metadata": result.metadata
    }
    
    # Print pretty JSON
    print("JSON output:")
    print(json.dumps(result_dict, indent=2))
    
    # Save to file
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    with open(output_dir / "evaluation_result.json", "w") as f:
        json.dump(result_dict, f, indent=2)
    
    print(f"Result saved to {output_dir/'evaluation_result.json'}")

def main():
    """Run the advanced LlamaCalc example."""
    print("LlamaCalc Advanced Example")
    print("=========================\n")
    
    # Create output directory
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    # Initialize LlamaCalc with caching enabled
    calc = LlamaCalc(
        use_cache=True,
        cache_dir=str(output_dir / "cache"),
        verbose=True
    )
    
    # Sample text pairs for testing
    text_pairs = [
        (
            "Machine learning is a field of inquiry devoted to understanding and building methods that 'learn', that is, methods that leverage data to improve performance on some set of tasks.",
            "Machine learning is an area of AI that focuses on developing systems that learn from data."
        ),
        (
            "The Internet is a global system of interconnected computer networks that uses the Internet protocol suite to communicate between networks and devices.",
            "The Internet is a worldwide network of connected computers that communicate using standardized protocols."
        ),
        (
            "Climate change includes both global warming driven by human-induced emissions of greenhouse gases and the resulting large-scale shifts in weather patterns.",
            "Climate change refers to significant changes in global temperature, precipitation, wind patterns, and other measures of climate that occur over several decades or longer."
        ),
        (
            "Photosynthesis is a process used by plants and other organisms to convert light energy into chemical energy that can later be released to fuel the organisms' activities.",
            "Through photosynthesis, plants use sunlight, water, and carbon dioxide to create oxygen and energy in the form of sugar."
        ),
        (
            "Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to natural intelligence displayed by humans or animals.",
            "AI refers to the simulation of human intelligence in machines that are programmed to think and learn like humans."
        ),
    ]
    
    # Benchmark performance
    first_run, second_run = benchmark_performance(calc, text_pairs)
    
    # Batch processing
    results_df = batch_processing_example(calc, text_pairs)
    
    # Visualize results
    visualize_results(results_df)
    
    # Custom text processing
    custom_text_processing_example()
    
    # Export results
    export_results_example(calc, text_pairs[0][0], text_pairs[0][1])
    
    print("\nAdvanced example completed successfully!")

if __name__ == "__main__":
    main() 