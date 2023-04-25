
# Create virtual environment

python3 -m venv dev-env


**Create virtual environment**
`python3 -m venv /path/to/virtual/environment/dev-env`

**Activate virtual environment**

`source dev-env/bin/activate`


**Check the Current Active Virtual Environment**
Current virtual environment

**On Linux or MacOS**
`echo $VIRTUAL_ENV`

**On windows**
`%VIRTUAL_ENV%`


[Source](https://sparkbyexamples.com/python/python-activate-virtual-environment-venv/)


**Working with requirements**

`pip freeze > requirements.txt`

`pip install -r requirements.txt`


**Ex**
`###### Requirements without Version Specifiers ######
nose
nose-cov
beautifulsoup4

###### Requirements with Version Specifiers ######

docopt == 0.6.1             # Version Matching. Must be version 0.6.1
keyring >= 4.1.1            # Minimum version 4.1.1
coverage != 3.5             # Version Exclusion. Anything except version 3.5
Mopidy-Dirble ~= 1.1        # Compatible release. Same as >= 1.1, == 1.* `





**About venv**
[real python](https://realpython.com/python-virtual-environments-a-primer/#avoid-installing-pip)


python3 -m venv venv --upgrade

