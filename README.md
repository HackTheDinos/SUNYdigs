<h1>#SUNYdigs</h1>

<h3>Overview</h3>

<h5><p><img src="/UX/images/digs_logo.jpg" align="left"><img src="/UX/images/team.jpg" align="right">Paleontologists throughout the 20th century used field notebooks to keep detailed logs of their expeditions. Previous work at the museum has given us these notes as scanned images and as very imperfect text transcriptions. The text has never analyzed for potentially relevant pieces of information that could lead to new understanding of past expeditions. "These data are very frequently requested by researchers from around the world, but their imperfect nature make them less useful than they could be."</p>
     <p>  The <i><font color="#ff0000">SUNYdigs team</font></i> decided that the best solution for this project was to gamify this "Dig Up the Past" challenge by creating a platform where users would transcribe without being overwhelmed.</p> 
	 
	</h5> 
	
<h3>Inspiration</h3>
The project was in part inspired by the hugely successful crowdsourcing project - [reCAPTCHA](https://www.cylab.cmu.edu/partners/success-stories/recaptcha.html)<br>
Here's a [link](https://www.youtube.com/watch?v=-Ht4qiDRZE8) to the TED talk about Massive-scale online collaboration by Luis Von Ahn, <br>founder of reCAPTCHA and CEO at Duolingo.

<h3>Design</h3>
As a first step, the system would perform text-based image segmentation on all scanned pages. <br>
For every scanned page in the [journal](https://github.com/amnh/HacktheDinos/tree/master/challenges/Dig-Up-The-Past) a corresponding folder is created with the same title that contains all the words segmented. A text file is also created alongside the original image of the scanned page, with the same title that contains each word's metadata in form of a JSON object.<br><br>
`{"img_page": path/to/parent_image, "year": 1899, "word": [path/to/word_image_file, "!@#$%", number_of_votes], "author": "brown"}`<br><br>
This metadata remains in queue till five upvotes have been gathered for a particular transcription. After this, it is saved to a database and archived.

<h3>Improvements and Observations</h3>
* 'Suggest' feature to aid guessing of difficult Paleontology terms for a layman transcribing documents.<br>
* Higher resolution images would help in getting words out of images with better accuracy.
* The text-based image segmentation is currently optimized for sparsely populated and well-formatted journal pages. 

<h3>Issues</h3>
Git issues have been created for problems needing immediate attention. Feel free to contribute. :)


