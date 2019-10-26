Nielsen Graph

This application will dynamically search the working directory for an excel or csv.
After finding the file name the application will parse the workbook using pandas.

The application will generate a screen and display the data graphed in the bar chart format.
Dataframe column 0  will always be the x axis items.
Any Dataframe column after will be set to values to be graphed.

The display will also include labels and legends for the graph items.

################################################################################
To install:
Requirements - have Python installed.
1. Clone from repository and save to local machine.
2. Locate the folder and input the excel/csv.
3. In command prompt or terminal and cd/chdir to graph folder.
4. Run the command "pip install -r requirements.txt"
    -This will install all dependencies, wait until it has completed.
5. run the following command "python NielsenGraph.py"

After executing step 5, a display will pop up with the graph information.

################################################################################
