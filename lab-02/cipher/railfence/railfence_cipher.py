class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # 1: down, -1: up
        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        # Calculate the length of each rail first
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1
        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # Distribute the cipher_text into rails based on calculated lengths
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[start:start + length])) # Convert to list to allow pop/slice
            start += length

        # Reconstruct the plain_text by traversing the rails in a zigzag pattern
        plain_text = ""
        rail_index = 0
        direction = 1
        for _ in range(len(cipher_text)):
            # Take the next character from the current rail
            plain_text += rails[rail_index].pop(0) 
            
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
            
        return plain_text