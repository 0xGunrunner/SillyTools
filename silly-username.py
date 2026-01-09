#!/usr/bin/env python3
"""
Username Variation Generator
Generates common username formats from a list of first/last names.
Usage: python3 silly-username.py --in name.txt --out username.txt
"""

import argparse
import sys

def generate_variations(first, last):
    """Generate all username variations for a given first and last name."""
    variations = []
    
    # Lowercase versions
    f = first.lower()
    l = last.lower()
    fi = f[0]
    li = l[0]
    
    # Original case combinations
    variations.append(first + last)           # FergusSmith
    variations.append(first + "." + last)    # Fergus.Smith
    variations.append(first + "_" + last)    # Fergus_Smith
    variations.append(first[0] + last)       # FSmith
    variations.append(first[0] + "." + last) # F.Smith
    variations.append(first[0] + "_" + last) # F_Smith
    variations.append(first + last[0])       # FergusS
    variations.append(first + "." + last[0]) # Fergus.S
    variations.append(first + "_" + last[0]) # Fergus_S
    
    # All lowercase combinations
    variations.append(f + l)                 # fergussmith
    variations.append(f + "." + l)           # fergus.smith
    variations.append(f + "_" + l)           # fergus_smith
    variations.append(fi + l)                # fsmith
    variations.append(fi + "." + l)          # f.smith
    variations.append(fi + "_" + l)          # f_smith
    variations.append(f + li)                # ferguss
    variations.append(f + "." + li)          # fergus.s
    variations.append(f + "_" + li)          # fergus_s
    
    # Reversed combinations
    variations.append(last + first)           # SmithFergus
    variations.append(last + "." + first)     # Smith.Fergus
    variations.append(last + "_" + first)     # Smith_Fergus
    variations.append(l + f)                  # smithfergus
    variations.append(l + "." + f)            # smith.fergus
    variations.append(l + "_" + f)            # smith_fergus
    
    return variations

def process_names(names_list):
    """Process a list of name tuples and return all variations."""
    all_variations = []
    
    for first, last in names_list:
        variations = generate_variations(first, last)
        all_variations.extend(variations)
    
    # Remove duplicates and sort
    unique_variations = sorted(set(all_variations))
    return unique_variations

def read_names_from_file(filename):
    """Read names from a file, expecting format: First Last"""
    names = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split()
                    if len(parts) >= 2:
                        # Take first two parts as first and last name
                        names.append((parts[0], parts[1]))
                    else:
                        print(f"Warning: Invalid line format: {line}", file=sys.stderr)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)
    
    return names

def main():
    parser = argparse.ArgumentParser(
        description='Generate username variations from a list of names',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 silly-username.py --in names.txt --out usernames.txt
  python3 silly-username.py -i names.txt -o usernames.txt
        """
    )
    parser.add_argument('--in', '-i', dest='input_file', required=True,
                       help='Input file with names (format: "First Last" on each line)')
    parser.add_argument('--out', '-o', dest='output_file', required=True,
                       help='Output file for generated usernames')
    
    args = parser.parse_args()
    
    # Read names from input file
    names = read_names_from_file(args.input_file)
    
    if not names:
        print("Error: No valid names found in input file.", file=sys.stderr)
        sys.exit(1)
    
    print(f"Processing {len(names)} names...", file=sys.stderr)
    
    # Generate variations
    variations = process_names(names)
    
    # Write to output file
    try:
        with open(args.output_file, 'w') as f:
            for v in variations:
                f.write(v + '\n')
        print(f"Generated {len(variations)} unique usernames to {args.output_file}", file=sys.stderr)
    except Exception as e:
        print(f"Error writing to output file: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
