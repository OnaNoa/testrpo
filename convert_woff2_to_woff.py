from fontTools.ttLib.woff2 import decompress
import os
import argparse

def convert_woff2_to_woff(input_file, output_file=None):
    if not output_file:
        output_file = os.path.splitext(input_file)[0] + '.woff'
    
    try:
        decompress(input_file, output_file)
        print(f"Successfully converted to WOFF: {output_file}")
    except Exception as e:
        print(f"Conversion error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert WOFF2 fonts to WOFF format.")
    parser.add_argument("input", help="Path to the input WOFF2 file.")
    parser.add_argument("-o", "--output", help="Path to save the output WOFF file.")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print("Error: Input file does not exist.")
    else:
        convert_woff2_to_woff(args.input, args.output)
