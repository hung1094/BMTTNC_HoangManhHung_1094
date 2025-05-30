class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I").upper()
        
        matrix_letters = []
        for char in key:
            if char not in matrix_letters:
                matrix_letters.append(char)

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for letter in alphabet:
            if letter not in matrix_letters:
                matrix_letters.append(letter)
        
        playfair_matrix = [matrix_letters[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        return -1, -1

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I").upper().replace(" ", "")

        processed_plain_text = ""
        i = 0
        while i < len(plain_text):
            processed_plain_text += plain_text[i]
            if i + 1 < len(plain_text):
                if plain_text[i] == plain_text[i+1]:
                    processed_plain_text += "X"
                else:
                    processed_plain_text += plain_text[i+1]
                    i += 1
            i += 1

        if len(processed_plain_text) % 2 != 0:
            processed_plain_text += "X"

        encrypted_text = ""
        for i in range(0, len(processed_plain_text), 2):
            pair = processed_plain_text[i:i+2]
            
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper().replace(" ", "")
        decrypted_raw_text = ""

        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                decrypted_raw_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_raw_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_raw_text += matrix[row1][col2] + matrix[row2][col1]

        banro = ""
        j = 0
        while j < len(decrypted_raw_text) - 2:
            if decrypted_raw_text[j] == decrypted_raw_text[j+2] and decrypted_raw_text[j+1] == 'X':
                banro += decrypted_raw_text[j]
                j += 3
            else:
                banro += decrypted_raw_text[j] + decrypted_raw_text[j+1]
                j += 2
        
        remaining_length = len(decrypted_raw_text) - j
        if remaining_length == 1:
            banro += decrypted_raw_text[j]
        elif remaining_length == 2:
            if decrypted_raw_text[j + 1] == "X":
                banro += decrypted_raw_text[j]
            else:
                banro += decrypted_raw_text[j] + decrypted_raw_text[j+1]

        if banro and banro[-1] == 'X':
            banro = banro[:-1]

        return banro