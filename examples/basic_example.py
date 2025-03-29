#!/usr/bin/env python3
"""
Basic Example for LlamaCalc

This example demonstrates the fundamental usage of LlamaCalc
for evaluating text relevance.
"""

from llamacalc import LlamaCalc

def main():
    """Run the basic LlamaCalc example."""
    print("LlamaCalc Basic Example")
    print("=======================\n")

    # Initialize LlamaCalc with default settings
    print("Initializing LlamaCalc...")
    calc = LlamaCalc()
    print("Initialization complete!\n")

    # Example 1: Basic Evaluation
    print("Example 1: Basic Evaluation")
    print("--------------------------")
    
    reference = "The quick brown fox jumps over the lazy dog."
    candidate = "A brown fox quickly jumped over a dog that was lazy."
    
    print(f"Reference: {reference}")
    print(f"Candidate: {candidate}")
    
    # Evaluate the candidate against the reference
    result = calc.evaluate(candidate, reference)
    
    # Print results
    print("\nResults:")
    print(f"Overall Score: {result.overall_score:.2f}")
    print(f"Proximity Score: {result.proximity_score:.2f}")
    print(f"Coverage Score: {result.coverage_score:.2f}")
    print(f"Conciseness Score: {result.conciseness_score:.2f}")
    print(f"Logical Flow Score: {result.logical_flow_score:.2f}")
    
    # Example 2: Different Weights
    print("\n\nExample 2: Customized Weights")
    print("-----------------------------")
    
    # Initialize with custom weights
    custom_calc = LlamaCalc(
        proximity_weight=0.4,
        coverage_weight=0.3,
        conciseness_weight=0.2,
        logical_flow_weight=0.1
    )
    
    print("Custom weights:")
    print("- Proximity: 0.4")
    print("- Coverage: 0.3")
    print("- Conciseness: 0.2")
    print("- Logical Flow: 0.1")
    
    # Using the same texts
    custom_result = custom_calc.evaluate(candidate, reference)
    
    # Print custom-weighted results
    print("\nResults with custom weights:")
    print(f"Overall Score: {custom_result.overall_score:.2f}")
    print(f"Proximity Score: {custom_result.proximity_score:.2f}")
    print(f"Coverage Score: {custom_result.coverage_score:.2f}")
    print(f"Conciseness Score: {custom_result.conciseness_score:.2f}")
    print(f"Logical Flow Score: {custom_result.logical_flow_score:.2f}")
    
    # Example 3: Different Text Pairs
    print("\n\nExample 3: Different Text Pairs")
    print("-------------------------------")
    
    references = [
        "Python is a high-level, interpreted programming language.",
        "The Earth orbits the Sun at an average distance of 93 million miles."
    ]
    
    candidates = [
        "Python is a popular programming language that is interpreted and high-level.",
        "Our planet revolves around the Sun, typically about 150 million kilometers away."
    ]
    
    for i, (ref, cand) in enumerate(zip(references, candidates)):
        print(f"\nPair {i+1}:")
        print(f"Reference: {ref}")
        print(f"Candidate: {cand}")
        
        result = calc.evaluate(cand, ref)
        
        print(f"Overall Score: {result.overall_score:.2f}")

if __name__ == "__main__":
    main() 