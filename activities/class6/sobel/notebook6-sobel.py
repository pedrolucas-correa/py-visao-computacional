#%%
import cv2 as cv
import matplotlib.pyplot as plt

def main(argv):
    
    scale = 1
    delta = 0
    ddepth = cv.CV_16S
    
    
    if len(argv) < 1:
        print ('Not enough parameters')
        print ('Usage:\nmorph_lines_detection.py < path_to_image >')
        return -1

    # Load the image
    img = cv.imread(argv[0], 0)
    # Check if image is loaded fine
    if img is None:
        print ('Error opening image: ' + argv[0])
        return -1
    
    # Reduce noise
    img = cv.GaussianBlur(img, (3, 3), 0)
    
    # Sobel Operator
    grad_x = cv.Sobel(img, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    grad_y = cv.Sobel(img, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    
    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)
    
    
    # Gradient
    grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.2, 0)


    # Show image
    plt.imshow(grad, cmap='gray')
    cv.imwrite('Sobel Image.jpg', grad );
    
    return 0

if __name__ == "__main__":
    main(['desk.jpg'])
# %%
