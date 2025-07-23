# Data Directory

This directory is where your downloaded ancient DNA data will be stored.

## Expected Files

After running `src/download_data.py`, you should have:

- `ancient_mtDNA.fasta` - The downloaded ancient mitochondrial genome sequence

## Data Sources

Recommended databases for ancient DNA sequences:
- **Allen Ancient DNA Resource (AADR)** - Curated ancient genomic data
- **NCBI Nucleotide Database** - Large collection of sequence data
- **European Nucleotide Archive (ENA)** - European sequence repository

## File Formats

- **FASTA format** (`.fasta`, `.fa`, `.fas`)
  - Text-based format for nucleotide sequences
  - Starts with header line beginning with `>`
  - Followed by sequence data (can be multi-line)

## Data Handling Best Practices

1. **Keep original data unchanged** - Don't modify downloaded files
2. **Document data sources** - Record where data came from
3. **Check file integrity** - Verify downloads completed successfully
4. **Respect data usage policies** - Follow database terms of use

## Troubleshooting

If you don't see files here after running the download script:
1. Check if the download script ran without errors
2. Verify your internet connection
3. Check if the accession ID is valid
4. Look for error messages in the console output
