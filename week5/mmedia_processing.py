import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy.io.wavfile import read, write

class MMedia_Processing:
    def ImgProc(self, image_path):
        """
        Reads and processes an image file.

        Args:
            image_path (str): Path to the image file.

        Returns:
            None
        """
        try:
            # Read the image using mpimg
            img = mpimg.imread(image_path)

            # Display the image
            plt.imshow(img)
            plt.title("Image")
            plt.show()

            # Process the image further if needed
            # ...
            red_component = img[:, :, 0]  # Select the red channel (0 corresponds to red)
            plt.imshow(red_component, cmap='gray')  # Use a grayscale colormap
            plt.title("Red Component")
            plt.show()

        except FileNotFoundError:
            print(f"Error: Image file '{image_path}' not found.")

    def AudProc(self):
        # Read in the audio file (replace 'Alone-Sistar.wav' with the actual file path)
        Fs, data = read('Alone-Sistar.wav')

        # Plot the waveform
        plt.figure(figsize=(10, 6))
        plt.plot(data)
        plt.title("Waveform of Test Audio")
        plt.xlabel("Sample Index")
        plt.ylabel("Amplitude")
        plt.grid(True)
        plt.show()

        # Flip the data to play the track backwards
        reversed_data = np.flip(data)

        # Save the reversed data to a new file
        write('Alone-Sistar-Reversed.wav', Fs, reversed_data)

        print("Reversed audio saved as 'Alone-Sistar-Reversed.wav'")

        
# Example usage
if __name__ == "__main__":
    image_file_path = "BigDataImage-1.jpg"  # Replace with the actual image file path
    media_processor = MMedia_Processing()
    #media_processor.ImgProc(image_file_path)
    media_processor.AudProc()

