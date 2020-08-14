# Image_Similarity_Python-Open_CV

### Problem Statement : 
You are provided with a dataset of ~5k 512x512 images, your program should accept an 512x512 input image and return N images from the provided dataset similar to the input image.

### The architecture  :
There are four steps followed in the architecture:

1. Defining our Image Descriptor:
  colordescriptor.py-We grab the dimensions of the image and Compute the center of the image (x,y).
  we are going to divide our image into five different regions: 
  (1) the top-left corner, 
  (2) the top-right corner, 
  (3) the bottom-right corner, 
  (4) the bottom-left corner, and finally 
  (5) the center of the image.
  
   The most efficient way of representing each of these segments is to use a mask. Only (x, y)-coordinates in the image that has a corresponding (x, y) location in
   the mask with a white (255) pixel value will be included in the histogram calculation. If the pixel value for an (x, y)-coordinate in the mask has a value of
   black (0), it will be ignored.
2. Extracting Features from Our Dataset:
  In this index.py, we extarcy the features of the image and storing them in index.csv.
3. Searcher:
  Created a class where searching similarity metrics between the images and give the limit for the images.
  Images that have a chi-squared similarity of 0 will be deemed to be identical to each other. As the chi-squared similarity value increases, the images are
  considered to be less similar to each other.
  It requires two arguments,Which are two histograms that we compare for similarity.
4. Performing a Search:
  We call search.py for the query to get into and get the results.
  We Connect each other to build a full-fledged Content-Based-Image-Retreival System. 

  
### Follow the below steps and to run locally.

### The steps required to run it on local system :

<mark>Follow the steps</mark>
  <p>Then open your terminal and create new folder<br>
  
  ```mkdir (Name of the folder)```<br>
  
  after making the directory get into the directory by using the following command<br>
  
  ```cd (Name of the folder)```
  </p>
  

<p>
  <mark>First create a virtual environment where it doesn't merge with the existing environment</mark>
<p>
  
  ```virtualenv --python=python3 app```

</p><br>

<p>Enter into the the Virtual Environment and then</p><br>

<mark>Clone the github repository into the system</mark><br>
  <p>
    
   ```git clone https://github.com/Speedster-95/Aelouss.git```<br>
   
   and download the dataset from the link https://drive.google.com/drive/folders/1VMAFykUwnxyvCyNqgKDRkG05IAtMayPi?usp=sharing
    
</p><br>

<mark>Use the following command to go into the directory </mark>
<p>
  
  ```cd (Name of the folder)```
  
 </p><br>
 
<mark> First install all the prerequisite by the following command</mark>
<p>
  
  ```pip install -r requirements.txt```

</p><br>

<mark> Once everything is done. Now we can run it on the local by using this command</mark>
<p>Give the place where datasetis avaiable and where you wanna place the index.csv and run the below code</p>
<p>
  
  ```python index.py --dataset dataset --index index.csv```
  
</p><br> 
<p>Give the path for the csv file and the path of the dataset.</p>
<p>
  
  ``` python search.py --index index.csv --query queries/111.png --result-path dataset```
  
</p><br>  

<mark>Result</mark>
<p>In this result u can see the query and results window.</p>
