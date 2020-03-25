# navtrac-testing-tools
Testing tools for Navtrac apps

## Installation
- Make sure you are running python3 v3.x.x
- Use package [pip3] to install requirements
```bash
./install.sh
```
- Make sure you activate the virtual environment
```bash
source .venv/bin/activate
```
- To exit virtual environment, type
```bash
deactivate
```

## Run
- Run while in virtual environment
```bash
python3 main.py
```

## Adding modules
1. Make sure to add testing modules in [modules] folder

- File name naming convention is file_name.py
- Classname naming convention is FileName

2. Add **file_name** to **procedures.py** in **_module_list** method in the proper order of running producedures
