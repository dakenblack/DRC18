# README
This directory will have some helpful jupyter notebooks. Jupyter is a very common data science tool used by a lot of people. It's web based so there's not much to install. 

## Prereq
* python3
* all python packages from requirements.txt
* virtualenv (optional)
    you can make custom environments to develop in
    there's no need to install all python packages to your system directories (some packages might be dodgy)

## List of Files
* Bayes Histogram Classifier
* Decision Tree Classifier

## Resources
* https://docs.scipy.org/doc/numpy/reference/
* https://matplotlib.org/api/pyplot_api.html
* https://matplotlib.org/users/image_tutorial.html
* https://virtualenv.pypa.io/en/stable/
* https://jupyter.org/
* http://scikit-learn.org/stable/index.html
* Google *No Seriously*
* Some specific articles
    * https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html
    * https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html
    * https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.astype.html

## TODO
* Put images in it's own subdirectory

## PFAQ (Possible Frequently Asked Questions)
Q : Why Jupyter?
A :
    1. It's really cool
    2. github already supports it so you can look at the code and the pretty pictures without having to install anything

Q : What programs do I need
A : everything (including version numbers) is in the requirements.txt, install by
    `cd to/this/directory`
    `pip install -r requirements.txt`
    it's even better inside a virtualenv environment, you won't run the risk of corrupting your system with excessive packages
    
Q : Are these useful?
A : They could be, that's up to you. play with both and see what fits. I will mention that the Bayes Histogram Classifier was used by us last year and it has proved to be an excellent colour classifier, with semi-success in varying light conditions. The decision tree classifier has not been used before but a lecturer has mentioned that it is commonly used for colour classification.