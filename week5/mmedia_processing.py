import matplotlib.pyplot as plt #4 #12
import matplotlib.image as mpimg #4
import numpy as np #12
from scipy.io.wavfile import read, write #12

class MMedia_Processing:  #1
    def ImgProc(self, image_path): #2
        try:
            
            my_img = mpimg.imread(image_path) #3 #5

            plt.figure(1) #9
            
            plt.imshow(my_img) #6
            
            plt.figure(2) #9
            lum_img = my_img[:, :, 1] #7
            plt.imshow(lum_img)   #8 #9
            plt.title("Title : using img[:, :, 1]") #8 
            
            #extra credit 
            plt.figure(3)
            red_component = my_img[:, :, 0]
            red_image = np.zeros_like(my_img)
            red_image[:, :, 0] = red_component
            plt.imshow(red_image)
            plt.title('Extra Credit')
            plt.axis('off')  # Turn off axis

            plt.figure(4) #9
            
            # Plot the histogram
            plt.hist(lum_img.ravel(), bins=256, range=(0.0, 255), fc='k', ec='k') #9

            # Add grid, title, xlabel, and ylabel
            plt.grid(True) #10
            plt.title("Histogram") #10
            plt.xlabel("Luminance") #10
            plt.ylabel("Frequency") #10
            #plt.show()

        except FileNotFoundError:
            print(f"Error: Image file '{image_path}' not found.")

    def AudProc(self,audio_path): #2
        Fs, data = read(audio_path) #13
        plt.figure(5) #9
        # Plot the waveform
        #plt.figure(figsize=(10, 6))
        plt.plot(data) #14
        plt.title("Waveform of Test Audio") #14
        plt.xlabel("Sample Index") #14
        plt.ylabel("Amplitude") #14
        #plt.grid(True)
        plt.show()

        # Flip the data to play the track backwards
        reversed_data = np.flip(data) #15

        # Save the reversed data to a new file
        write('Alone-Sistar-Reversed.wav', Fs, reversed_data) #15

        print("Reversed audio saved as 'Alone-Sistar-Reversed.wav'")

        
if __name__ == "__main__":
    image_file_path = "BigDataImage-1.jpg"  
    audio_file_path ='Alone-Sistar.wav'
    media_processor = MMedia_Processing()
    media_processor.ImgProc(image_file_path)
    media_processor.AudProc(audio_file_path)

