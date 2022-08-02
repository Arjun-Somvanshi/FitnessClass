# FitnessClass

A class which allows users to register a classes on app, cancel it and 
also manages a waiting list.


## Run it

Install python latest version 3.10.5 or use pyenv.

Install pipenv like this: 
```bash
    python -m pip install pipenv
```
Get all dependencies easily:
```bash
  pipenv install
```
Run it:
```bash
    pipenv shell
    cd src/
    python main.py
```

## Database
I didn't have mongoDB installed so I used json files, but I would have used the same 
kind of schema there. To see how the data is changing after performing an action
look at the `database.json` file to see if the functionality works. 
