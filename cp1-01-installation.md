<img align="right" src="media/insulina_124.jpg">

### mlzoomcamp-2022-12 Capstone Project 1    

# Diabetes Health Indicators <font size=2>[[home]](README.md)</font>

# Installation

Check version needed: 3.9.11
- > python --version  
```
    Python 3.9.11
```

Create a dedicated folder and inside create your "pipenv"
- pipenv should be installed. If not see https://pypi.org/project/pipenv/

- > pipenv --python 3.9.11
```   
     Successfully created virtual environment!   
     Virtualenv location: C:\Users\alain\.virtualenvs\mlzc-cp1-TwdYS11w
```
- > pipenv install notebook numpy pandas scikit-learn xgboost bentoml matplotlib seaborn tqdm ipywidgets

```python
        
        Installing notebook...
        Adding notebook to Pipfile's [packages]...
        Installation Succeeded
        Installing numpy...
        Adding numpy to Pipfile's [packages]...
        Installation Succeeded
        Installing pydantic...
        Adding pydantic to Pipfile's [packages]...
        Installation Succeeded
        Installing pandas...
        Adding pandas to Pipfile's [packages]...
        Installation Succeeded
        Installing sklearn...
        Adding sklearn to Pipfile's [packages]...
        Installation Succeeded
        Installing xgboost...
        Adding xgboost to Pipfile's [packages]...
        Installation Succeeded
        Installing bentoml...
        Adding bentoml to Pipfile's [packages]...
        Installation Succeeded
        Pipfile.lock not found, creating...
        Locking [packages] dependencies...
        Locking...
        Resolving dependencies...
        Success!
        Locking [dev-packages] dependencies...
        Updated Pipfile.lock (1ebbec)!
        Installing dependencies from Pipfile.lock (1ebbec)...
        To activate this project's virtualenv, run pipenv shell.
        Alternatively, run a command inside the virtualenv with pipenv run.
```


To lanch jupyter in the pipenv:
- > pipenv shell
```
    > jupyter notebook
```
or directly:  
- > pipenv run jupyter notebook  

#

To allow tqdm to work (nicely) in jupyter run this once:

- > pipenv run jupyter nbextension enable --py widgetsnbextension