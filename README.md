# ODB Tester

1. Make sure Python is correctly installed on your machine by typing `python` or `python3` into a terminal for your choise. If that is not working follow [this](https://code.visualstudio.com/docs/python/python-tutorial) guide.

2. Open the cloned repository in your terminal

3. Enter `pip install -r requirements.txt` to install all required libraries

4. Connect the OBD adapter to the left USE port of the notebook

5. Start the car engine and run the python script with `python obd_tester.py`

6. Exit data collection with CRTL+C

7. The output file is in the same folder the python script is in. Follow [this](https://www.fcc.gov/general/opening-csv-file-excel) guide to open it in Excel. 


8. You can now do the calculations in Excel: For example:

    - Mass m = P / (a*v) 

10. The power in watts is calculated as 919.37 * MAF (mass air flow, air mass absorbed in grams per second) 

11. More details in the Word document placed in this repo