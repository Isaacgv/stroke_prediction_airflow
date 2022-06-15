import great_expectations as ge
import pandas as pd
import json
from great_expectations.core.batch import RuntimeBatchRequest


#context = ge.data_context.DataContext("/opt/great_expectations")
context = ge.data_context.DataContext()

def great_expectation_exec(df):
    batch_request = RuntimeBatchRequest(
        datasource_name="stroke_data",
        data_connector_name="default_runtime_data_connector_name",
        data_asset_name="stroke_data_csv",  # This can be anything that identifies this data_asset for you
        runtime_parameters={"batch_data": df},  # df is your dataframe
        batch_identifiers={"default_identifier_name": "default_identifier"},
    )

    validator = context.get_validator(
        batch_request=batch_request, expectation_suite_name="stroke_data.csv.warning"
    )

    results = context.run_validation_operator("action_list_operator" , assets_to_validate=[validator])
  
    dict_info = json.loads(str(results["run_id"]))
    bach_id = str(list(results["run_results"].keys())[0]).split("/")[-1]
    return {"success": results["success"], 
            "run_name": dict_info["run_name"], 
            "run_time": dict_info["run_time"],
            "batch_id": bach_id}

#input_data_df = pd.read_csv("stroke_ingest.csv")
#data_ingest_df = input_data_df.sample(n=5)
#print(great_expectation_exec(data_ingest_df))