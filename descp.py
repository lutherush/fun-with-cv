#" = :: =========================================================== :: =
#"  Filename: /home/lutherus/builds/cv/img_description.py
    #"  Filesize: 1.5KB on 26 Lines
#"   Purpose: Image description for blind people
#"    Author: Velimir Baksa 
#"   License: GPL_v2
#"   Created: 26.01.2019 18:20 CET (+0100)
#"  Modified: 18.03.2020 13:01 CET (+0100)
#"   text editor used: VIM - Vi IMproved 7.3 (2010 Aug 15, compiled Dec  2 2010 10:44:11)
#"   Version : pythobn 3.8.2
#" = :: =========================================================== :: =




# USAGE
# python extract_descp.py --image jp_01.png

# import the necessary packages
from __future__ import print_function
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# initialize the keypoint detector and local invariant descriptor
detector = cv2.FeatureDetector_create("DESCP")
extractor = cv2.DescriptorExtractor_create("DESCP")

# load the input image, convert it to grayscale, detect keypoints, and then
# extract local invariant descriptors
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kps = detector.detect(gray)
(kps, descs) = extractor.compute(gray, kps)

# show the shape of the keypoints and local invariant descriptors array
print("[INFO] # of keypoints detected: {}".format(len(kps)))
print("[INFO] feature vector shape: {}".format(descs.shape))
