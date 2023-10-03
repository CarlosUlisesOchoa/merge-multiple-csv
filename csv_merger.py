import os
import argparse

def process_line(line, num_expected_cols):
    line = line.strip()
    cols = line.split(",")
    
    # Filter out lines with incorrect number of columns
    if len(cols) != num_expected_cols:
        return None, None
    
    # Use the first column as a unique identifier for duplicate filtering
    unique_id = cols[0].replace('"', '')
    
    return unique_id, line + "\n"

def main():
    parser = argparse.ArgumentParser(description='Merge CSV files.')
    parser.add_argument('-n', '--name', default='merged', help='Name of the output file (default: merged)')
    parser.add_argument('-d', '--delete', action='store_true', help='Delete input files after merging (default: False)')
    args = parser.parse_args()
    
    # Check if 'input' and 'output' directories exist, create if not
    if not os.path.exists('input'):
        os.makedirs('input')
        
    if not os.path.exists('output'):
        os.makedirs('output')
    
    output_filename = os.path.join('output', f"{args.name}.csv")
    seen_ids = set()
    num_expected_cols = 0
    header_written = False

    with open(output_filename, 'w', encoding='utf-8') as f_out:
        
        for filename in os.listdir("input"):
            if filename.endswith(".csv"):
                with open(os.path.join("input", filename), 'r', encoding='utf-8') as f_in:
                    
                    # Read header
                    header = f_in.readline().strip()
                    if not header_written:
                        f_out.write(header + "\n")
                        header_written = True
                        num_expected_cols = len(header.split(","))
                    
                    # Process lines
                    for line in f_in:
                        unique_id, processed_line = process_line(line, num_expected_cols)
                        if processed_line and unique_id not in seen_ids:
                            seen_ids.add(unique_id)
                            f_out.write(processed_line)
                            
                    # Remove the input file after processing if -d flag is set
                    if args.delete:
                        os.remove(os.path.join("input", filename))

if __name__ == "__main__":
    main()
