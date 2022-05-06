# black_contamination

## Background
* I was facing with a **contamination** of certain product.
* Therefore, filter the solution of the product and look at the filter to check the blackness.
* Though the above procedure was conducted, it was very **qualitative**,  not quantified blackness of the product and amount of contamination.
* So, I came up with **quantifying** a contamination of the product by counting number of black dots in image of filter using programming language, python.

## Feature
* You can quantify blackness in image of filter.
* You can see a contour of filter which computer recognized.
* You can get csv file written several data such as number of black dots, area of filter and **black_value**.
* **black_value** is rate of black dots and area of filter.


![add_contour](https://user-images.githubusercontent.com/57758623/167147890-fa82607b-eb78-48d6-bd68-f001ea8b625c.jpg)
![csv_table](https://user-images.githubusercontent.com/57758623/167148519-d96c03ff-bc34-422c-8378-6ecc992ee307.jpg)

## Python version
* python 3.7.11

## Requirement
* cv2 version 4.2.0
* numpy version 1.20.3
* matplotliib version 3.4.2
* pandas version 1.3.4

## How to use
1. Scan the filter using a printer or a machine which has scanning reproducibility.
2. Put the image file to "Untreated" directory.
3. In script, adjust size of contour according to image to extract the contour for filter by size of it.
4. Run script.
5. The original image file is moved to "Treated" directory, the image file drawn contour is transferred to "Add_contour" directory respectively.
6. Get csv file described several data.

## Note
* Scanning parameters for a printer should be adjusted refering to example image, "sample.tif". Make the shade of color darker. Any extension of image is acceptable, but fix script like so.
* The image file name of filter can not contain Japanese due to specification of cv2 library.

## Information
* Author : Ryuhei Shiomoto
* Created Date : 2022/05/07

## License
* 
