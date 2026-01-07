#!/usr/bin/env python3
import base64
import urllib.parse
import binascii
import os

def base64_encode(text, iterations=1):
    """Apply base64 encoding multiple times"""
    result = text
    for _ in range(iterations):
        result = base64.b64encode(result.encode()).decode()
    return result

def hex_encode(text, iterations=1):
    """Apply hex encoding multiple times"""
    result = text
    for _ in range(iterations):
        result = binascii.hexlify(result.encode()).decode()
    return result

def url_encode(text, iterations=1):
    """Apply URL encoding multiple times"""
    result = text
    for _ in range(iterations):
        result = urllib.parse.quote(result)
    return result

def ascii_encode(text, iterations=1):
    """Convert to ASCII decimal representation"""
    result = text
    for _ in range(iterations):
        # Convert each character to its ASCII decimal value
        result = ' '.join(str(ord(char)) for char in result)
    return result

def binary_encode(text, iterations=1):
    """Convert to binary representation"""
    result = text
    for _ in range(iterations):
        # Convert each character to 8-bit binary
        result = ' '.join(format(ord(char), '08b') for char in result)
    return result

def rot13_encode(text, iterations=1):
    """Apply ROT13 encoding multiple times"""
    result = text
    for _ in range(iterations):
        encoded = []
        for char in result:
            if 'a' <= char <= 'z':
                encoded.append(chr(((ord(char) - ord('a') + 13) % 26) + ord('a')))
            elif 'A' <= char <= 'Z':
                encoded.append(chr(((ord(char) - ord('A') + 13) % 26) + ord('A')))
            else:
                encoded.append(char)
        result = ''.join(encoded)
    return result

def reverse_encode(text, iterations=1):
    """Reverse the string multiple times"""
    result = text
    for _ in range(iterations):
        result = result[::-1]
    return result

def main():
    print("=== Password List Encoder ===")
    
    # Wordlist selection
    print("\nWordlist Source:")
    print("1. Use default rockyou.txt")
    print("2. Use custom wordlist file")
    
    wordlist_choice = input("\nSelect wordlist source (1 or 2): ").strip()
    
    wordlist_path = ""
    if wordlist_choice == "1":
        wordlist_path = '/usr/share/wordlists/rockyou.txt'
    elif wordlist_choice == "2":
        wordlist_path = input("Enter full path to custom wordlist: ").strip()
        if not os.path.exists(wordlist_path):
            print(f"Error: File '{wordlist_path}' not found!")
            return
    else:
        print("Invalid choice. Using default rockyou.txt.")
        wordlist_path = '/usr/share/wordlists/rockyou.txt'
    
    # Encoding type selection
    print("\nSelect encoding type:")
    print("1. Base64")
    print("2. Hex")
    print("3. URL Encoding")
    print("4. ASCII Decimal")
    print("5. Binary")
    print("6. ROT13")
    print("7. Reverse")
    
    try:
        choice = int(input("\nEnter type (1-7): ").strip())
        if choice not in range(1, 8):
            print("Invalid choice. Using Base64 as default.")
            choice = 1
    except ValueError:
        print("Invalid input. Using Base64 as default.")
        choice = 1
    
    # Iterations input
    try:
        iterations = int(input("How many times you want to encode it?: ").strip())
        if iterations < 1:
            print("Must be at least 1. Setting to 1.")
            iterations = 1
    except ValueError:
        print("Invalid input. Using 1 iteration.")
        iterations = 1
    
    # Output path
    output_path = input("Enter output file path: ").strip()
    if not output_path:
        output_path = "encoded-wordlist.txt"
    
    # Encoding function mapping
    encoders = {
        1: base64_encode,
        2: hex_encode,
        3: url_encode,
        4: ascii_encode,
        5: binary_encode,
        6: rot13_encode,
        7: reverse_encode
    }
    
    encoder = encoders[choice]
    encoder_names = ["Base64", "Hex", "URL", "ASCII Decimal", "Binary", "ROT13", "Reverse"]
    encoder_name = encoder_names[choice-1]
    
    # Additional options
    print("\nAdditional Options:")
    print("1. Apply URL encoding to final result (default: Yes)")
    print("2. Skip URL encoding")
    
    url_encode_choice = input("Apply URL encoding? (1 or 2): ").strip()
    apply_url_encode = url_encode_choice != "2"
    
    print(f"\nUsing wordlist: {wordlist_path}")
    print(f"Encoding with {encoder_name} x{iterations}")
    if apply_url_encode:
        print("Final output will be URL encoded")
    
    try:
        # Fixed: removed duplicate 'errors' parameter
        with open(wordlist_path, 'r', encoding='utf-8', errors='replace') as f:
            total_lines = sum(1 for _ in f)
            f.seek(0)  # Reset file pointer
            
            with open(output_path, 'w', encoding='utf-8') as out_file:
                count = 0
                for line in f:
                    pwd = line.strip()
                    if pwd:  # Skip empty lines
                        # Apply the selected encoding
                        encoded = encoder(pwd, iterations)
                        
                        # Apply URL encoding if selected
                        if apply_url_encode:
                            final_output = urllib.parse.quote(encoded)
                        else:
                            final_output = encoded
                        
                        out_file.write(final_output + "\n")
                        count += 1
                        
                        # Progress indicator
                        if count % 10000 == 0:
                            percentage = (count / total_lines) * 100
                            print(f"Processed {count}/{total_lines} passwords ({percentage:.1f}%)...")
                
                print(f"\n✓ Done! Encoded {count} passwords to {output_path}")
                print(f"  Wordlist: {wordlist_path}")
                print(f"  Encoding: {encoder_name} x{iterations}")
                if apply_url_encode:
                    print(f"  Final step: URL encoding")
                
                # Show file size
                if os.path.exists(output_path):
                    size = os.path.getsize(output_path)
                    if size < 1024:
                        print(f"  Output size: {size} bytes")
                    elif size < 1024*1024:
                        print(f"  Output size: {size/1024:.2f} KB")
                    else:
                        print(f"  Output size: {size/(1024*1024):.2f} MB")
    
    except FileNotFoundError:
        print(f"Error: Wordlist file '{wordlist_path}' not found!")
        if wordlist_choice == "1":
            print("The default rockyou.txt might not be installed.")
            print("You can install it with: sudo apt install wordlists")
            print("Or use your custom wordlist with option 2.")
    except PermissionError:
        print(f"Error: Permission denied accessing '{wordlist_path}'")
    except UnicodeDecodeError:
        print("Error: Could not decode the wordlist file. Try using a different encoding.")
        print("You can try running the script with a wordlist that uses ASCII or UTF-8 encoding.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print(f"Error type: {type(e).__name__}")

if __name__ == "__main__":
    main()
