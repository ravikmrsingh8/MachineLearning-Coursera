### Setting up Python and turicreate on linux
1)sudo apt-get update <br />
2)sudo apt-get upgrade <br />
3)python /usr/lib/python2.7/dist-packages/easy_install.py pip <br />
#### if error at 3 try below
4)sudo apt-get install python-setuptools <br />
5)sudo apt-get install python-pip <br />


#### setup for turicreate
1)sudo pip install virtualenv <br />
2)virtualenv venv <br />
3)cd venv <br />
4)source bin/activate    # to deactiavte type deactivate <br />
5)pip install --upgrade pip <br />
6)pip install turicreate <br />
