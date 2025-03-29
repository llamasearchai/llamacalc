# Scoring Methodology

This document explains how LlamaCalc evaluates the relevance of answers to questions. The scoring methodology is based on four key components that each assess a different aspect of answer quality.

## Overview

LlamaCalc generates a total relevance score between 0.0 and 1.0, which is a weighted average of four component scores:

1. **Proximity Score (default weight: 0.35)**: How directly the answer addresses the question
2. **Coverage Score (default weight: 0.30)**: How well the answer covers key concepts from the question
3. **Conciseness Score (default weight: 0.15)**: How appropriately detailed the answer is
4. **Logical Flow Score (default weight: 0.20)**: How well-structured and coherent the answer is

The formula for the total score is:

```
Total Score = (Proximity × 0.35) + (Coverage × 0.30) + (Conciseness × 0.15) + (Logical Flow × 0.20)
```

These weights can be customized based on the specific evaluation needs (see [Customization](customization.md)).

## Component Scores

### Proximity Score

The Proximity Score measures how directly the answer addresses the question using vector similarity. This helps identify answers that are topically relevant to the question.

**Calculation Process:**
1. Convert both question and answer to vector representations
2. Compute the cosine similarity between these vectors
3. Scale the similarity to a 0.0-1.0 range

**Example:**
- **High score (0.8+)**: Answer directly addresses the main topic of the question
- **Medium score (0.5-0.7)**: Answer is related but slightly tangential
- **Low score (<0.5)**: Answer is about a different topic altogether

### Coverage Score

The Coverage Score evaluates how well the answer covers key concepts mentioned in the question. This helps identify answers that are comprehensive in addressing all aspects of the question.

**Calculation Process:**
1. Extract key concepts from both question and answer
2. Calculate what percentage of question concepts appear in the answer
3. Apply a soft curve to reward partial coverage

**Example:**
- **High score (0.8+)**: Answer addresses all key concepts from the question
- **Medium score (0.5-0.7)**: Answer addresses some but not all concepts
- **Low score (<0.5)**: Answer misses most key concepts from the question

### Conciseness Score

The Conciseness Score assesses whether the answer is appropriately detailed without being too verbose or too brief. This helps identify answers that are the right length for the question.

**Calculation Process:**
1. Calculate a reasonable expected length range based on question complexity
2. Compare actual answer length to this expected range
3. Score highest for answers in the middle of the expected range, penalizing those that are too short or too long

**Example:**
- **High score (0.8+)**: Answer length is appropriate for the complexity of the question
- **Medium score (0.5-0.7)**: Answer is slightly too short or too long
- **Low score (<0.5)**: Answer is significantly too brief or excessively verbose

### Logical Flow Score

The Logical Flow Score analyzes the logical structure and coherence of the answer. This helps identify answers that are well-organized and easy to follow.

**Calculation Process:**
1. Analyze sentence structure, transitions, and paragraph organization
2. Check for appropriate sentence length variation
3. Penalize very short sentences (fragments) and extremely long sentences
4. Reward multi-paragraph answers with good structure

**Example:**
- **High score (0.8+)**: Well-structured answer with clear logical progression
- **Medium score (0.5-0.7)**: Generally coherent but with some structural issues
- **Low score (<0.5)**: Poorly organized, choppy, or incoherent answer

## Interpreting the Total Score

The total score can be interpreted as follows:

- **0.8-1.0**: Excellent answer that directly and comprehensively addresses the question with appropriate detail and clear organization
- **0.6-0.8**: Good answer with some minor issues in relevance, coverage, length, or structure
- **0.4-0.6**: Fair answer with significant issues in one or more components
- **0.2-0.4**: Poor answer that fails to adequately address the question
- **0.0-0.2**: Very poor answer that is largely irrelevant or incomprehensible

## Technical Implementation

The current implementation uses simplified vector representations based on word frequencies. In production environments, you might want to consider using more sophisticated embedding models for the Proximity Score calculation.

The key concept extraction for Coverage Score currently uses a simplified approach based on word tokenization and filtering. For more advanced applications, you could integrate specialized NLP libraries for entity recognition and key phrase extraction.

See [Performance](performance.md) for more information about the technical implementation and optimization options. 