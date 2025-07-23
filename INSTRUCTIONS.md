# Workshop 1: Detailed Instructions

## Overview

This workshop introduces you to computational analysis of ancient DNA data. You'll download real ancient mitochondrial genome data and perform basic sequence analysis using Python, with assistance from Large Language Models (LLMs).

## Prerequisites

- Access to BU Shared Computing Cluster (SCC)
- VS Code installed and configured
- Basic familiarity with command line
- GitHub account (for version control)

## Workshop Schedule (3 hours)

### Hour 1: Setup and Environment (50 min + 10 min break)
- SCC OnDemand setup and SSH keys
- VS Code configuration and plugins
- Git/GitHub workflow basics
- Understanding SCC structure (head nodes, compute nodes, interactive jobs)

### Hour 2: Data Download and Initial Analysis (60 min)
- **Objective 1** (20 min): Develop method to download genome and calculate GC content
- **Discussion** (10 min): Review approaches and best practices
- **Modifications** (30 min): Refine your approach based on feedback

### Hour 3: Advanced Analysis and Reporting (60 min)
- **New modifications** (30 min): Implement additional features
- **Final discussion** (30 min): Present results and discuss approaches

## Step-by-Step Instructions

### Step 1: Environment Setup

1. **Log into SCC OnDemand**
   - Navigate to your project directory
   - Open VS Code through OnDemand interface

2. **Clone your repository**
   ```bash
   git clone [your-github-classroom-repo-url]
   cd workshop-1-ancient-dna-[your-username]
   ```

3. **Set up Python environment**
   ```bash
   # Install required packages
   pip install --user -r requirements.txt
   ```

### Step 2: Data Acquisition

**Goal**: Download an ancient mitochondrial genome FASTA file from a public database.

**Recommended databases**:
- Allen Ancient DNA Resource (AADR)
- NCBI Nucleotide Database
- European Nucleotide Archive (ENA)

**Your task**:
1. Open `src/download_data.py`
2. Use an LLM to help you write code that downloads a small ancient mtDNA sequence
3. Save the sequence to `data/ancient_mtDNA.fasta`

**Sample LLM Prompt**:
```
I need to download a small ancient mitochondrial genome FASTA file from a public database like NCBI. Please help me write Python code that:
1. Downloads a specific ancient mtDNA sequence
2. Saves it as a FASTA file
3. Handles potential errors gracefully

The sequence should be from an ancient human sample, preferably under 20kb in size.
```

### Step 3: Sequence Analysis

**Goal**: Calculate basic statistics for your downloaded sequence.

**Your task**:
1. Open `src/analyze_sequence.py`
2. Implement functions to:
   - Read the FASTA file
   - Calculate sequence length
   - Calculate GC content percentage
   - Display results clearly

**Key functions to implement**:
- `read_fasta(filename)` - Parse FASTA file
- `calculate_gc_content(sequence)` - Calculate GC percentage
- `analyze_sequence(fasta_file)` - Main analysis function

**Sample LLM Prompt**:
```
I have a FASTA file containing an ancient mitochondrial genome. Please help me write Python code that:
1. Reads the FASTA file and extracts the DNA sequence
2. Calculates the total sequence length
3. Calculates the GC content as a percentage
4. Prints the results in a clear format
5. Handles common file reading errors

The code should be well-documented with comments explaining each step.
```

### Step 4: Results Documentation

**Goal**: Document your findings in structured reports.

**Your task**:
1. Fill out `results/results.md` with your numerical findings
2. Complete `results/summary_report.md` with your analysis and interpretation
3. Include any challenges you encountered and how you solved them

### Step 5: Optional Visualization

**Goal**: Create a simple visualization of your results.

**Your task**:
1. Open `src/visualize_results.py`
2. Create a bar chart or pie chart showing:
   - Base composition (A, T, G, C percentages)
   - GC vs AT content
3. Save the plot as `results/gc_content_plot.png`

**Sample LLM Prompt**:
```
I have calculated the GC content and base composition of a DNA sequence. Please help me create a Python script using matplotlib that:
1. Creates a pie chart showing the percentage of each base (A, T, G, C)
2. Creates a bar chart comparing GC content vs AT content
3. Saves both plots as PNG files
4. Uses clear labels and titles

My data includes: sequence length, GC percentage, and individual base counts.
```

### Step 6: Version Control

**Goal**: Track your work with git and push to GitHub.

**Your task**:
1. Add all your files to git:
   ```bash
   git add .
   git commit -m "Complete Workshop 1: Ancient DNA analysis"
   git push origin main
   ```

2. Verify all deliverables are in your GitHub repository

## Problem-Solving Strategy

### The LLM Collaboration Cycle

1. **Problem Definition**: Clearly state what you want to accomplish
2. **Prompt Crafting**: Write specific, detailed prompts for the LLM
3. **Code Generation**: Let the LLM help you write initial code
4. **Testing & Debugging**: Run the code and identify issues
5. **Iteration**: Use the LLM to help debug and improve
6. **Documentation**: Record your approach and results

### Effective LLM Prompting Tips

- **Be specific**: Include file formats, expected outputs, error handling
- **Provide context**: Mention you're working with ancient DNA data
- **Ask for explanations**: Request comments and documentation in code
- **Iterate**: If the first response isn't perfect, ask for modifications
- **Debug together**: Share error messages with the LLM for help

### Common Challenges and Solutions

**Challenge**: FASTA file parsing errors
- **Solution**: Check file format, handle headers correctly, strip whitespace

**Challenge**: Network/download issues on SCC
- **Solution**: Use wget or curl commands, check file permissions

**Challenge**: GC calculation discrepancies
- **Solution**: Verify sequence cleaning (remove headers, newlines, non-ATGC characters)

**Challenge**: Git/GitHub authentication
- **Solution**: Ensure SSH keys are properly configured

## Assessment Criteria

Your work will be evaluated on:

- **Functionality** (40%): Do your scripts work correctly?
- **Code Quality** (25%): Is your code well-documented and organized?
- **Problem Solving** (20%): Did you effectively use LLMs and debug issues?
- **Documentation** (15%): Are your reports clear and complete?

## Resources

- **Sample Prompts**: See `docs/sample_prompts.md`
- **Troubleshooting**: See `docs/troubleshooting.md`
- **Python FASTA parsing**: BioPython documentation
- **SCC Documentation**: BU Research Computing guides

## Final Deliverables Checklist

Before submitting, ensure you have:

- [ ] `data/ancient_mtDNA.fasta` - Downloaded sequence file
- [ ] `src/analyze_sequence.py` - Working analysis script
- [ ] `results/results.md` - Numerical results summary
- [ ] `results/summary_report.md` - Brief analysis report
- [ ] `results/gc_content_plot.png` - Optional visualization
- [ ] All files committed and pushed to GitHub
- [ ] Repository is clean and well-organized

Remember: The goal is learning, not perfection. Document your process, including challenges and how you overcame them!
