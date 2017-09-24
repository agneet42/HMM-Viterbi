Contains the following files : 

comp0002.bmp - original file
test.bmp - converted to 8-bit
resized.bmp - resized to 48*48

daisy_descrpt.png shows the output of the keypoints generated in the input file, 'resized.bmp'
The shape of the returned vector by the descriptor generator is (5,5,200). This implies that total keypoints/features identified are 25 (5*5), and we get 25 descriptor vectors of length 200 for each of the keypoint detected. 

The first two dimensions indicate which particular feature vector we want to access, while the third dimension is the actual descriptor vector.

feature.txt contains the features in the form of [[][][][][]] * 5.
