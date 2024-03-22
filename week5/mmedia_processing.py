import matplotlib.pyplot as plt #4
import matplotlib.image as mpimg #4
import numpy as np
from scipy.io.wavfile import read, write

class MMedia_Processing:  #1
    def ImgProc(self, image_path): #2
        try:
            
            my_img = mpimg.imread(image_path) #3 #5

            # Display the image
            plt.figure(1)
            plt.imshow(my_img) #6
            #plt.title("Image")
            
            #plt.show() #6

            plt.figure(2)
            lum_img = my_img[:, :, 1]   #7
            plt.imshow(lum_img)   #8
            plt.title("Red") #8
            #plt.show()
            
            plt.figure(3) #9
            # Plot the histogram
            plt.hist(lum_img.ravel(), bins=256, range=(0.0, 255), fc='k', ec='k') #9

            # Add grid, title, xlabel, and ylabel
            plt.grid(True) #10
            plt.title("Histogram of Luminance Values") #10
            plt.xlabel("Luminance") #10
            plt.ylabel("Frequency") #10


        except FileNotFoundError:
            print(f"Error: Image file '{image_path}' not found.")

    def AudProc(self,audio_path): #2
        # Read in the audio file (replace 'Alone-Sistar.wav' with the actual file path)
        Fs, data = read(audio_path)

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
    image_file_path = "BigDataImage-1.jpg"  
    audio_file_path ='Alone-Sistar.wav'
    media_processor = MMedia_Processing()
    #media_processor.ImgProc(image_file_path)
    media_processor.AudProc(audio_file_path)

