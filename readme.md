# JSON2SVG
This script helps to convert JSON representation of a linechart to SVG format. 
Currently only supports JSON where the x/y values are assigned to keys 't' (time) and 'v' (value) 
as this was originally written to convert Glassnode Studio's charts (but is easily modifiable).

## Guide
1. Clone the project
2. Install Python
    * Python: https://www.python.org/downloads/
    * verify installation `python --version`
3. Install pip
    * pip: https://bootstrap.pypa.io/get-pip.py
    * install: `python get-pip.py`
    * verify installation: `pip -V`    
3. Install the dependencies from the project folder: `pip install -r requirements.txt`
4. Run the script: `python json2svg.py pathToJson`
    * use _-d_ parameter to turn on debugging log level: `python json2svg.py pathToFile -d`
    * use _-h_ parameter to show help
5. ???
6. Success!
