# Copy .pyi files into your virtual environment from the https://github.com/scottkmaxwell/MoneyDancePython package.
# To start, create a virtual environment in this folder with the name `env`. You should be able to use your current
# Python 3 interpreter, even though all of the code will be Python 2.7 (Jython). We won't ever run this code with this
# virtual environment. We will just tell PyCharm or VSCode that we are using it so that it can do proper static
# analysis.
#
# Next, clone https://github.com/scottkmaxwell/MoneyDancePython to the same root folder as this package, something like
# ~/Source.
#
# Now when you run this script, it will copy the .pyi files from MoneyDancePython into your virtual environment.
# If you used a Python version other than python3.10, adjust the SITE_PACKAGES line below.

SITE_PACKAGES=env/lib/python3.10/site-packages
rm -rf $SITE_PACKAGES/com $SITE_PACKAGES/java $SITE_PACKAGES/javax $SITE_PACKAGES/org $SITE_PACKAGES/moneydance.pyi
cp -r ../MoneyDancePython/site-packages/* $SITE_PACKAGES
