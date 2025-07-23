# Workshop 1 Troubleshooting Guide

This guide helps you solve common issues encountered during Workshop 1.

## Environment Setup Issues

### SSH Key Problems on SCC
**Problem:** Can't authenticate with GitHub from SCC
**Solutions:**
1. Generate SSH key: `ssh-keygen -t ed25519 -C "your_email@bu.edu"`
2. Add to SSH agent: `ssh-add ~/.ssh/id_ed25519`
3. Copy public key: `cat ~/.ssh/id_ed25519.pub`
4. Add to GitHub: Settings → SSH and GPG keys → New SSH key

### VS Code Issues
**Problem:** VS Code not working properly on SCC OnDemand
**Solutions:**
1. Try refreshing the browser page
2. Request a new interactive session
3. Check if you have enough allocated resources
4. Clear browser cache and cookies

### Python Package Installation
**Problem:** `pip install` fails or packages not found
**Solutions:**
1. Use `--user` flag: `pip install --user package_name`
2. Check Python version: `python --version`
3. Try: `python -m pip install --user -r requirements.txt`
4. Load Python module: `module load python3`

## Data Download Issues

### Network/Connection Problems
**Problem:** Downloads fail or timeout
**Solutions:**
1. Check internet connection
2. Try smaller files first
3. Use `wget` or `curl` as alternative:
   ```bash
   wget "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=NC_012920&rettype=fasta&retmode=text" -O ancient_mtDNA.fasta
   ```
4. Check if SCC has firewall restrictions

### Invalid Accession IDs
**Problem:** NCBI returns empty or error responses
**Solutions:**
1. Verify accession ID format (e.g., NC_012920, not NC_012920.1)
2. Try alternative accessions:
   - NC_012920 (human mtDNA reference)
   - JQ701596 (ancient human mtDNA)
3. Check if sequence exists in NCBI database
4. Use browser to test URL manually

### File Permission Errors
**Problem:** Can't write downloaded files
**Solutions:**
1. Check directory permissions: `ls -la`
2. Create directory: `mkdir -p data`
3. Change permissions: `chmod 755 data`
4. Check disk space: `df -h`

## Code Debugging Issues

### FASTA Parsing Errors

**Problem:** Sequence parsing fails or gives wrong results
**Common Issues & Solutions:**

1. **Multi-line sequences not handled:**
   ```python
   # Wrong:
   sequence = line.strip()
   
   # Right:
   if line.startswith('>'):
       # New header
   else:
       sequence += line.strip()
   ```

2. **Headers included in sequence:**
   ```python
   # Add check to skip header lines
   if not line.startswith('>'):
       sequence += line.strip()
   ```

3. **Whitespace and newlines:**
   ```python
   # Clean sequence
   sequence = sequence.replace('\n', '').replace(' ', '').upper()
   ```

### GC Content Calculation Errors

**Problem:** GC content results seem wrong
**Common Issues:**

1. **Case sensitivity:**
   ```python
   sequence = sequence.upper()  # Convert to uppercase first
   gc_count = sequence.count('G') + sequence.count('C')
   ```

2. **Non-nucleotide characters:**
   ```python
   # Remove non-ATGC characters
   clean_seq = ''.join(c for c in sequence if c in 'ATGC')
   ```

3. **Division by zero:**
   ```python
   if len(sequence) == 0:
       return 0.0
   return (gc_count / len(sequence)) * 100
   ```

### File Path Issues

**Problem:** Scripts can't find files
**Solutions:**
1. Use absolute paths: `/full/path/to/file`
2. Check current directory: `pwd`
3. Use Path library:
   ```python
   from pathlib import Path
   fasta_file = Path("../data/ancient_mtDNA.fasta")
   if fasta_file.exists():
       # Process file
   ```

## Data Quality Issues

### Empty or Corrupted Files
**Problem:** Downloaded files are empty or corrupted
**Diagnosis:**
1. Check file size: `ls -lh data/`
2. View first few lines: `head data/ancient_mtDNA.fasta`
3. Check for FASTA header: `grep ">" data/ancient_mtDNA.fasta`

**Solutions:**
1. Re-download the file
2. Try different accession ID
3. Verify URL manually in browser

### Unexpected Sequence Content
**Problem:** Sequence doesn't look like DNA
**Diagnosis:**
1. Check for protein sequences (20 amino acids vs 4 nucleotides)
2. Look for unusual characters
3. Verify sequence type in NCBI

**Solutions:**
1. Ensure you're downloading nucleotide sequences
2. Use `rettype=fasta` not `rettype=fasta_cds_na`
3. Filter out non-ATGC characters

## Results Validation

### Sanity Checks for Results

**Sequence Length:**
- Mitochondrial genomes: typically 16,000-17,000 bp
- If much smaller: might be partial sequence
- If much larger: might include nuclear DNA

**GC Content:**
- Human mtDNA: typically ~44-45%
- If <20% or >80%: likely calculation error
- If exactly 25%: might be random/test sequence

**Base Composition:**
- Should add up to 100%
- No base should be 0% (unless very short sequence)
- Extreme values (>60% single base) indicate problems

## Performance Issues

### Slow Script Execution
**Problem:** Scripts take too long to run
**Solutions:**
1. Check file sizes: `ls -lh data/`
2. Use smaller test files first
3. Add progress indicators:
   ```python
   print(f"Processing {len(sequence)} nucleotides...")
   ```
4. Profile code to find bottlenecks

### Memory Issues
**Problem:** Script crashes with memory errors
**Solutions:**
1. Process files in chunks
2. Don't load entire file into memory at once
3. Use generators instead of lists
4. Request more memory in SCC job

## Git/GitHub Issues

### Commit Problems
**Problem:** Can't commit or push to GitHub
**Solutions:**
1. Configure git:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your_email@bu.edu"
   ```
2. Check repository status: `git status`
3. Add files: `git add .`
4. Commit: `git commit -m "Your message"`
5. Push: `git push origin main`

### Large File Issues
**Problem:** Git rejects large files
**Solutions:**
1. Check file sizes: `ls -lh`
2. Add to .gitignore if too large
3. Use Git LFS for large data files
4. Compress files before committing

## Getting Help

### When to Ask for Help
1. After trying solutions in this guide
2. When error messages are unclear
3. When results don't make biological sense
4. When stuck for more than 15-20 minutes

### How to Ask for Help Effectively
1. **Describe what you're trying to do**
2. **Share the exact error message**
3. **Show the relevant code**
4. **Explain what you've already tried**
5. **Include sample data if relevant**

### LLM Debugging Strategy
1. Copy exact error message to LLM
2. Include relevant code snippet
3. Mention you're working with FASTA files
4. Ask for specific debugging steps
5. Test suggested solutions one at a time

## Emergency Procedures

### If Everything Breaks
1. **Don't panic** - this is normal in computational work
2. **Save your work** - commit what you have
3. **Start fresh** - create new script file
4. **Use working examples** - copy from sample prompts
5. **Ask for help** - instructors are there to help

### Last Resort Solutions
1. Use the sample code from `docs/sample_prompts.md`
2. Work with a partner to compare approaches
3. Focus on getting basic functionality working first
4. Document what you tried (even if it didn't work)

Remember: The goal is learning, not perfection. Every error is a learning opportunity!
