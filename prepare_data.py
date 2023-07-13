# Purpose: This file is used to prepare the data for the model. 
import os
from dataclasses import dataclass
import pandas as pd
import numpy as np

@dataclass
class PrepareData:
    file_location : str = None
    data : pd.DataFrame = None

    def get_season(self, date):
        """
        Spring:  Begins on March 20 and ends on June 21
        Summer:  Begins on June 21 and ends on September 23
        Fall and Winter:  Begins on September 23 and ends on March 19, 2024
        """
        month = date.month
        day = date.day
        if (month == 3 and day >= 20) or (month == 4) or (month == 5) or (month == 6 and day <= 21):
            return "Spring"
        elif (month == 6 and day >= 21) or (month == 7) or (month == 8) or (month == 9 and day <= 23):
            return "Summer"
        else:
            return "Fall_Winter"

    def export_data_by_season(self):
        """ Export the data by 3 seasons from get_season function."""
        # 1. take the date column and convert to python date
        # 2. group by season
        # 3. export the data by season
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data['Season'] = self.data['Date'].apply(self.get_season)
        self.data = self.data.groupby('Season')
        for season, data in self.data:
            # check if file exists if yes delete it and create new one
            file_name = f"{season}.csv"
            try:
                os.remove(file_name)
            except:
                pass
            data.to_csv(file_name, index=False)
            print(f"File {file_name} created successfully.")
        
    def __init__(self, file_location):
        self.file_location = file_location
        self.data = None
        print("Data preparation started.")
    
    def read_data(self):
        self.data = pd.read_csv(self.file_location)
        print("Data read successfully.")
def main():
    """ Ask file location from user and read the data."""
    """ Export the data by season."""
    # /Users/kabipokhrel/Downloads/ad_viz_plotval_data (3).csv
    file_location = input("Enter the file location: ")
    data = PrepareData(file_location)
    data.read_data()
    data.export_data_by_season()

if __name__ == "__main__":
    main()