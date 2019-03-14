import pandas as pd
from flask_restful import Resource

df = pd.read_csv('base.csv', index_col=0)
df.columns = [item.upper() for item in df.columns]

class BoxPlotResource(Resource):
    def get(self):
        items = []

        for cluster in df['CLUSTER'].unique():
            name = 'Cluster ' + str(cluster)
            values = df[df['CLUSTER'] == cluster]['TOTAL_BILL'].tolist()
            items.append({"name": name, "y": values})

        return {"status":"success", "data": items}, 200