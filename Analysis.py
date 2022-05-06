# Note:
# The image of filter is scaned by printer. Scaning parameter should be adjusted refering to example image. Make the shade of color darker.
# The image file name of filter can not contain Japanese due to specification of cv2 library.
# Specify extension for image file you want to analyze.
# Adjust size of contour according to image to extract the contour for filter by size of it.

# Features:
# Transfer the original image file to Treated directory.
# Make copy image drawn contour to Add_contour directory.
# The black_value is calculated that mean of black dot in the filter is divided by area of the filter, then multipiled by 100. Max of black_value is 100.
# The higher black_value, the darker filter.

print('\nLoading libraries ...\n')
import cv2
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import pandas as pd
import shutil
import glob
plt.gray()

print("python version:\t", sys.version)
print("cv2 version:\t", cv2.__version__)
print("numpy version:\t", np.__version__)
print("matplotlib version\t", matplotlib.__version__)
print("pandas version:\t", pd.__version__)

# Save image file in Untreated directory.
# Specify extension for image file you want to analyze.
extension = 'tif'
len_extension = len(extension) + 1 # increase 1 as priod.
list_file_name = glob.glob(r'Untreated/*.{}'.format(extension))
# Set DataFrame for exporting csv file.
df = pd.DataFrame(index = [os.path.basename(img)[:-len_extension] for img in list_file_name])

print('\n*** Start analyze. ***\n')
for file_name in list_file_name: # file_name => Untreated\~.tif
    basename = os.path.basename(file_name)[:-len_extension]
    # read and preprocess image.
    img = cv2.imread(file_name)
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    threshold = 254 # adjust according to image.
    ret, img_thresh = cv2.threshold(img_gray, threshold, 255, cv2.THRESH_BINARY)
    img_median = cv2.medianBlur(img_thresh,5)

    # extract the contour for filter, qualify blackness, log measured data and transfer original image file.
    try:
        contours, hierarchy = cv2.findContours(img_median, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
        cnts=[]
        for cnt in contours:
            if cv2.contourArea(cnt) >200000: # extract the contour for filter by size of it.
                if cv2.contourArea(cnt) < 300000: # adjust size of contour according to image.
                    cnts.append(cnt)
        cnt_num = len(cnts)
        cnt_area = cv2.contourArea(cnts[0]) # calculate area of filter.
        mask = np.zeros(img.shape[:-1], np.uint8)
        cv2.drawContours(mask, cnts, 0, 255, -1)
        mean = cv2.mean(img, mask=mask) # calculate black dot in filter.
        mean = mean[0]
        black_value = round((255-mean)/255*100,3) # qualify blackness rate for filter.
        
        # write data calculated above.
        df.loc["{}".format(basename), "cnt_num"] = cnt_num
        df.loc["{}".format(basename), "cnt_area"] = cnt_area
        df.loc["{}".format(basename), "black_value"] = black_value
        print(basename,"...detected filter \t black_value:", black_value)
        # display image of filter drawn contour.
        cv2.drawContours(img, cnts, 0,(255,  0,  0),50)
        #cv2.putText(img, '{}'.format(black_value), (0, 50), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 3, cv2.LINE_AA)
        cv2.imwrite("Add_contour\{}_add_{}.jpg".format(basename, black_value), img)
        # shutil.move: Specify the path of the file or directory you want to move in the first argument, 
        # and the path of the destination directory in the second argument.
        # move the original image file to Treated directory.
        new_path = shutil.move(file_name, 'Treated')

    except:
        contours, hierarchy = cv2.findContours(img_thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
        cnts=[]
        for cnt in contours:
            if cv2.contourArea(cnt) >200000:
                if cv2.contourArea(cnt) < 300000:
                    cnts.append(cnt)
        cnt_num = len(cnts)
        cnt_area = cv2.contourArea(cnts[0])

        mask = np.zeros(img.shape[:-1], np.uint8)
        cv2.drawContours(mask, cnts, 0, 255, -1)
        mean = cv2.mean(img, mask=mask)
        mean = mean[0]
        black_value = round((255-mean)/255*100,3)

        df.loc["{}".format(basename), "cnt_num"] = cnt_num
        df.loc["{}".format(basename), "cnt_area"] = cnt_area
        df.loc["{}".format(basename), "black_value"] = black_value
        print(basename,"...detected filter \t black_value:", black_value)
        cv2.drawContours(img, cnts, 0,(255,  0,  0),50)
        #cv2.putText(img, '{}'.format(black_value), (0, 50), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 3, cv2.LINE_AA)
        cv2.imwrite("Add_contour\{}_add_{}.jpg".format(basename, black_value), img)
        new_path = shutil.move(file_name, 'Treated')
print("\n*** Done scaning all image files. ***\n")


# Save data calculated as csv file.
import datetime
dt_now = datetime.datetime.now()
dt_now_str = dt_now.strftime('%Y%m%d_%H%M%S')
df.to_csv("filter_black_value_{}.csv".format(dt_now_str))