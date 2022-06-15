{
  "validation_operator_config": {
    "class_name": "ActionListValidationOperator",
    "module_name": "great_expectations.validation_operators",
    "name": "action_list_operator",
    "kwargs": {
      "action_list": [
        {
          "name": "store_validation_result",
          "action": {
            "class_name": "StoreValidationResultAction"
          }
        },
        {
          "name": "store_evaluation_params",
          "action": {
            "class_name": "StoreEvaluationParametersAction"
          }
        },
        {
          "name": "update_data_docs",
          "action": {
            "class_name": "UpdateDataDocsAction"
          }
        }
      ],
      "result_format": {
        "result_format": "SUMMARY",
        "partial_unexpected_count": 20
      }
    }
  },
  "evaluation_parameters": null,
  "run_id": {
    "run_name": "20220615T100608.971549Z",
    "run_time": "2022-06-15T10:06:08.971549+00:00"
  },
  "run_results": {
    "ValidationResultIdentifier::stroke_data/csv/warning/20220615T100608.971549Z/20220615T100608.971549Z/cc97c050f8d02734791081205ad9b054": {
      "validation_result": {
        "evaluation_parameters": {},
        "meta": {
          "great_expectations_version": "0.15.8",
          "expectation_suite_name": "stroke_data.csv.warning",
          "run_id": {
            "run_name": "20220615T100608.971549Z",
            "run_time": "2022-06-15T10:06:08.971549+00:00"
          },
          "batch_spec": {
            "data_asset_name": "stroke_data_csv",
            "batch_data": "PandasDataFrame"
          },
          "batch_markers": {
            "ge_load_time": "20220615T100608.898069Z",
            "pandas_data_fingerprint": "fc6468e64d21de2a301c59f7ab882c80"
          },
          "active_batch_definition": {
            "datasource_name": "stroke_data",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "stroke_data_csv",
            "batch_identifiers": {
              "default_identifier_name": "default_identifier"
            }
          },
          "validation_time": "20220615T100608.978055Z"
        },
        "statistics": {
          "evaluated_expectations": 65,
          "successful_expectations": 50,
          "unsuccessful_expectations": 15,
          "success_percent": 76.92307692307693
        },
        "results": [
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_table_columns_to_match_ordered_list",
              "kwargs": {
                "column_list": [
                  "id",
                  "firstname",
                  "lastname",
                  "gender",
                  "age",
                  "hypertension",
                  "heart_disease",
                  "ever_married",
                  "work_type",
                  "Residence_type",
                  "avg_glucose_level",
                  "bmi",
                  "smoking_status"
                ],
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": [
                "id",
                "firstname",
                "lastname",
                "gender",
                "age",
                "hypertension",
                "heart_disease",
                "ever_married",
                "work_type",
                "Residence_type",
                "avg_glucose_level",
                "bmi",
                "smoking_status"
              ]
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_table_row_count_to_be_between",
              "kwargs": {
                "max_value": 1687,
                "min_value": 5,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 5
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_be_in_set",
              "kwargs": {
                "column": "gender",
                "value_set": [
                  "Female",
                  "Male"
                ],
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "element_count": 5,
              "unexpected_count": 0,
              "unexpected_percent": 0.0,
              "partial_unexpected_list": [],
              "missing_count": 0,
              "missing_percent": 0.0,
              "unexpected_percent_total": 0.0,
              "unexpected_percent_nonmissing": 0.0,
              "partial_unexpected_index_list": null,
              "partial_unexpected_counts": []
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_not_be_null",
              "kwargs": {
                "column": "gender",
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "element_count": 5,
              "unexpected_count": 0,
              "unexpected_percent": 0.0,
              "partial_unexpected_list": [],
              "partial_unexpected_index_list": null,
              "partial_unexpected_counts": []
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_proportion_of_unique_values_to_be_between",
              "kwargs": {
                "column": "gender",
                "max_value": 0.2,
                "min_value": 0.0011855364552459987,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 0.4
            },
            "success": false
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_be_in_type_list",
              "kwargs": {
                "column": "gender",
                "type_list": [
                  "CHAR",
                  "NCHAR",
                  "VARCHAR",
                  "NVARCHAR",
                  "TEXT",
                  "NTEXT",
                  "STRING",
                  "StringType",
                  "string",
                  "str",
                  "object",
                  "dtype('O')"
                ],
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "element_count": 5,
              "unexpected_count": 0,
              "unexpected_percent": 0.0,
              "partial_unexpected_list": [],
              "missing_count": 0,
              "missing_percent": 0.0,
              "unexpected_percent_total": 0.0,
              "unexpected_percent_nonmissing": 0.0,
              "partial_unexpected_index_list": null,
              "partial_unexpected_counts": []
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_min_to_be_between",
              "kwargs": {
                "column": "age",
                "max_value": 82,
                "min_value": 0,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 40.0
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_max_to_be_between",
              "kwargs": {
                "column": "age",
                "max_value": 82,
                "min_value": 0,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 82.0
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_mean_to_be_between",
              "kwargs": {
                "column": "age",
                "max_value": 68,
                "min_value": 27,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 56.4
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_median_to_be_between",
              "kwargs": {
                "column": "age",
                "max_value": 55.0,
                "min_value": 40.0,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 46.0
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_quantile_values_to_be_between",
              "kwargs": {
                "allow_relative_error": "lower",
                "column": "age",
                "quantile_ranges": {
                  "quantiles": [
                    0.05,
                    0.25,
                    0.5,
                    0.75,
                    0.95
                  ],
                  "value_ranges": [
                    [
                      3.0,
                      12.0
                    ],
                    [
                      20.0,
                      30.0
                    ],
                    [
                      38.0,
                      44.0
                    ],
                    [
                      40.0,
                      61.0
                    ],
                    [
                      68.0,
                      78.0
                    ]
                  ]
                },
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": {
                "quantiles": [
                  0.05,
                  0.25,
                  0.5,
                  0.75,
                  0.95
                ],
                "values": [
                  40.0,
                  44.0,
                  46.0,
                  70.0,
                  70.0
                ]
              },
              "details": {
                "success_details": [
                  false,
                  false,
                  false,
                  false,
                  true
                ]
              }
            },
            "success": false
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_be_in_set",
              "kwargs": {
                "column": "age",
                "value_set": [
                  0.24,
                  0.32,
                  0.4,
                  0.56,
                  0.64,
                  0.8,
                  0.88,
                  1.0,
                  1.08,
                  1.16,
                  1.24,
                  1.32,
                  1.48,
                  1.64,
                  1.72,
                  1.8,
                  1.88,
                  2.0,
                  3.0,
                  4.0,
                  5.0,
                  6.0,
                  7.0,
                  8.0,
                  9.0,
                  10.0,
                  11.0,
                  12.0,
                  13.0,
                  14.0,
                  15.0,
                  16.0,
                  17.0,
                  18.0,
                  19.0,
                  20.0,
                  21.0,
                  22.0,
                  23.0,
                  24.0,
                  25.0,
                  26.0,
                  27.0,
                  28.0,
                  29.0,
                  30.0,
                  31.0,
                  32.0,
                  33.0,
                  34.0,
                  35.0,
                  36.0,
                  37.0,
                  38.0,
                  39.0,
                  40.0,
                  41.0,
                  42.0,
                  43.0,
                  44.0,
                  45.0,
                  46.0,
                  47.0,
                  48.0,
                  49.0,
                  50.0,
                  51.0,
                  52.0,
                  53.0,
                  54.0,
                  55.0,
                  56.0,
                  57.0,
                  58.0,
                  59.0,
                  60.0,
                  61.0,
                  62.0,
                  63.0,
                  64.0,
                  65.0,
                  66.0,
                  67.0,
                  68.0,
                  69.0,
                  70.0,
                  71.0,
                  72.0,
                  73.0,
                  74.0,
                  75.0,
                  76.0,
                  77.0,
                  78.0,
                  79.0,
                  80.0,
                  81.0,
                  82.0
                ],
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "element_count": 5,
              "unexpected_count": 0,
              "unexpected_percent": 0.0,
              "partial_unexpected_list": [],
              "missing_count": 0,
              "missing_percent": 0.0,
              "unexpected_percent_total": 0.0,
              "unexpected_percent_nonmissing": 0.0,
              "partial_unexpected_index_list": null,
              "partial_unexpected_counts": []
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_not_be_null",
              "kwargs": {
                "column": "age",
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "element_count": 5,
              "unexpected_count": 0,
              "unexpected_percent": 0.0,
              "partial_unexpected_list": [],
              "partial_unexpected_index_list": null,
              "partial_unexpected_counts": []
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_proportion_of_unique_values_to_be_between",
              "kwargs": {
                "column": "age",
                "max_value": 1,
                "min_value": 0.058091286307053944,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 1.0
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_be_in_type_list",
              "kwargs": {
                "column": "age",
                "type_list": [
                  "FLOAT",
                  "FLOAT4",
                  "FLOAT8",
                  "FLOAT64",
                  "DOUBLE",
                  "DOUBLE_PRECISION",
                  "NUMERIC",
                  "FloatType",
                  "DoubleType",
                  "float",
                  "float_",
                  "float16",
                  "float32",
                  "float64",
                  "number",
                  "DECIMAL",
                  "REAL"
                ],
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": "float64"
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_min_to_be_between",
              "kwargs": {
                "column": "hypertension",
                "max_value": 0,
                "min_value": 0,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 0
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_max_to_be_between",
              "kwargs": {
                "column": "hypertension",
                "max_value": 1,
                "min_value": 1,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 1
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_mean_to_be_between",
              "kwargs": {
                "column": "hypertension",
                "max_value": 0.1049199762892709,
                "min_value": 0,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 0.2
            },
            "success": false
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_median_to_be_between",
              "kwargs": {
                "column": "hypertension",
                "max_value": 0.0,
                "min_value": 0.0,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 0.0
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_quantile_values_to_be_between",
              "kwargs": {
                "allow_relative_error": "lower",
                "column": "hypertension",
                "quantile_ranges": {
                  "quantiles": [
                    0.05,
                    0.25,
                    0.5,
                    0.75,
                    0.95
                  ],
                  "value_ranges": [
                    [
                      0,
                      0
                    ],
                    [
                      0,
                      0
                    ],
                    [
                      0,
                      0
                    ],
                    [
                      0,
                      0
                    ],
                    [
                      0,
                      1
                    ]
                  ]
                },
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": {
                "quantiles": [
                  0.05,
                  0.25,
                  0.5,
                  0.75,
                  0.95
                ],
                "values": [
                  0,
                  0,
                  0,
                  0,
                  0
                ]
              },
              "details": {
                "success_details": [
                  true,
                  true,
                  true,
                  true,
                  true
                ]
              }
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_be_in_set",
              "kwargs": {
                "column": "hypertension",
                "value_set": [
                  0,
                  1
                ],
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "element_count": 5,
              "unexpected_count": 0,
              "unexpected_percent": 0.0,
              "partial_unexpected_list": [],
              "missing_count": 0,
              "missing_percent": 0.0,
              "unexpected_percent_total": 0.0,
              "unexpected_percent_nonmissing": 0.0,
              "partial_unexpected_index_list": null,
              "partial_unexpected_counts": []
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_not_be_null",
              "kwargs": {
                "column": "hypertension",
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "element_count": 5,
              "unexpected_count": 0,
              "unexpected_percent": 0.0,
              "partial_unexpected_list": [],
              "partial_unexpected_index_list": null,
              "partial_unexpected_counts": []
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_proportion_of_unique_values_to_be_between",
              "kwargs": {
                "column": "hypertension",
                "max_value": 0.2,
                "min_value": 0.0011855364552459987,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 0.4
            },
            "success": false
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_be_in_type_list",
              "kwargs": {
                "column": "hypertension",
                "type_list": [
                  "INTEGER",
                  "integer",
                  "int",
                  "int_",
                  "int8",
                  "int16",
                  "int32",
                  "int64",
                  "uint8",
                  "uint16",
                  "uint32",
                  "uint64",
                  "Int8Dtype",
                  "Int16Dtype",
                  "Int32Dtype",
                  "Int64Dtype",
                  "UInt8Dtype",
                  "UInt16Dtype",
                  "UInt32Dtype",
                  "UInt64Dtype",
                  "INT",
                  "INTEGER",
                  "INT64",
                  "TINYINT",
                  "BYTEINT",
                  "SMALLINT",
                  "BIGINT",
                  "IntegerType",
                  "LongType"
                ],
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": "int64"
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_min_to_be_between",
              "kwargs": {
                "column": "heart_disease",
                "max_value": 1,
                "min_value": 0,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 0
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_max_to_be_between",
              "kwargs": {
                "column": "heart_disease",
                "max_value": 1,
                "min_value": 0,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 0
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_mean_to_be_between",
              "kwargs": {
                "column": "heart_disease",
                "max_value": 0.05572021339656195,
                "min_value": 0,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 0.0
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_median_to_be_between",
              "kwargs": {
                "column": "heart_disease",
                "max_value": 0.0,
                "min_value": 0.0,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 0.0
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_quantile_values_to_be_between",
              "kwargs": {
                "allow_relative_error": "lower",
                "column": "heart_disease",
                "quantile_ranges": {
                  "quantiles": [
                    0.05,
                    0.25,
                    0.5,
                    0.75,
                    0.95
                  ],
                  "value_ranges": [
                    [
                      0,
                      0
                    ],
                    [
                      0,
                      0
                    ],
                    [
                      0,
                      0
                    ],
                    [
                      0,
                      0
                    ],
                    [
                      0,
                      1
                    ]
                  ]
                },
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": {
                "quantiles": [
                  0.05,
                  0.25,
                  0.5,
                  0.75,
                  0.95
                ],
                "values": [
                  0,
                  0,
                  0,
                  0,
                  0
                ]
              },
              "details": {
                "success_details": [
                  true,
                  true,
                  true,
                  true,
                  true
                ]
              }
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_be_in_set",
              "kwargs": {
                "column": "heart_disease",
                "value_set": [
                  0,
                  1
                ],
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "element_count": 5,
              "unexpected_count": 0,
              "unexpected_percent": 0.0,
              "partial_unexpected_list": [],
              "missing_count": 0,
              "missing_percent": 0.0,
              "unexpected_percent_total": 0.0,
              "unexpected_percent_nonmissing": 0.0,
              "partial_unexpected_index_list": null,
              "partial_unexpected_counts": []
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_not_be_null",
              "kwargs": {
                "column": "heart_disease",
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "element_count": 5,
              "unexpected_count": 0,
              "unexpected_percent": 0.0,
              "partial_unexpected_list": [],
              "partial_unexpected_index_list": null,
              "partial_unexpected_counts": []
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_proportion_of_unique_values_to_be_between",
              "kwargs": {
                "column": "heart_disease",
                "max_value": 0.1,
                "min_value": 0.0011855364552459987,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 0.2
            },
            "success": false
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_be_in_type_list",
              "kwargs": {
                "column": "heart_disease",
                "type_list": [
                  "INTEGER",
                  "integer",
                  "int",
                  "int_",
                  "int8",
                  "int16",
                  "int32",
                  "int64",
                  "uint8",
                  "uint16",
                  "uint32",
                  "uint64",
                  "Int8Dtype",
                  "Int16Dtype",
                  "Int32Dtype",
                  "Int64Dtype",
                  "UInt8Dtype",
                  "UInt16Dtype",
                  "UInt32Dtype",
                  "UInt64Dtype",
                  "INT",
                  "INTEGER",
                  "INT64",
                  "TINYINT",
                  "BYTEINT",
                  "SMALLINT",
                  "BIGINT",
                  "IntegerType",
                  "LongType"
                ],
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": "int64"
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_be_in_set",
              "kwargs": {
                "column": "ever_married",
                "value_set": [
                  "No",
                  "Yes"
                ],
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "element_count": 5,
              "unexpected_count": 0,
              "unexpected_percent": 0.0,
              "partial_unexpected_list": [],
              "missing_count": 0,
              "missing_percent": 0.0,
              "unexpected_percent_total": 0.0,
              "unexpected_percent_nonmissing": 0.0,
              "partial_unexpected_index_list": null,
              "partial_unexpected_counts": []
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_not_be_null",
              "kwargs": {
                "column": "ever_married",
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "element_count": 5,
              "unexpected_count": 0,
              "unexpected_percent": 0.0,
              "partial_unexpected_list": [],
              "partial_unexpected_index_list": null,
              "partial_unexpected_counts": []
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_proportion_of_unique_values_to_be_between",
              "kwargs": {
                "column": "ever_married",
                "max_value": 0.2,
                "min_value": 0.0011855364552459987,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 0.2
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_be_in_type_list",
              "kwargs": {
                "column": "ever_married",
                "type_list": [
                  "CHAR",
                  "NCHAR",
                  "VARCHAR",
                  "NVARCHAR",
                  "TEXT",
                  "NTEXT",
                  "STRING",
                  "StringType",
                  "string",
                  "str",
                  "object",
                  "dtype('O')"
                ],
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "element_count": 5,
              "unexpected_count": 0,
              "unexpected_percent": 0.0,
              "partial_unexpected_list": [],
              "missing_count": 0,
              "missing_percent": 0.0,
              "unexpected_percent_total": 0.0,
              "unexpected_percent_nonmissing": 0.0,
              "partial_unexpected_index_list": null,
              "partial_unexpected_counts": []
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_be_in_set",
              "kwargs": {
                "column": "work_type",
                "value_set": [
                  "Govt_job",
                  "Never_worked",
                  "Private",
                  "Self-employed",
                  "children"
                ],
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "element_count": 5,
              "unexpected_count": 0,
              "unexpected_percent": 0.0,
              "partial_unexpected_list": [],
              "missing_count": 0,
              "missing_percent": 0.0,
              "unexpected_percent_total": 0.0,
              "unexpected_percent_nonmissing": 0.0,
              "partial_unexpected_index_list": null,
              "partial_unexpected_counts": []
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_not_be_null",
              "kwargs": {
                "column": "work_type",
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "element_count": 5,
              "unexpected_count": 0,
              "unexpected_percent": 0.0,
              "partial_unexpected_list": [],
              "partial_unexpected_index_list": null,
              "partial_unexpected_counts": []
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_proportion_of_unique_values_to_be_between",
              "kwargs": {
                "column": "work_type",
                "max_value": 0.4,
                "min_value": 0.002963841138114997,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 0.6
            },
            "success": false
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_be_in_type_list",
              "kwargs": {
                "column": "work_type",
                "type_list": [
                  "CHAR",
                  "NCHAR",
                  "VARCHAR",
                  "NVARCHAR",
                  "TEXT",
                  "NTEXT",
                  "STRING",
                  "StringType",
                  "string",
                  "str",
                  "object",
                  "dtype('O')"
                ],
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "element_count": 5,
              "unexpected_count": 0,
              "unexpected_percent": 0.0,
              "partial_unexpected_list": [],
              "missing_count": 0,
              "missing_percent": 0.0,
              "unexpected_percent_total": 0.0,
              "unexpected_percent_nonmissing": 0.0,
              "partial_unexpected_index_list": null,
              "partial_unexpected_counts": []
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_be_in_set",
              "kwargs": {
                "column": "Residence_type",
                "value_set": [
                  "Rural",
                  "Urban"
                ],
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "element_count": 5,
              "unexpected_count": 0,
              "unexpected_percent": 0.0,
              "partial_unexpected_list": [],
              "missing_count": 0,
              "missing_percent": 0.0,
              "unexpected_percent_total": 0.0,
              "unexpected_percent_nonmissing": 0.0,
              "partial_unexpected_index_list": null,
              "partial_unexpected_counts": []
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_not_be_null",
              "kwargs": {
                "column": "Residence_type",
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "element_count": 5,
              "unexpected_count": 0,
              "unexpected_percent": 0.0,
              "partial_unexpected_list": [],
              "partial_unexpected_index_list": null,
              "partial_unexpected_counts": []
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_proportion_of_unique_values_to_be_between",
              "kwargs": {
                "column": "Residence_type",
                "max_value": 0.2,
                "min_value": 0.0011855364552459987,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 0.4
            },
            "success": false
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_be_in_type_list",
              "kwargs": {
                "column": "Residence_type",
                "type_list": [
                  "CHAR",
                  "NCHAR",
                  "VARCHAR",
                  "NVARCHAR",
                  "TEXT",
                  "NTEXT",
                  "STRING",
                  "StringType",
                  "string",
                  "str",
                  "object",
                  "dtype('O')"
                ],
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "element_count": 5,
              "unexpected_count": 0,
              "unexpected_percent": 0.0,
              "partial_unexpected_list": [],
              "missing_count": 0,
              "missing_percent": 0.0,
              "unexpected_percent_total": 0.0,
              "unexpected_percent_nonmissing": 0.0,
              "partial_unexpected_index_list": null,
              "partial_unexpected_counts": []
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_min_to_be_between",
              "kwargs": {
                "column": "avg_glucose_level",
                "max_value": 60,
                "min_value": 55.22,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 66.85
            },
            "success": false
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_max_to_be_between",
              "kwargs": {
                "column": "avg_glucose_level",
                "max_value": 271.74,
                "min_value": 150,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 100.26
            },
            "success": false
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_mean_to_be_between",
              "kwargs": {
                "column": "avg_glucose_level",
                "max_value": 107,
                "min_value": 95,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 79.824
            },
            "success": false
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_median_to_be_between",
              "kwargs": {
                "column": "avg_glucose_level",
                "max_value": 98,
                "min_value": 75,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 73.87
            },
            "success": false
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_quantile_values_to_be_between",
              "kwargs": {
                "allow_relative_error": "lower",
                "column": "avg_glucose_level",
                "quantile_ranges": {
                  "quantiles": [
                    0.05,
                    0.25,
                    0.5,
                    0.75,
                    0.95
                  ],
                  "value_ranges": [
                    [
                      55,
                      62
                    ],
                    [
                      60,
                      78
                    ],
                    [
                      91.68,
                      97
                    ],
                    [
                      100,
                      113.01
                    ],
                    [
                      120,
                      217.08
                    ]
                  ]
                },
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": {
                "quantiles": [
                  0.05,
                  0.25,
                  0.5,
                  0.75,
                  0.95
                ],
                "values": [
                  66.85,
                  73.72,
                  73.87,
                  84.42,
                  84.42
                ]
              },
              "details": {
                "success_details": [
                  false,
                  true,
                  false,
                  false,
                  false
                ]
              }
            },
            "success": false
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_not_be_null",
              "kwargs": {
                "column": "avg_glucose_level",
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "element_count": 5,
              "unexpected_count": 0,
              "unexpected_percent": 0.0,
              "partial_unexpected_list": [],
              "partial_unexpected_index_list": null,
              "partial_unexpected_counts": []
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_proportion_of_unique_values_to_be_between",
              "kwargs": {
                "column": "avg_glucose_level",
                "max_value": 1,
                "min_value": 0.917605216360403,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 1.0
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_be_in_type_list",
              "kwargs": {
                "column": "avg_glucose_level",
                "type_list": [
                  "FLOAT",
                  "FLOAT4",
                  "FLOAT8",
                  "FLOAT64",
                  "DOUBLE",
                  "DOUBLE_PRECISION",
                  "NUMERIC",
                  "FloatType",
                  "DoubleType",
                  "float",
                  "float_",
                  "float16",
                  "float32",
                  "float64",
                  "number",
                  "DECIMAL",
                  "REAL"
                ],
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": "float64"
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_min_to_be_between",
              "kwargs": {
                "column": "bmi",
                "max_value": 24,
                "min_value": 13.3,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 25.7
            },
            "success": false
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_max_to_be_between",
              "kwargs": {
                "column": "bmi",
                "max_value": 92.0,
                "min_value": 43,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 29.3
            },
            "success": false
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_mean_to_be_between",
              "kwargs": {
                "column": "bmi",
                "max_value": 31,
                "min_value": 26,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 27.45
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_median_to_be_between",
              "kwargs": {
                "column": "bmi",
                "max_value": 31,
                "min_value": 26,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 27.4
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_quantile_values_to_be_between",
              "kwargs": {
                "allow_relative_error": "lower",
                "column": "bmi",
                "quantile_ranges": {
                  "quantiles": [
                    0.05,
                    0.25,
                    0.5,
                    0.75,
                    0.95
                  ],
                  "value_ranges": [
                    [
                      16,
                      24
                    ],
                    [
                      22,
                      26
                    ],
                    [
                      26,
                      31
                    ],
                    [
                      30,
                      34
                    ],
                    [
                      31,
                      43
                    ]
                  ]
                },
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": {
                "quantiles": [
                  0.05,
                  0.25,
                  0.5,
                  0.75,
                  0.95
                ],
                "values": [
                  25.7,
                  25.7,
                  26.0,
                  28.8,
                  28.8
                ]
              },
              "details": {
                "success_details": [
                  false,
                  true,
                  true,
                  false,
                  false
                ]
              }
            },
            "success": false
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_not_be_null",
              "kwargs": {
                "column": "bmi",
                "mostly": 0.6,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "element_count": 5,
              "unexpected_count": 1,
              "unexpected_percent": 20.0,
              "partial_unexpected_list": [
                null
              ],
              "partial_unexpected_index_list": null,
              "partial_unexpected_counts": [
                {
                  "value": null,
                  "count": 1
                }
              ]
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_proportion_of_unique_values_to_be_between",
              "kwargs": {
                "column": "bmi",
                "max_value": 1,
                "min_value": 0.2041949413942011,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 1.0
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_be_in_type_list",
              "kwargs": {
                "column": "bmi",
                "type_list": [
                  "FLOAT",
                  "FLOAT4",
                  "FLOAT8",
                  "FLOAT64",
                  "DOUBLE",
                  "DOUBLE_PRECISION",
                  "NUMERIC",
                  "FloatType",
                  "DoubleType",
                  "float",
                  "float_",
                  "float16",
                  "float32",
                  "float64",
                  "number",
                  "DECIMAL",
                  "REAL"
                ],
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": "float64"
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_be_in_set",
              "kwargs": {
                "column": "smoking_status",
                "value_set": [
                  "Unknown",
                  "formerly smoked",
                  "never smoked",
                  "smokes"
                ],
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "element_count": 5,
              "unexpected_count": 0,
              "unexpected_percent": 0.0,
              "partial_unexpected_list": [],
              "missing_count": 0,
              "missing_percent": 0.0,
              "unexpected_percent_total": 0.0,
              "unexpected_percent_nonmissing": 0.0,
              "partial_unexpected_index_list": null,
              "partial_unexpected_counts": []
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_not_be_null",
              "kwargs": {
                "column": "smoking_status",
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "element_count": 5,
              "unexpected_count": 0,
              "unexpected_percent": 0.0,
              "partial_unexpected_list": [],
              "partial_unexpected_index_list": null,
              "partial_unexpected_counts": []
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_proportion_of_unique_values_to_be_between",
              "kwargs": {
                "column": "smoking_status",
                "max_value": 0.4,
                "min_value": 0.0023710729104919974,
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "observed_value": 0.4
            },
            "success": true
          },
          {
            "exception_info": {
              "raised_exception": false,
              "exception_traceback": null,
              "exception_message": null
            },
            "meta": {},
            "expectation_config": {
              "expectation_type": "expect_column_values_to_be_in_type_list",
              "kwargs": {
                "column": "smoking_status",
                "type_list": [
                  "CHAR",
                  "NCHAR",
                  "VARCHAR",
                  "NVARCHAR",
                  "TEXT",
                  "NTEXT",
                  "STRING",
                  "StringType",
                  "string",
                  "str",
                  "object",
                  "dtype('O')"
                ],
                "batch_id": "cc97c050f8d02734791081205ad9b054"
              },
              "meta": {}
            },
            "result": {
              "element_count": 5,
              "unexpected_count": 0,
              "unexpected_percent": 0.0,
              "partial_unexpected_list": [],
              "missing_count": 0,
              "missing_percent": 0.0,
              "unexpected_percent_total": 0.0,
              "unexpected_percent_nonmissing": 0.0,
              "partial_unexpected_index_list": null,
              "partial_unexpected_counts": []
            },
            "success": true
          }
        ],
        "success": false
      },
      "actions_results": {
        "store_validation_result": {
          "class": "StoreValidationResultAction"
        },
        "store_evaluation_params": {
          "class": "StoreEvaluationParametersAction"
        },
        "update_data_docs": {
          "local_site": "file:///home/isaac/Downloads/airflow/stroke_prediction_airflow/great_expectations/uncommitted/data_docs/local_site/validations/stroke_data/csv/warning/20220615T100608.971549Z/20220615T100608.971549Z/cc97c050f8d02734791081205ad9b054.html",
          "class": "UpdateDataDocsAction"
        }
      }
    }
  },
  "success": false
}