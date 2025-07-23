# Sample LLM Prompts for Workshop 1

This document provides example prompts you can use with Large Language Models (LLMs) to help complete Workshop 1 tasks.

## General Prompting Tips

1. **Be specific** - Include file formats, expected outputs, and context
2. **Provide context** - Mention you're working with ancient DNA data
3. **Ask for explanations** - Request comments and documentation in code
4. **Iterate** - If the first response isn't perfect, ask for modifications
5. **Share errors** - Include error messages when asking for debugging help

## Data Download Prompts

### Basic Download
```
I need to download a FASTA file from NCBI using Python. Please help me write a function that:
1. Takes an accession ID as input
2. Uses the NCBI efetch API to download the sequence
3. Saves it as a FASTA file
4. Handles potential network errors

The URL format should be: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id={accession}&rettype=fasta&retmode=text
```

### Error Handling
```
Please add robust error handling to my NCBI download function. It should handle:
- Network connection errors
- Invalid accession IDs (HTTP 400/404 errors)
- File writing permission errors
- Empty responses from the server

Include informative error messages for each case.
```

### File Verification
```
I need a function to verify that a downloaded FASTA file is valid. Please help me write a function that:
1. Checks if the file exists and is not empty
2. Verifies it starts with a proper FASTA header (line starting with '>')
3. Checks that it contains DNA sequence data
4. Reports basic file information (size, number of lines)
```

## Sequence Analysis Prompts

### FASTA Parsing
```
I need to parse a FASTA file in Python without using BioPython. Please help me write a function that:
1. Reads a FASTA file line by line
2. Handles multi-line sequences properly
3. Returns a dictionary with headers as keys and sequences as values
4. Strips whitespace and handles empty lines
5. Includes error handling for malformed files

Example input file format:
>Header line
ATCGATCGATCG
GCTAGCTAGCTA
>Second sequence
TTTTAAAACCCC
```

### GC Content Calculation
```
Please help me write a Python function to calculate GC content of a DNA sequence. The function should:
1. Take a DNA sequence string as input
2. Count G and C nucleotides (case-insensitive)
3. Calculate percentage: (G + C) / total_length * 100
4. Handle edge cases like empty sequences
5. Return the result as a float rounded to 2 decimal places
6. Include input validation for non-DNA characters
```

### Base Composition Analysis
```
I need a function that analyzes the composition of a DNA sequence. Please help me create a function that:
1. Counts each nucleotide (A, T, G, C) in the sequence
2. Calculates both raw counts and percentages
3. Returns results in a structured format (dictionary)
4. Handles case-insensitive input
5. Ignores non-nucleotide characters
6. Includes summary statistics

Expected output format:
{'A': {'count': 100, 'percent': 25.0}, 'T': {'count': 100, 'percent': 25.0}, ...}
```

## Visualization Prompts

### Pie Chart Creation
```
I want to create a pie chart showing DNA base composition using matplotlib. Please help me write a function that:
1. Takes base composition data (percentages for A, T, G, C)
2. Creates a colorful pie chart with clear labels
3. Uses appropriate colors (e.g., A=red, T=blue, G=green, C=orange)
4. Includes a title and legend
5. Saves the plot as a PNG file
6. Has good visual formatting for a scientific report
```

### Bar Chart for GC Content
```
Please help me create a bar chart comparing GC content vs AT content using matplotlib. The chart should:
1. Have two bars: one for GC% and one for AT%
2. Use different colors for each bar
3. Include clear labels and a title
4. Show percentage values on top of each bar
5. Have proper axis labels
6. Save as a high-quality PNG file
```

## Debugging Prompts

### General Debugging
```
I'm getting this error when running my Python script:
[PASTE ERROR MESSAGE HERE]

Here's the relevant code:
[PASTE CODE HERE]

Please help me understand what's causing this error and how to fix it. I'm working with FASTA files and DNA sequence analysis.
```

### File Path Issues
```
My Python script can't find the FASTA file. I'm getting a "FileNotFoundError". Here's my code:
[PASTE CODE]

I'm running the script from the src/ directory and the FASTA file is in ../data/. Please help me fix the file path handling and add proper error checking.
```

### Data Format Issues
```
My FASTA parsing function isn't working correctly with multi-line sequences. Here's what I have:
[PASTE CODE]

The sequences are getting split incorrectly. Please help me fix the parsing logic to handle sequences that span multiple lines.
```

## Advanced Prompts

### Code Optimization
```
Please review my DNA analysis code and suggest improvements for:
1. Performance optimization
2. Code readability and documentation
3. Error handling
4. Following Python best practices
5. Making it more modular and reusable

Here's my current code:
[PASTE CODE]
```

### Adding Features
```
I have a working DNA analysis script that calculates length and GC content. Please help me add these features:
1. Calculate melting temperature estimation
2. Find and count specific motifs (e.g., CpG sites)
3. Identify the longest stretch of each nucleotide
4. Add command-line argument parsing
5. Export results to CSV format

Current code:
[PASTE CODE]
```

## Workshop-Specific Context

When using these prompts, remember to mention:
- You're working on a bioinformatics workshop
- The data is ancient mitochondrial DNA
- You're using the BU Shared Computing Cluster
- This is for educational purposes
- You want well-documented, beginner-friendly code

## Example Complete Workflow Prompt

```
I'm a graduate student working on an ancient DNA bioinformatics workshop. I need to:

1. Download an ancient mitochondrial genome FASTA file from NCBI
2. Parse the file and extract the DNA sequence
3. Calculate sequence length and GC content
4. Create a simple visualization

Please help me create a complete Python workflow with:
- Error handling and validation
- Clear documentation and comments
- Modular functions that I can understand and modify
- Output that's suitable for a scientific report

I'm working on a computing cluster, so the code should be robust and not require interactive input.
```
