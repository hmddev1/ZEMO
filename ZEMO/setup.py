import setuptools


setuptools.setup(
    name='ZEMO',
    version='1.0.0',
    description='Zernike moments: Digital images',
    author='Hossein Safari',    
    author='Hamed Ghaderi',
    author='Nasibe Alipour',
    author_email='safari@znu.ac.ir',
    author_email='albert.ghaderi@gmail.com',
    author_email='nasibealipour@gmail.com',
    packages=['ZEMO'],
    install_requires=[
        'math'
        'numpy'
        'numpy.linalg'
 ],
    url='https://github.com/hmddev1/ZEMO',
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
)
