from data_processing import (pipeline,
                            build_model,
                            evaluate_model)


def make_model(df):
    xtrain, ytrain, xtest, ytest = pipeline(df)
    build_model(xtrain, ytrain)
    return evaluate_model(xtest, ytest)


if __name__ == "__main__":
    import pandas as pd
    import os

    # Default data path
    data_path = os.path.join(os.path.dirname(__file__), "../input_data/stroke_data.csv")
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
        score = make_model(df)
        print(f"Model trained successfully. Test Score: {score:.4f}")
    else:
        print(f"Error: Data file not found at {data_path}")
