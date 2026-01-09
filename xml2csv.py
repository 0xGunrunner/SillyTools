import xml.etree.ElementTree as ET
import csv
import sys
import os

def column_to_index(col_letter: str) -> int:
    """Convert Excel column letter (A, B, C) to zero-based index."""
    index = 0
    for char in col_letter.upper():
        index = index * 26 + (ord(char) - ord('A') + 1)
    return index - 1

def parse_shared_strings(ss_file: str = None) -> list:
    """Parse shared strings XML file."""
    if not ss_file or not os.path.exists(ss_file):
        return []
    
    try:
        tree = ET.parse(ss_file)
        root = tree.getroot()
    except ET.ParseError:
        return []
    
    ns = {'ss': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    
    shared_strings = []
    for si in root.findall('.//ss:si', ns):
        text_elements = si.findall('.//ss:t', ns)
        if text_elements:
            cell_text = ''.join([t.text if t.text else '' for t in text_elements])
        else:
            t_elem = si.find('.//ss:t', ns)
            cell_text = t_elem.text if t_elem is not None and t_elem.text else ''
        shared_strings.append(cell_text)
    
    return shared_strings

def parse_worksheet(worksheet_file: str, shared_strings: list) -> list:
    """Parse worksheet XML file and return 2D list of cell values."""
    try:
        tree = ET.parse(worksheet_file)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"Error parsing worksheet XML: {e}")
        return []
    
    ns = {'ss': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    
    # Parse hyperlinks
    hyperlinks = {}
    for hyperlink in root.findall('.//ss:hyperlink', ns):
        ref = hyperlink.get('ref')
        display = hyperlink.get('display')
        if ref and display:
            hyperlinks[ref] = display
    
    # Parse cell data
    max_row = 0
    max_col = 0
    cell_data = {}
    
    for row_elem in root.findall('.//ss:row', ns):
        row_num = int(row_elem.get('r')) - 1
        
        for cell_elem in row_elem.findall('ss:c', ns):
            cell_ref = cell_elem.get('r')
            cell_type = cell_elem.get('t', 'n')
            
            col_letter = ''.join([c for c in cell_ref if c.isalpha()])
            col_idx = column_to_index(col_letter)
            
            max_row = max(max_row, row_num)
            max_col = max(max_col, col_idx)
            
            value_elem = cell_elem.find('ss:v', ns)
            if value_elem is not None:
                raw_value = value_elem.text if value_elem.text else ''
            else:
                raw_value = ''
            
            cell_value = ""
            if cell_type == 's':  # Shared string
                try:
                    idx = int(raw_value)
                    if idx < len(shared_strings):
                        cell_value = shared_strings[idx]
                except (ValueError, IndexError):
                    cell_value = raw_value
            elif cell_type == 'inlineStr':
                t_elem = cell_elem.find('.//ss:t', ns)
                if t_elem is not None:
                    cell_value = t_elem.text if t_elem.text else ''
                else:
                    cell_value = raw_value
            else:
                cell_value = raw_value
            
            if cell_ref in hyperlinks:
                cell_value = hyperlinks[cell_ref]
            
            cell_data[(row_num, col_idx)] = cell_value
    
    # Build grid
    grid = []
    for r in range(max_row + 1):
        row = []
        for c in range(max_col + 1):
            row.append(cell_data.get((r, c), ""))
        grid.append(row)
    
    return grid

def main():
    """Main function with command-line arguments."""
    if len(sys.argv) < 3:
        print("Usage: python3 xml2csv.py <worksheet.xml> [sharedstrings.xml] <output.csv>")
        print("Examples:")
        print("  python3 xml2csv.py sheet.xml sharedStrings.xml output.csv")
        print("  python3 xml2csv.py sheet.xml output.csv (without shared strings)")
        sys.exit(1)
    
    # Parse arguments
    if len(sys.argv) == 3:
        # Only worksheet and output specified
        worksheet_file = sys.argv[1]
        output_file = sys.argv[2]
        shared_strings_file = None
    else:
        # worksheet, shared strings, and output specified
        worksheet_file = sys.argv[1]
        shared_strings_file = sys.argv[2]
        output_file = sys.argv[3]
    
    # Check input files
    if not os.path.exists(worksheet_file):
        print(f"Error: Worksheet file '{worksheet_file}' not found")
        sys.exit(1)
    
    if shared_strings_file and not os.path.exists(shared_strings_file):
        print(f"Warning: Shared strings file '{shared_strings_file}' not found")
        shared_strings_file = None
    
    # Parse and convert
    print(f"Parsing worksheet: {worksheet_file}")
    if shared_strings_file:
        print(f"Using shared strings: {shared_strings_file}")
    
    shared_strings = parse_shared_strings(shared_strings_file)
    data_grid = parse_worksheet(worksheet_file, shared_strings)
    
    # Write to CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data_grid)
    
    print(f"CSV saved to: {output_file}")
    print(f"Dimensions: {len(data_grid)} rows × {len(data_grid[0]) if data_grid else 0} columns")

if __name__ == "__main__":
    main()
