def menu():
    while True:
        print("1. /X to Mask")
        print("2. Mask to /X")
        print("3. Address to Network and Broadcast")
        print("4. Hosts Usable")
        print("5. Address to Network and Broadcast using CIDR")
        print("6. Convert IP to Binary and Vice Versa")
        print("7. Calculate IP Address Class")
        print("8. Check if IP is Private or Public")
        print("9. Find Next Subnet")
        print("10. Exit")

        choice = input("Choose an option: ")
        match choice:
            case "1":
                X = int(input("Enter CIDR (X in /X): "))
                print(XtoMASK(X))
                input("Press Enter to continue...")
            case "2":
                mask = input("Enter Mask (e.g., 255.255.255.0): ")
                print(MasktoX(mask))
                input("Press Enter to continue...")

            case "3":
                ip_address = input("Enter IP Address (e.g., 192.168.1.10): ")
                subnet_mask = input("Enter Subnet Mask (e.g., 255.255.255.0): ")
                network, broadcast = calculate_network_and_broadcast(ip_address, subnet_mask)
                print(f"Network Address: {network}, Broadcast Address: {broadcast}")
                input("Press Enter to continue...")

            case "4":
                subnet_mask = input("Enter Subnet Mask (e.g., 255.255.255.0): ")
                print(hosts_usable(subnet_mask))
                input("Press Enter to continue...")

            case "5":
                ip_address = input("Enter IP Address (e.g., 192.168.1.10): ")
                cidr = int(input("Enter CIDR (e.g., 24 for /24): "))
                subnet_mask = XtoMASK(cidr)
                network, broadcast = calculate_network_and_broadcast(ip_address, subnet_mask)
                print(f"Network Address: {network}, Broadcast Address: {broadcast}, Subnet Mask: {subnet_mask}")
                input("Press Enter to continue...")

            case "6":
                ip = input("Enter IP Address: ")
                choice = input("Convert to (1) Binary or (2) Decimal: ")
                if choice == '1':
                    print(ip_to_binary(ip))
                    input("Press Enter to continue...")
                elif choice == '2':
                    print(binary_to_ip(ip))
                    input("Press Enter to continue...")
                else:
                    print("Invalid choice")
                    input("Press Enter to continue...")
            case "7":
                ip = input("Enter IP Address: ")
                print(calculate_ip_class(ip))
                input("Press Enter to continue...")

            case "8":
                ip = input("Enter IP Address: ")
                print("Private" if is_private_ip(ip) else "Public")
                input("Press Enter to continue...")

            case "9":
                ip_address = input("Enter IP Address: ")
                subnet_mask = input("Enter Subnet Mask: ")
                print(find_next_subnet(ip_address, subnet_mask))
                input("Press Enter to continue...")

            case "10":
                print("Exiting...")
                break
            case _:
                print("Invalid option")


def MasktoX(decimal_mask):

        # Split the decimal mask into its constituent parts
        mask_parts = decimal_mask.split('.')

        # Convert each part to binary and concatenate
        binary_mask = ''.join(format(int(part), '08b') for part in mask_parts)

        # Count the number of 1s in the binary representation
        cidr = binary_mask.count('1')

        return f"/{cidr}"
def XtoMASK(mask_bits):
        # Validate input
        if not (0 <= mask_bits <= 32):
            return "Invalid input: the number must be between 0 and 32"

        # Create a binary string of 32 bits with 'mask_bits' number of 1s
        binary_mask = '1' * mask_bits + '0' * (32 - mask_bits)

        # Convert binary string to four decimal numbers
        decimal_mask = [str(int(binary_mask[i:i + 8], 2)) for i in range(0, 32, 8)]

        return '.'.join(decimal_mask)

def ip_to_binary(ip):
    """Convert an IP address from decimal to binary format."""
    return ''.join(format(int(octet), '08b') for octet in ip.split('.'))

def binary_to_ip(binary):
    """Convert a binary string to an IP address in decimal format."""
    return '.'.join(str(int(binary[i:i+8], 2)) for i in range(0, 32, 8))

def calculate_network_and_broadcast(ip_address, subnet_mask):
    """
    Calculate the network and broadcast address from an IP address and subnet mask.
    """
    # Convert IP and subnet mask to binary
    ip_binary = ip_to_binary(ip_address)
    subnet_binary = ip_to_binary(subnet_mask)

    # Calculate network address (IP AND Subnet Mask)
    network_binary = ''.join('1' if ip_binary[i] == '1' and subnet_binary[i] == '1' else '0' for i in range(32))
    network_address = binary_to_ip(network_binary)

    # Calculate broadcast address (Network Address OR Inverted Subnet Mask)
    inverted_subnet = ''.join('0' if bit == '1' else '1' for bit in subnet_binary)
    broadcast_binary = ''.join('1' if network_binary[i] == '1' or inverted_subnet[i] == '1' else '0' for i in range(32))
    broadcast_address = binary_to_ip(broadcast_binary)

    return network_address, broadcast_address

def hosts_usable(subnet_mask):

    # Count the number of 0s in the subnet mask's binary form
    zeros = ip_to_binary(subnet_mask).count('0')
    # Subtract 2 for the network and broadcast addresses
    return (2 ** zeros) - 2

def calculate_ip_class(ip):
    first_octet = int(ip.split('.')[0])
    if first_octet >= 1 and first_octet <= 126:
        return "Class A"
    elif first_octet >= 128 and first_octet <= 191:
        return "Class B"
    elif first_octet >= 192 and first_octet <= 223:
        return "Class C"
    elif first_octet >= 224 and first_octet <= 239:
        return "Class D (Multicast)"
    elif first_octet >= 240 and first_octet <= 255:
        return "Class E (Experimental)"
    else:
        return "Invalid IP Class"

def is_private_ip(ip):
    first_octet, second_octet, *_ = [int(o) for o in ip.split('.')]
    return ((first_octet == 10) or
            (first_octet == 172 and 16 <= second_octet <= 31) or
            (first_octet == 192 and second_octet == 168))

def find_next_subnet(ip_address, subnet_mask):
    # Convertir l'adresse IP et le masque de sous-réseau en binaire
    ip_binary = ip_to_binary(ip_address)
    mask_binary = ip_to_binary(subnet_mask)

    # Calculer l'adresse réseau
    network_binary = ''.join('1' if ip_binary[i] == '1' and mask_binary[i] == '1' else '0' for i in range(32))
    network_address = binary_to_ip(network_binary)

    # Ajouter 1 au dernier octet de l'adresse réseau pour obtenir l'adresse du prochain sous-réseau
    network_octets = [int(octet) for octet in network_address.split('.')]
    network_octets[-1] += 1

    # Gérer le débordement
    for i in range(3, -1, -1):
        if network_octets[i] == 256:
            network_octets[i] = 0
            if i > 0:
                network_octets[i - 1] += 1

    return '.'.join(map(str, network_octets))

# Fonctions auxiliaires existantes: ip_to_binary et binary_to_ip


def main ():
    menu()
main()