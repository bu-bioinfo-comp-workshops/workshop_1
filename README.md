# Workshop 1: Download and Explore Ancient DNA Data

Welcome to your first hands-on computational workshop! This repository contains all the materials you need to complete Workshop 1 of the BU Bioinformatics Computational Skills Workshop series.

## 🎯 Learning Objectives

By the end of this workshop, you will be able to:
- Download ancient mitochondrial genome data from public databases
- Write Python scripts to analyze DNA sequences
- Calculate basic sequence statistics (length, GC content)
- Use Large Language Models (LLMs) effectively for coding assistance
- Practice version control with git and GitHub

## 🔬 Problem Statement

You are a new graduate student in an ancient genomics lab. Your PI wants to know: **"What are the basic characteristics of this ancient mitochondrial genome?"**

Your task is to:
1. Download a small ancient mitochondrial genome dataset from a public database
2. Calculate basic statistics (sequence length, GC content)
3. Summarize your findings in a brief report

## 📚 Workshop Materials

- **Instructions**: See [INSTRUCTIONS.md](INSTRUCTIONS.md) for detailed step-by-step guidance
- **Intro Slides**: [Workshop 1 Introduction](../workshop_1_introduction_slides/index.html)
- **Background Slides**: [Workshop 1 Background](../workshop_1_background_slides/index.html)

## 🛠 Technical Environment

This workshop is designed for the **BU Shared Computing Cluster (SCC)**:
- Use VS Code for development
- Python 3.x for analysis
- Git for version control

## 📁 Repository Structure

```
├── README.md                    # This file
├── INSTRUCTIONS.md              # Detailed workshop guide
├── requirements.txt             # Python dependencies
├── src/                         # Your Python scripts go here
│   ├── download_data.py         # Script to download FASTA data
│   ├── analyze_sequence.py      # Script to analyze sequences
│   └── visualize_results.py     # Optional visualization script
├── data/                        # Downloaded data files
├── results/                     # Analysis results and outputs
├── templates/                   # Report templates
└── docs/                        # Additional documentation
```

## 🚀 Getting Started

1. **Clone this repository** (already done via GitHub Classroom)
2. **Read the full instructions** in [INSTRUCTIONS.md](INSTRUCTIONS.md)
3. **Set up your environment** on the SCC
4. **Start with the first task**: downloading ancient DNA data

## 📋 Deliverables Checklist

By the end of this workshop, you should have:

- [ ] Downloaded FASTA file (`data/ancient_mtDNA.fasta`)
- [ ] Python analysis script (`src/analyze_sequence.py`)
- [ ] Results summary (`results/results.md`)
- [ ] Brief report (`results/summary_report.md`)
- [ ] Optional visualization (`results/gc_content_plot.png`)
- [ ] All files committed and pushed to GitHub

## 🆘 Getting Help

1. **Use the sample prompts** in `docs/sample_prompts.md`
2. **Check troubleshooting guide** in `docs/troubleshooting.md`
3. **Ask instructors** during workshop sessions
4. **Use LLMs effectively** - they're your coding partner!

## 🎓 Workshop Philosophy

This workshop follows the **Problem → Prompt → Code → Debug → Result** cycle:
- **Problem**: Understand what you need to accomplish
- **Prompt**: Craft effective LLM prompts for assistance
- **Code**: Write and run your Python scripts
- **Debug**: Identify and fix issues with LLM help
- **Result**: Achieve your goal and document findings

Good luck, and remember: iteration and debugging are normal parts of the process!

---

**BU Bioinformatics Computational Skills Workshop** | Workshop 1 | Ancient DNA Analysis
