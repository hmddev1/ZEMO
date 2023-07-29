**Zernike Moments - Astronomical and none-astronomical images**

This code calculates Zernike moments for astronomical images. Zernike moments are unique due to orthogonality and a complete set of Zernike polynomials. Zernike moments are used in image analysis to characterize the shape and structure of objects. The following articles and their references give a detailed description of the Zernike polynomials and Zernike moments.

Raboonik, A., Safari, H., Alipour, N., & Wheatland, M. S. 2017, ApJ, 834, 11

Alipour, N., Mohammadi, F., Safari, H. 2019, ApJS, 243, 20

The code includes the following functions:

zernike_order_list: Generates a list of Zernike polynomial orders.
robust_fact_quot: Calculates the robust factor quotient between two lists of values.
zernike_bf: Generates Zernike basis functions for a given size and order.
zernike_mom: Calculates the Zernike moments of an input image using precomputed Zernike basis functions.
zernike_rec: Reconstructs an image from Zernike moments(Inverse trasformation).

- The zernike_order_list function calculates factorials, p-indices, and q-indices for Zernike polynomials.
- The robust_fact_quot function removes common elements from lists and calculates product quotients.
- The zernike_bf function generates Zernike basis functions stored in a complex-valued grid.
- The zernike_mom function calculates Zernike moments by summing the product of the image and basis functions.
- The zernike_rec function reconstructs an image by summing the weighted Zernike basis functions based on moments.
- The code utilizes additional helper functions, mathematical calculations, and NumPy operations.
- The functions accept parameters such as image data, maximum order, size, and optional arguments.
- The code includes checks for data validity, such as square image size matching, and prints informative error messages.
- The functions return relevant results, such as Zernike moments or reconstructed images.

Authors: Hamed Ghaderi, Nasibe Alipour, Pardise Garavand, Hosein Safari
