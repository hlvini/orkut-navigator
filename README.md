# Orkut Navigator
Script that automatically navigates the Orkut Archives on Wayback Machine in search of a specified word

## Setup
1. Clone the repository
2. Inside, create a virtual environment `python3 -m venv venv` and activate it `source venv/bin/activate`
3. Install requirements.txt using `pip install -r requirements.txt`

## Usage
Invoke the script by calling `python3 main.py` then specifing the `--index` and `--word` arguments, must be done inside the virtual environment (e.g.: `python3 main.py --index l --word carro`)

`*--index*`  
The archive is divided alphabetically, from numbers and special characters (represented by 0), from A to Z. 

`*--word*`  
Searches for the specified whole word through the archives, not case-sensitive
