# USAGE
# python search.py --index index.csv --query queries/103100.png --result-path dataset

# import the necessary packages
from pyimagesearch.colordescriptor import ColorDescriptor
from pyimagesearch.searcher import Searcher
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-n", "--Number-of-images", required = True,
	help = "Number of images to fetch")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())

# initialize the image descriptor
cd = ColorDescriptor((8, 12, 3))

# load the query image and describe it
query = cv2.imread(args["query"])
print "Shape of the Image:",query.shape
if query.shape==(512,512,3):
	features = cd.describe(query)
	n = args["Number_of_images"]
	print "Number of images to be fetched:",n
	# perform the search
	searcher = Searcher(args["index"])
	print'Please wait for the results.'
	results = searcher.search(features,n)

	# display the query
	cv2.imshow("Query", query)

	# loop over the results
	for (score, resultID) in results:
		# load the result image and display it
		result = cv2.imread(args["result_path"] + "/" + resultID)
		cv2.imshow("Result", result)
		#cv2.imwrite(result)
		cv2.waitKey(0)
else:
	print('Please Give an image size of 512x512')