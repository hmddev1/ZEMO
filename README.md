# Zernike Moments - Astronomical and non-astronomical images

This program is prepared based on the code provided by Mr. Christian Wolf, originally written in MATLAB. This code calculates Zernike moments for astronomical and non-astronomical images. Zernike moments are unique due to orthogonality and a complete set of Zernike polynomials. Zernike moments are used in image analysis to characterize the shape and structure of objects. The following articles and their references give a detailed description of the Zernike polynomials and Zernike moments.

[Raboonik, A., Safari, H., Alipour, N., & Wheatland, M. S. 2017, ApJ, 834, 11](https://iopscience.iop.org/article/10.3847/1538-4357/834/1/11/meta)

[Alipour, N., Mohammadi, F., Safari, H. 2019, ApJS, 243, 20](https://iopscience.iop.org/article/10.3847/1538-4365/ab289b/meta)

## Description 

The code includes the following functions:

**zernike_order_list**: Generates a list of Zernike polynomial orders.

**robust_fact_quot**: Calculates the robust factor quotient between two lists of values.

**zernike_bf**: Generates Zernike basis functions for a given size and order.

**zernike_mom**: Calculates the Zernike moments of an input image using precomputed Zernike basis functions.

**zernike_rec**: Reconstructs an image from Zernike moments(Inverse trasformation).

### Notes

- The zernike_order_list function calculates factorials, p-indices, and q-indices for Zernike polynomials.
- The robust_fact_quot function removes common elements from lists and calculates product quotients.
- The zernike_bf function generates Zernike basis functions stored in a complex-valued grid.
- The zernike_mom function calculates Zernike moments by summing the product of the image and basis functions.
- The zernike_rec function reconstructs an image by summing the weighted Zernike basis functions based on moments.
- The code utilizes additional helper functions, mathematical calculations, and NumPy operations.
- The functions accept parameters such as image data, maximum order, size, and optional arguments.
- The code includes checks for data validity, such as square image size matching, and prints informative error messages.
- The functions return relevant results, such as Zernike moments or reconstructed images.

## Installation 

1. Download the ZM repository.
2. In the main ZM directory use the package manager [pip](https://pip.pypa.io/en/stable/) to install ZM package:

```bash
!pip install .
```
3. Now you can use ZM package in any local directory on your computer.

## Usage

1. In any Python editor (interpreter) import the ZM next to the necessary libraries:
```python
import numpy as np
import matplotlib.pyplot as plt
from ZM import zernikim as zm
```

2. Import the image:
```python
img = plt.imread() 
```

3. Generates Zernike basis functions for a given `size`, `order`, and optional `withneg` parameter for a **square images** of size **SZ**.
   If WITHNEG is 1, then the basis functions with negative repetition are included.
```python
ZBFSTR = zm.zernike_bf(SZ,order,withng)
```

4. Calculates Zernike moments of an input image (images) using precomputed Zernike basis functions. **I** is the input image.
```python
Z=zernike_mom(I,ZBFSTR)
```

5. Reconstructs an image from Zernike moments using precomputed Zernike basis functions.
```python
I=zernike_rec(Z,SZ,ZBFSTR)
```

You can see some of the examples of the ZM code Usage.

## Examples

In the following examples, you can see the reconstructed images in different orders of Zernike. By calculating the *reconstruction error*, you can choose the best order for reconstruction.

1. Spiral galaxy image:
![download](https://github.com/hmddev1/ZM/assets/53661111/3d7a6e46-0591-41c2-9b61-d5e56ab03ead)

2. Irregular galaxy image:
![msg26473559-3113](https://github.com/hmddev1/ZM/assets/53661111/b0c33925-6123-49af-a425-f0363fe871ef)

3. Elliptical galaxy image:
![msg26473559-3115](https://github.com/hmddev1/ZM/assets/53661111/233ee62c-3f5a-4ec3-b8c9-cf75f70bcfe9)


## Authors

[Hamed Ghaderi](https://github.com/hmddev1), [Nasibe Alipour](https://scholar.google.com/citations?user=PfzZOI0AAAAJ&hl=en), [Pardis Garavand](https://www.linkedin.com/in/pardis-garavand-25b30527b/), [Hossein Safari](https://scholar.google.com/citations?user=nCc1FV8AAAAJ&hl=en)

## License
[MIT](https://choosealicense.com/licenses/mit/)
