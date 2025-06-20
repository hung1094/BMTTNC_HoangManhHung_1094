import sys
from PIL import Image

def encode_image(image_path, message):
    img = Image.open(image_path)
    width, height = img.size
    
    # Chuyển đổi tin nhắn thành chuỗi bit
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    # Thêm dấu hiệu kết thúc tin nhắn (EOF marker)
    binary_message += '11111111111110' 

    data_index = 0
    # Lặp qua từng pixel
    for row in range(height):
        for col in range(width):
            # Lấy giá trị RGB của pixel
            pixel = list(img.getpixel((col, row)))

            # Lặp qua từng kênh màu (R, G, B)
            for color_channel in range(3):
                if data_index < len(binary_message):
                    # Thay đổi bit cuối cùng của kênh màu bằng bit của tin nhắn
                    # pixel[color_channel] là giá trị thập phân của kênh màu
                    # format(pixel[color_channel], '08b') chuyển nó thành chuỗi nhị phân 8 bit
                    # [-1] lấy bit cuối cùng (ít quan trọng nhất)
                    # Sau đó, bit cuối cùng này được thay thế bằng bit từ binary_message
                    # int(..., 2) chuyển lại chuỗi nhị phân thành số thập phân
                    pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1
                else:
                    # Nếu đã nhúng hết tin nhắn, thoát khỏi vòng lặp kênh màu
                    break
            
            # Cập nhật pixel đã thay đổi vào ảnh
            img.putpixel((col, row), tuple(pixel))

            # Nếu đã nhúng hết tin nhắn, thoát khỏi vòng lặp pixel
            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break

    encoded_image_path = 'encoded_image.png'
    img.save(encoded_image_path)
    print("Steganography complete. Encoded image saved as", encoded_image_path)

def main():
    # Kiểm tra số lượng đối số dòng lệnh
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image_path> <message>")
        return

    # Lấy đường dẫn ảnh và tin nhắn từ đối số dòng lệnh
    image_path = sys.argv[1]
    message = sys.argv[2]
    
    # Gọi hàm để nhúng tin nhắn vào ảnh
    encode_image(image_path, message)

if __name__ == "__main__":
    main()