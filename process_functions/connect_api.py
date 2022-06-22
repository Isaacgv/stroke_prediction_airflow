
import pandas as pd
import json

import requests

BACKEND_SERVER = "http://35.238.16.200:8005/"


def get_prediction_document(filename: str, data: pd.DataFrame) -> pd.DataFrame:
    """_summary_
    Takes File Input from User Interface returns a Prediction Dataframe
    Args:
        data (pd.DataFrame): _description_
    """
    data = data_frame_fix_column_with_Nan_float(data)
    list_of_json = data.to_dict(orient='records')
    data_json = dict()
    data_json["record"] = {"id": 0, "file_name": filename}
    data_json["patient"] = list_of_json
    url = BACKEND_SERVER + "predict_multiple"
    print(url)
    response = requests.get(url, json=data_json)

    if response.status_code == 200:
        result = json.loads(response.content)
        prediction_df = pd.read_json(result, orient='index')
        data["prediction"] = prediction_df["prediction"]
        return data, True
    elif response.status_code == 422:
        return "File is Not withint the Correct Format !", False
    else:
        return pd.DataFrame([]), True


def data_frame_fix_column_with_Nan_float(data):
    """_summary_
    Fix Nan_float issues in dataframe , Pydantic model doesn't like
    Nan's in Float columns Json Encoder doesnt like to deal
    with Nan's in Float columns
    Args:
        data (_type_): _description_

    Returns:
        _type_: _description_
    """
    float_cols = data.select_dtypes(include=['float64', 'int64']).columns
    str_cols = data.select_dtypes(include=['object']).columns
    data.loc[:, float_cols] = data.loc[:, float_cols].fillna(0.0)
    data.loc[:, str_cols] = data.loc[:, str_cols].fillna('')
    return data
