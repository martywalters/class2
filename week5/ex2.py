import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Read in the image (replace 'your_image.png' with the actual image file)
img = mpimg.imread('BigDataImage-1.jpg')

# Select the Red component (R) of the image
lum_img = img[:, :, 0]

# Display the new image with a title
plt.imshow(lum_img)
plt.title("Red Component of the Image")
plt.axis('off')  # Turn off axis ticks
plt.show()

# Plot the histogram of the Red component
plt.figure(2)
plt.hist(lum_img.ravel(), bins=256, range=(0.0, 255), fc='k', ec='k')
plt.title("Histogram of Red Component")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
