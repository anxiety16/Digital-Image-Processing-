import cv2

def get_neighbors(image, x, y):
    rows, cols = image.shape[:2]
    
    # 4-Point Neighbors
    N4 = []
    if x + 1 < rows: N4.append(image[x + 1, y])
    if x - 1 >= 0: N4.append(image[x - 1, y])
    if y + 1 < cols: N4.append(image[x, y + 1])
    if y - 1 >= 0: N4.append(image[x, y - 1])
    print("N4:", N4)
    
    # 8-Point Neighbors
    N8 = N4.copy()
    if x + 1 < rows and y + 1 < cols: N8.append(image[x + 1, y + 1])
    if x + 1 < rows and y - 1 >= 0: N8.append(image[x + 1, y - 1])
    if x - 1 >= 0 and y - 1 >= 0: N8.append(image[x - 1, y - 1])
    if x - 1 >= 0 and y + 1 < cols: N8.append(image[x - 1, y + 1])
    print("N8:", N8)
    
    # Diagonal Neighbors
    ND = []
    if x + 1 < rows and y + 1 < cols: ND.append(image[x + 1, y + 1])
    if x + 1 < rows and y - 1 >= 0: ND.append(image[x + 1, y - 1])
    if x - 1 >= 0 and y - 1 >= 0: ND.append(image[x - 1, y - 1])
    if x - 1 >= 0 and y + 1 < cols: ND.append(image[x - 1, y + 1])
    print("ND:", ND)

def display_image(image, x, y):
    display_img = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    cv2.circle(display_img, (y, x), 5, (0, 0, 255), -1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    # Load an image in grayscale
    path = ("Mahinay.jpg")
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Error: Could not load image.")
        return
    resized_image = cv2.resize(image, (5, 5), interpolation=cv2.INTER_AREA)
    print(f"Output \n a= \n{resized_image}")
    print(f"\nImage Loaded Successfully with dimensions of {image.shape[0]}x{image.shape[1]}")
    
    while True:
        try:
            x = int(input(f"Enter the row size of the matrix (0-{image.shape[0]}): "))
            y = int(input(f"Enter the column size of the matrix (0-{image.shape[1]}): "))
            if 0 <= x < image.shape[0] and 0 <= y < image.shape[1]:
                break
            else:
                print("Invalid index. \nPlease enter values within the image dimensions(480-1= dimension 479).")
        except ValueError:
            print("Invalid input. \nPlease enter numerical values.")
    
    print("Element Value:", image[x, y])
    get_neighbors(image, x, y)
    display_image(image, x, y)
    
if __name__ == "__main__":
    main()


