# ON-Bank

...

## Technologies

* Python
* Flask

## Setup

GitHub:
```
$ git clone https://github.com/dazcona/flaskerizer
$ mv flaskerizer my-project && cd my-project && rm -rf .git/
```

Manual:
```
$ mkdir -p my-project && cd my-project
$ touch .env .flaskenv .gitignore README.md requirements.txt
$ mkdir -p src && cd src && mkdir templates static && cd static && mkdir css js
```

## Create a Virtual Environment using Bash

1. Creation of a virtual environments done by executing the command venv
2. Command to activate virtual environment
3. Install dependencies
4. List the libraries installed on your environment
5. Do your work!
6. When you are done, the command to deactivate virtual environment
```
$ python3 -m venv env/
$ source env/bin/activate
(env) $ pip install -r requirements.txt
(env) $ pip freeze
(env) $ ...
(env) $ deactivate
```

## Resources

* https://github.com/dazcona/flaskerizer
* https://github.com/dazcona/flask-login
* https://github.com/dazcona/viz