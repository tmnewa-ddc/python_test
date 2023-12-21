# python test example

python test example

* unittest
* mock
* api test

_python_version = "3.8"_

## install

using [Pyenv](https://github.com/pyenv/pyenv) manages python versions

`brew install pyenv`

```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
```

reload zsh

`exec "$SHELL"`

install python 3.8 

`pyenv install 3.8.3`


using [Pipenv](https://github.com/pypa/pipenv) manages a virtualenv  and package

`brew install pipenv`

then install package and virtualenv

`pipenv install`

spawns a shell within the virtualenv

`pipenv shell`

check python env

`python --version`

*Python 3.8.3*

`which python`

*/Users/\<userName\>/.local/share/virtualenvs/testing-bQVNgF24/bin/python*

exit virtualenv

`exit` or ctrl + D


## run test

`pipenv shell`

`pytest`

## coverage

`coverage run -m pytest`

`coverage html`

`open htmlcov/index.html`

`pytest  --cov=./ --cov-report=html`
