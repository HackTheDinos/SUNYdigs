<h3>Text-based Image Segmentation  </h3>
This folder contains the python script to execute segmentation of a scanned page based on text.<br>
This is basically done by using Adaptive Gaussian Thresholding to separate words from background, <br>
noise removal on image, Morphology Transformation to make the word look like a connected component <br>
and lastly, contour detection to filter out bounding rectangles that are about the size of a word.<br>
Here's a [simple example](http://blog.christianperone.com/2014/06/simple-and-effective-coin-segmentation-using-python-and-opencv/) that explains all of the above modules for a coin detection problem.<br><br>
The code is designed to accept the repository in the exact format as the [Dig Up the Past Github repository](https://github.com/amnh/HacktheDinos/tree/master/challenges/Dig-Up-The-Past).<br>
You can `git clone` and run this script right out of the box by changing the path of `rootdir` in script to the <br>
cloned repository. However, be warned that this script would create a folder for each "scanned page" segmented in the<br>
"images" folder of a journal. It would also generate metadata in the form of a JSON object for the particular "scanned page"<br>
Each JSON object in the list describes a "cropped" word image file, which stores author, book year, <br>
path to parent image (scanned page) and path to word image. Please see the demo folder in the repository<br>
to get a visualization of the results.<br><br>
Because the algorithm isn't perfect and is optimized for true positives (cropped image is word) <br>
it might skip a few words on the page that are indeed words. Future hackers can decide to fine-tune <br>
the algorithm or alternatively, after enough words have been transcribed for a particular page, one could<br>
choose to use the metadata to extract Paleontology topics/terms mentioned in a journal.<br>

Please check open git issues for the repository, if you need to contribute.

<h3>Setup</h3>
<h6>Pre-requisites</h6>
Python 2.7, Numpy, Scipy, OpenCV
<h6>Create a virtual environment</h6>
pip install -r requirements.txt

<h3>Run code</h3>
python img_to_txt.py

