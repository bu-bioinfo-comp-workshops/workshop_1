#!/usr/bin/env python3
"""
Workshop 1: Visualize Ancient DNA Analysis Results
=================================================

This script creates visualizations of the ancient DNA sequence analysis results.
This is an OPTIONAL component of Workshop 1.

Your task: Complete the functions below to create informative plots.

Author: [Your Name]
Date: [Date]
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import json


def load_analysis_results():
    """
    Load analysis results from the analyze_sequence.py output.
    
    Returns:
        dict: Analysis results, or None if not found
    
    TODO: Implement this function
    """
    # TODO: Try to load results from a saved file or re-run analysis
    # For now, you might need to run analyze_sequence.py first
    # or modify this to directly analyze the FASTA file
    
    # Placeholder - you'll need to adapt this based on how you save results
    pass


def create_base_composition_pie_chart(base_composition, output_file):
    """
    Create a pie chart showing the composition of each base (A, T, G, C).
    
    Args:
        base_composition (dict): Base composition data
        output_file (str): Path to save the plot
    
    TODO: Implement this function
    """
    # TODO: Extract base percentages from the composition data
    # TODO: Create a pie chart with matplotlib
    # TODO: Add appropriate labels, colors, and title
    # TODO: Save the plot to the specified file
    
    # Suggested colors: A=red, T=blue, G=green, C=orange
    colors = ['red', 'blue', 'green', 'orange']
    
    pass


def create_gc_content_bar_chart(gc_content, output_file):
    """
    Create a bar chart comparing GC content vs AT content.
    
    Args:
        gc_content (float): GC content percentage
        output_file (str): Path to save the plot
    
    TODO: Implement this function
    """
    # TODO: Calculate AT content (100 - GC content)
    # TODO: Create a bar chart with two bars: GC and AT
    # TODO: Add appropriate labels, colors, and title
    # TODO: Save the plot to the specified file
    
    pass


def create_sequence_length_visualization(length, output_file):
    """
    Create a simple visualization showing sequence length context.
    
    Args:
        length (int): Sequence length in base pairs
        output_file (str): Path to save the plot
    
    TODO: Implement this function (OPTIONAL - be creative!)
    """
    # TODO: Create an informative visualization of sequence length
    # Ideas: Compare to other genomes, show as a scale, etc.
    
    pass


def create_summary_dashboard(results, output_file):
    """
    Create a multi-panel dashboard with all visualizations.
    
    Args:
        results (dict): Complete analysis results
        output_file (str): Path to save the dashboard
    
    TODO: Implement this function (ADVANCED - optional)
    """
    # TODO: Create a figure with multiple subplots
    # TODO: Include pie chart, bar chart, and other visualizations
    # TODO: Add overall title and formatting
    
    pass


def main():
    """
    Main function to create all visualizations.
    """
    print("📊 Workshop 1: Ancient DNA Visualization")
    print("=" * 50)
    
    # Create results directory
    results_dir = Path("../results")
    results_dir.mkdir(exist_ok=True)
    
    # TODO: Load your analysis results
    # You might need to modify this based on how you store results
    results = load_analysis_results()
    
    if not results:
        print("❌ No analysis results found!")
        print("Please run analyze_sequence.py first to generate results.")
        return
    
    print("📈 Creating visualizations...")
    
    # TODO: Create individual plots
    # create_base_composition_pie_chart(
    #     results['base_composition'], 
    #     "../results/base_composition_pie.png"
    # )
    
    # create_gc_content_bar_chart(
    #     results['gc_content'], 
    #     "../results/gc_content_bar.png"
    # )
    
    # TODO: Optional advanced visualizations
    # create_sequence_length_visualization(
    #     results['length'], 
    #     "../results/sequence_length.png"
    # )
    
    # create_summary_dashboard(
    #     results, 
    #     "../results/analysis_dashboard.png"
    # )
    
    print("✅ Visualizations complete!")
    print("📁 Plots saved to: ../results/")


if __name__ == "__main__":
    main()


# SAMPLE LLM PROMPTS FOR THIS SCRIPT:
"""
1. Pie chart prompt:
   "I need to create a pie chart in Python using matplotlib that shows the percentage composition of DNA bases (A, T, G, C). Please help me write a function that takes base composition data and creates a colorful, well-labeled pie chart."

2. Bar chart prompt:
   "Please help me create a bar chart comparing GC content vs AT content of a DNA sequence. The chart should have two bars with different colors and clear labels."

3. Dashboard prompt:
   "I want to create a multi-panel figure in matplotlib that combines several plots (pie chart, bar chart) into one dashboard. Please help me create a function that arranges multiple subplots nicely."

4. Styling prompt:
   "Help me improve the styling of my matplotlib plots - add better colors, fonts, titles, and make them publication-ready for a scientific report."
"""
