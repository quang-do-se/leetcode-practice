def get_twos_complement_binary(number, bit_length):
    if number >= 0:
        # For positive numbers, simply get the binary and pad with leading zeros
        return bin(number)[2:].zfill(bit_length)
    else:
        # For negative numbers, calculate two's complement
        # 1. Take the absolute value
        abs_number = abs(number)
        # 2. Invert the bits of the positive equivalent (one's complement)
        #    This is done by XORing with a mask of all 1s
        mask = (1 << bit_length) - 1
        ones_complement = abs_number ^ mask
        # 3. Add 1 to get two's complement
        twos_complement = ones_complement + 1
        # 4. Convert to binary and ensure correct length
        return bin(twos_complement)[2:].zfill(bit_length)

# Example usage:
negative_number = -3
bit_length = 8  # Representing in 8 bits

twos_complement_representation = get_twos_complement_binary(negative_number, bit_length)
print(f"The two's complement binary of {negative_number} in {bit_length} bits is: {twos_complement_representation}")

