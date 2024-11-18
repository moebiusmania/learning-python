# learning-python 🐍

> Just some takes on learning Python, simple stuff, nothing too fancy.

[Claude 3.5 Sonnet](https://www.anthropic.com/claude) and [Cursor](https://www.cursor.com/) helped me a lot with this.

## Why?

I already had to get my hands dirty with Python in the last months, so I think it's time to start learning it properly. At least the basics.

Also I would like to start playing a bit with LLMs and related stuff on my local machine, and that's mostly Python ground.

## Setting up the global environment

- install `pyenv` with `brew`
- install latest `python` with `pyenv`
- set latest `python` as global default with `pyenv global <version>`
  - in case it doesn't work, adding `eval "$(pyenv init -)"` to `.zshrc` has helped
- checked its working with `$ python --version`

## Setting up the local environment
- set a `python` version as local default with `$ pyenv local <version>`
- `$ python -m venv .venv` create local virtual env
- `$ source .venv/bin/activate` activate the virtual env
  - `$ deactivate` to leave the virtual env
- checked its working with `$ python --version`

## Managing dependencies

- install existing dependencies with `$ pip install -r requirements.txt`
- update dependencies with `$ pip freeze > requirements.txt`

## How to run the projects

install dependencies

```bash
$ pip install -r requirements.txt
```

run the script

```bash
$ python <script>.py
```

## Some useful libraries

- pytest - testing
- ruff - format + linter
- ipython - interactive shell
- ipdb - debugger
- litestar - web framework api

## License

Released under the MIT License. See the [LICENSE](LICENSE) file for details.
