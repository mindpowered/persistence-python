import setuptools

#with open("README.md", "r") as fh:
    #long_description = fh.read()
setuptools.setup(
     name='mindpoweredlogic-persistence',
     version='0.0.9',
     description="persistence",
     #long_description=long_description,
     #long_description_content_type="text/markdown",
     py_modules=['persistence'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )
