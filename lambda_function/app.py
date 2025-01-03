import os
import pandas as pd
import requests

def lambda_handler(event, context):

    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = response.json()
    

    df = pd.DataFrame(data)
    print(df.head())


    print("Environment Variables:")
    for key, value in os.environ.items():
        print(f"{key}: {value}")

    return {"statusCode": 200, 
            "body": "Lambda function executed successfully"
        }