# black_contamination

## Background
* I was facing with a **contamination** of certain product.
* To check the blackness to let a solution of the product filter, then look at the filter.
* Though the above procedure was conducted, it was very **qualitative**,  not quantified blackness of the product and amount of contamination.
* So, I came up with **quantifying** a contamination of the product by counting number of black dots in image of filter using programming language, python.

## Feature
* You can quantify blackness in image of filter.
* You can see a contour of filter which computer recognized.
* You can get csv file written several data such as number of black dots, area of filter and **black_value**.
* **black_value** is rate of black dots and area of filter.

## Python version
* python 3.7.11

## Requirement
* cv2 version 4.2.0
* numpy version 1.20.3
* matplotliib version 3.4.2
* pandas version 1.3.4

## How to use
1. The image of filter is scaned by printer. Scaning parameter should be adjusted refering to example image, "sample.tif". Make the shade of color darker. Any extension of image is acceptable, but fix script like so.
2. Put the image file to "Untreated" directory.
3. In script, adjust size of contour according to image to extract the contour for filter by size of it.
4. Run script.
5. The original image file is moved to "Treated" directory, the image file drawn contour is transferred to "Add_contour" directory respectively.
6. Get csv file described several data.

## Note
* The image file name of filter can not contain Japanese due to specification of cv2 library.

## Information
* Author : Ryuhei Shiomoto
* Created Date : 2022/05/06

## License
* 