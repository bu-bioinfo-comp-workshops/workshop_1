#!/usr/bin/env python3
"""
Workshop 1: Analyze Ancient DNA Sequence
========================================

This script analyzes an ancient mitochondrial genome FASTA file to calculate
basic sequence statistics including length and GC content.

Your task: Complete the functions below to analyze the downloaded sequence.

Author: [Your Name]
Date: [Date]
"""

import os
from pathlib import Path


def read_fasta(fasta_file):
    """
    Read a FASTA file and return the sequence(s).
    
    Args:
        fasta_file (str): Path to the FASTA file
    
    Returns:
        dict: Dictionary with headers as keys and sequences as values
              Example: {'header1': 'ATCGATCG', 'header2': 'GCTAGCTA'}
    
    TODO: Implement this function
    """
    sequences = {}
    
    # TODO: Open and read the FASTA file
    # TODO: Parse headers (lines starting with '>') and sequences
    # TODO: Handle multi-line sequences (concatenate sequence lines)
    # TODO: Store in dictionary format
    
    # Hint: You'll need to:
    # 1. Open the file
    # 2. Track current header
    # 3. Accumulate sequence lines
    # 4. Handle the transition between sequences
    
    pass


def clean_sequence(sequence):
    """
    Clean a DNA sequence by removing non-nucleotide characters.
    
    Args:
        sequence (str): Raw DNA sequence
    
    Returns:
        str: Cleaned sequence containing only A, T, G, C
    
    TODO: Implement this function
    """
    # TODO: Convert to uppercase
    # TODO: Remove any characters that aren't A, T, G, or C
    # TODO: Remove whitespace and newlines
    
    pass


def calculate_sequence_length(sequence):
    """
    Calculate the length of a DNA sequence.
    
    Args:
        sequence (str): DNA sequence
    
    Returns:
        int: Length of the sequence
    
    TODO: Implement this function
    """
    # TODO: Return the length of the cleaned sequence
    pass


def calculate_gc_content(sequence):
    """
    Calculate the GC content of a DNA sequence.
    
    Args:
        sequence (str): DNA sequence
    
    Returns:
        float: GC content as a percentage (0-100)
    
    TODO: Implement this function
    """
    # TODO: Count G and C nucleotides
    # TODO: Calculate percentage: (G + C) / total_length * 100
    # TODO: Handle edge case of empty sequence
    
    pass


def calculate_base_composition(sequence):
    """
    Calculate the composition of each base in the sequence.
    
    Args:
        sequence (str): DNA sequence
    
    Returns:
        dict: Dictionary with base counts and percentages
              Example: {'A': {'count': 100, 'percent': 25.0}, ...}
    
    TODO: Implement this function
    """
    composition = {}
    
    # TODO: Count each base (A, T, G, C)
    # TODO: Calculate percentages for each base
    # TODO: Return in the specified format
    
    pass


def analyze_sequence(fasta_file):
    """
    Main analysis function that processes a FASTA file and returns statistics.
    
    Args:
        fasta_file (str): Path to the FASTA file
    
    Returns:
        dict: Dictionary containing analysis results
    
    TODO: Implement this function by calling the other functions
    """
    print(f"🔬 Analyzing sequence from: {fasta_file}")
    
    # TODO: Read the FASTA file
    sequences = read_fasta(fasta_file)
    
    if not sequences:
        print("❌ No sequences found in the file!")
        return None
    
    # For this workshop, we'll analyze the first sequence
    # TODO: Get the first sequence from the dictionary
    header = list(sequences.keys())[0]
    raw_sequence = sequences[header]
    
    print(f"📝 Sequence header: {header}")
    
    # TODO: Clean the sequence
    clean_seq = clean_sequence(raw_sequence)
    
    # TODO: Calculate statistics
    length = calculate_sequence_length(clean_seq)
    gc_content = calculate_gc_content(clean_seq)
    base_comp = calculate_base_composition(clean_seq)
    
    # Compile results
    results = {
        'header': header,
        'length': length,
        'gc_content': gc_content,
        'base_composition': base_comp,
        'sequence_preview': clean_seq[:50] + "..." if len(clean_seq) > 50 else clean_seq
    }
    
    return results


def display_results(results):
    """
    Display the analysis results in a formatted way.
    
    Args:
        results (dict): Analysis results from analyze_sequence()
    
    TODO: Implement this function to display results nicely
    """
    if not results:
        print("❌ No results to display!")
        return
    
    print("\n" + "="*60)
    print("🧬 ANCIENT DNA SEQUENCE ANALYSIS RESULTS")
    print("="*60)
    
    # TODO: Display the header
    # TODO: Display sequence length
    # TODO: Display GC content
    # TODO: Display base composition
    # TODO: Display sequence preview
    
    pass


def save_results(results, output_file):
    """
    Save analysis results to a file.
    
    Args:
        results (dict): Analysis results
        output_file (str): Path to save results
    
    TODO: Implement this function
    """
    # TODO: Create results directory if it doesn't exist
    # TODO: Write results to file in a readable format
    # TODO: Include timestamp and other metadata
    
    pass


def main():
    """
    Main function to run the sequence analysis.
    """
    print("🧬 Workshop 1: Ancient DNA Sequence Analysis")
    print("=" * 50)
    
    # Path to the downloaded FASTA file
    fasta_file = "../data/ancient_mtDNA.fasta"
    
    # Check if the file exists
    if not os.path.exists(fasta_file):
        print(f"❌ FASTA file not found: {fasta_file}")
        print("Please run download_data.py first to download the sequence!")
        return
    
    # Analyze the sequence
    results = analyze_sequence(fasta_file)
    
    if results:
        # Display results
        display_results(results)
        
        # Save results
        results_dir = Path("../results")
        results_dir.mkdir(exist_ok=True)
        save_results(results, "../results/results.md")
        
        print("\n✅ Analysis complete!")
        print("📁 Results saved to: ../results/results.md")
        print("\nNext step: Fill out your summary report!")
    else:
        print("❌ Analysis failed!")


if __name__ == "__main__":
    main()


# SAMPLE LLM PROMPTS FOR THIS SCRIPT:
"""
1. FASTA parsing prompt:
   "I need to parse a FASTA file in Python. Please help me write a function that reads a FASTA file and returns a dictionary with headers as keys and sequences as values. Handle multi-line sequences properly."

2. GC content calculation prompt:
   "Please help me write a Python function to calculate GC content of a DNA sequence. It should return the percentage of G and C nucleotides in the sequence."

3. Base composition prompt:
   "I need a function that counts each nucleotide (A, T, G, C) in a DNA sequence and returns both counts and percentages for each base."

4. Results formatting prompt:
   "Help me create a function that displays DNA sequence analysis results in a nicely formatted way, including sequence length, GC content, and base composition."
"""
