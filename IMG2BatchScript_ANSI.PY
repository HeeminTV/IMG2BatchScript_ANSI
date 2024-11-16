import sys
from PIL import Image

def generate_batch_script(image_path, output_path):
    try:
        # opens what
        img = Image.open(image_path)
        width, height = img.size
        
        # why the uck
        if width < 16 or height < 16 or width > 200 or height > 400:
            print("Error: Image size must be at least 16x16 but less than 200x400.")
            return

        # fun fart
        with open(output_path, 'w', encoding='utf-8') as batch_file:
            # i emant part
            batch_file.write(f"@echo off\n")
            batch_file.write(f"mode {width + 1},{height + 1}\n\n")

            # ansi shit
            pixels = img.load()
            for y in range(0, height, 2):  # WHAT
                line = "echo "
                for x in range(width):
                    r, g, b = pixels[x, y][:3]
                    line += f"\x1b[48;2;{r};{g};{b}m "
                batch_file.write(line + "\n")
            
            # ANSI fuck
            batch_file.write("echo \x1b[0m\n")
            batch_file.write("pause\n")

        print(f"Batch script '{output_path}' has been generated.")








    except Exception as e:
        print(f"Error: {e}")

# i hate english for some reason
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python image_to_batch.py <input_image> <output_batch>")
    else:
        generate_batch_script(sys.argv[1], sys.argv[2])
