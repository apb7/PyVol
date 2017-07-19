# PyVol
A Python3 script to change the master volume from the command line.

### The script has the following arguments:  
* --volume _value_%  
    This argument sets the master volume to _value_% where _value_ is an integer between 0 to 100.  
    ```shell 
      python3 PyVol.py --volume 25%  
    ```
 * --present  
    This argument prints the present volume percentage.  
    ```shell  
      python3 PyVol.py --present  
    ```  
 * --mute  
    This argument mutes the master volume.  
    ```shell  
      python3 PyVol.py --mute  
    ```
 * --max  
    This argument sets the master volume to 100%.  
    ```shell
      python3 PyVol.py --max  
    ```

## Furthur Improvements:  
More arguments can be added to the script!  
Suggestions and improvements are welcome!
