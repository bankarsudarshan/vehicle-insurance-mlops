import sys
from typing import Optional

import pandas as pd
import numpy as np

from src.configuration.mongodb_connection import MongoDBClient
from src.exception import MyException

class MongoData:
    """
    A class to export MongoDB records as a pandas DataFrame.
    """

    def __init__(self, database_name: str) -> None:
        """
        Initializes the MongoDB client connection.
        Prameters:
        database_name : str
            the name of the database to get data from 
        """
        try:
            self.mongo_client = MongoDBClient(database_name=database_name)
        except Exception as e:
            raise MyException(e, sys)

    def export_collection_as_dataframe(self, collection_name: str) -> pd.DataFrame:
        """
        Exports an entire MongoDB collection as a pandas DataFrame.

        Parameters:
        collection_name : str
            The name of the MongoDB collection to export.

        Returns:
        pd.DataFrame
            DataFrame containing the collection data, with '_id' column removed and 'na' values replaced with NaN.
        """
        try:
            # Access specified collection from the database
            collection = self.mongo_client.database[collection_name]

            df = pd.DataFrame(list(collection.find()))

            if "id" in df.columns.to_list():
                df = df.drop(["id"], axis='columns')
            df.replace({"na":np.nan},inplace=True)
            return df

        except Exception as e:
            raise MyException(e, sys)