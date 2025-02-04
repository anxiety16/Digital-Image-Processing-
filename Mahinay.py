import cv2
import numpy as np
from matplotlib import pyplot as plt

def load_image(image_path):
    """Load an image and convert it from BGR to RGB."""
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Could not load image from {image_path}")
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def extract_channels(image):
    """Extract red, green, and blue components from an image."""
    red = image[:, :, 0]
    green = image[:, :, 1]
    blue = image[:, :, 2]
    return red, green, blue

def create_grayscale(image):
    """Convert an image to grayscale."""
    return cv2.cvtColor(cv2.cvtColor(image, cv2.COLOR_RGB2BGR), cv2.COLOR_BGR2GRAY)

def display_color_components(image):
    """Display the original image along with its color components."""
    red, green, blue = extract_channels(image)
    gray = create_grayscale(image)
    
    plt.figure(figsize=(12, 10))
    
    # Show original image
    plt.subplot(3, 2, 1)
    plt.imshow(image)
    plt.title("Original Image")
    plt.axis("off")
    
    # Show color components
    plt.subplot(3, 2, 2)
    plt.imshow(red, cmap='Reds')
    plt.title("Red Component")
    plt.axis("off")
    
    plt.subplot(3, 2, 3)
    plt.imshow(green, cmap='Greens')
    plt.title("Green Component")
    plt.axis("off")
    
    plt.subplot(3, 2, 4)
    plt.imshow(blue, cmap='Blues')
    plt.title("Blue Component")
    plt.axis("off")
    
    # Show grayscale image
    plt.subplot(3, 2, 5)
    plt.imshow(gray, cmap='gray')
    plt.title("Gray Image")
    plt.axis("off")
    
    plt.tight_layout()
    plt.show()

def display_complement_images(image):
    """Display the complement of the color and grayscale images."""
    gray = create_grayscale(image)
    color_complement = 255 - image
    grayscale_complement = 255 - gray
    plt.figure(figsize=(12, 10))
    
    # Original color image
    plt.subplot(2, 2, 1)
    plt.imshow(image, aspect='auto')
    plt.title("Color Image")
    plt.xticks([200, 400, 600])
    plt.yticks([400, 300, 200, 100])
    plt.axis("tight")
    # Complement of color image
    plt.subplot(2, 2, 2)
    plt.imshow(color_complement, aspect='auto')
    plt.title("Complement of Color Image")
    plt.xticks([200, 400, 600])
    plt.yticks([400, 300, 200, 100])
    plt.axis("tight")
   
    # Grayscale image
    plt.subplot(2, 2, 3)
    plt.imshow(gray, cmap='gray', aspect='auto')
    plt.title("Gray scale of color Image")
    plt.xticks([200, 400, 600 ])
    plt.yticks([400, 300, 200, 100])
    plt.axis("tight")
    # Complement of grayscale image
    plt.subplot(2, 2, 4)
    plt.imshow(grayscale_complement, cmap='gray', aspect='auto')
    plt.title("Complement of Gray Image")
    plt.xticks([200, 400, 600, ])
    plt.yticks([400, 300, 200, 100])
    plt.axis("tight")
    plt.tight_layout()
    plt.show()

def generate_patterns():
    """Generate and display different image patterns and operations."""
    a = np.ones((40, 40), dtype=np.uint8) * 255  # White block
    b = np.zeros((40, 40), dtype=np.uint8)       # Black block
    c = np.vstack([np.hstack([a, b]), np.hstack([b, a])])  # Checkerboard pattern
    d = np.vstack([np.hstack([b, b]), np.hstack([a, a])])  # Inverse Checkerboard
    
    # Perform operations
    A = 10 * (c + d)   # Addition
    M = cv2.multiply(c, d)  # Multiplication
    S = cv2.subtract(c, d)  # Subtraction
    D = cv2.divide(c, 4).astype(np.uint8)  # Division
    
    plt.figure(figsize=(12, 10))
    
    plt.subplot(3, 2, 1)
    plt.imshow(c, cmap='gray')
    plt.title("Pattern C")
    plt.axis("off")
    
    plt.subplot(3, 2, 2)
    plt.imshow(d, cmap='gray')
    plt.title("Pattern D")
    plt.axis("off")
    
    plt.subplot(3, 2, 3)
    plt.imshow(A, cmap='gray')
    plt.title("Addition (A)")
    plt.axis("off")
    
    plt.subplot(3, 2, 4)
    plt.imshow(M, cmap='gray')
    plt.title("Multiplication (M)")
    plt.axis("off")
    
    plt.subplot(3, 2, 5)
    plt.imshow(S, cmap='gray')
    plt.title("Subtraction (S)")
    plt.axis("off")
    
    plt.subplot(3, 2, 6)
    plt.imshow(D, cmap='gray')
    plt.title("Division (D)")
    plt.axis("off")
    
    plt.tight_layout()
    plt.show()

def main():
    """Main function to execute the image processing tasks."""
    try:
        image_path = "Mahinay.jpg"  # Specify the image path
        image = load_image(image_path)  # Load image
        
        display_color_components(image)  # Show RGB and grayscale images
        display_complement_images(image)  # Show color and grayscale complements
        generate_patterns()  # Generate and display patterns
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
