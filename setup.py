from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name="roipy",
    version="1.3.1",
    author="Will Decker",
    author_email="deckerwill7@gmail.com",
    description="Plotting brain regions of interest (ROI) for demonstration purposes in Python",
    url="https://github.com/w-decker/roipy",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering"
    ],
    python_requires='>=3.8',
    install_requires=['nilearn', 
                      'matplotlib',
                      'numpy'],
    long_description=description,
    long_description_content_type="text/markdown"

)