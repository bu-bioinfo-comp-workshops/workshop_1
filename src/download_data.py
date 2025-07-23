#!/usr/bin/env python3
"""
Workshop 1: Download Ancient DNA Data
=====================================

This script downloads an ancient mitochondrial genome FASTA file from a public database.

Your task: Complete the functions below to download ancient DNA data.

Author: [Your Name]
Date: [Date]
"""

import requests
import os
from pathlib import Path


def download_fasta_from_ncbi(accession_id, output_file):
    """
    Download a FASTA sequence from NCBI using an accession ID.
    
    Args:
        accession_id (str): NCBI accession number (e.g., 'NC_012920')
        output_file (str): Path where the FASTA file should be saved
    
    Returns:
        bool: True if download successful, False otherwise
    
    TODO: Implement this function
    Hint: Use NCBI's efetch API: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi
    """
    # TODO: Construct the NCBI efetch URL
    # Format: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id={accession}&rettype=fasta&retmode=text
    
    # TODO: Make the HTTP request
    
    # TODO: Check if the request was successful
    
    # TODO: Save the content to the output file
    
    # TODO: Return True if successful, False otherwise
    pass


def download_sample_ancient_mtdna():
    """
    Download a sample ancient mitochondrial DNA sequence.
    
    This function downloads a well-known ancient mtDNA sequence for analysis.
    You can modify this to download different sequences.
    
    Returns:
        str: Path to the downloaded FASTA file
    """
    # Create data directory if it doesn't exist
    data_dir = Path("../data")
    data_dir.mkdir(exist_ok=True)
    
    # Sample ancient mtDNA accession (you can change this)
    # NC_012920 is the human mitochondrial reference genome
    # For a real ancient sample, you might use a different accession
    sample_accession = "NC_012920"  # TODO: Replace with actual ancient DNA accession
    output_file = data_dir / "ancient_mtDNA.fasta"
    
    print(f"Downloading ancient mtDNA sequence: {sample_accession}")
    print(f"Saving to: {output_file}")
    
    # TODO: Call your download function
    success = download_fasta_from_ncbi(sample_accession, str(output_file))
    
    if success:
        print("✅ Download successful!")
        return str(output_file)
    else:
        print("❌ Download failed!")
        return None


def verify_download(fasta_file):
    """
    Verify that the downloaded FASTA file is valid.
    
    Args:
        fasta_file (str): Path to the FASTA file
    
    Returns:
        bool: True if file is valid, False otherwise
    """
    # TODO: Check if file exists
    
    # TODO: Check if file is not empty
    
    # TODO: Check if file starts with '>' (FASTA header)
    
    # TODO: Print basic file information (size, first line)
    
    pass


def main():
    """
    Main function to run the download process.
    """
    print("🧬 Workshop 1: Ancient DNA Data Download")
    print("=" * 50)
    
    # Download the sample data
    fasta_file = download_sample_ancient_mtdna()
    
    if fasta_file:
        # Verify the download
        if verify_download(fasta_file):
            print(f"✅ Successfully downloaded and verified: {fasta_file}")
            print("\nNext step: Run analyze_sequence.py to analyze this data!")
        else:
            print("⚠️  Download verification failed. Check the file.")
    else:
        print("❌ Failed to download data. Check your internet connection and try again.")


if __name__ == "__main__":
    main()


# SAMPLE LLM PROMPTS FOR THIS SCRIPT:
"""
1. Basic download prompt:
   "I need to download a FASTA file from NCBI using Python. Please help me write a function that takes an accession ID and downloads the sequence using the NCBI efetch API."

2. Error handling prompt:
   "Please add error handling to my NCBI download function to handle network errors, invalid accession IDs, and file writing errors."

3. File verification prompt:
   "I need a function to verify that a downloaded FASTA file is valid - it should check if the file exists, is not empty, and starts with a proper FASTA header."
"""
