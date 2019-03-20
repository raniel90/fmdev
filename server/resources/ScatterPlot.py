import pandas as pd
from flask_restful import Resource

df = pd.read_csv('base.csv', index_col=0)
df.columns = [item.upper() for item in df.columns]

class ScatterPlotResource(Resource):
    def get(self):
        items = []
        items_anomaly = []

        for cluster in df['CLUSTER'].unique():
            dataX = df[ (df['CLUSTER']==cluster) & (df['ANOMALY'] == 1) ]['TOTAL_BILL']
            dataY = df[ (df['CLUSTER']==cluster) & (df['ANOMALY'] == 1) ]['TIP']

            items.append({
                "x": dataX.tolist(), 
                "y": dataY.tolist(), 
                "mode": 'markers',
                "name": 'Cluster ' + str(cluster) + ' sem poss. anom.',
                "marker": dict(size=10, line=dict(width=1.5))
                })

        items_anomaly.append({
            "x": df[df['ANOMALY'] == -1]['TOTAL_BILL'].tolist(), 
            "y": df[df['ANOMALY'] == -1]['TIP'].tolist(), 
            "mode": 'markers',
            "name": 'Poss. Anomalia',
            "text": list(map(lambda x: 'Cluster ' + x, map(str, df[df['ANOMALY'] == -1]['CLUSTER'].values))),
            "marker": dict(
                size = 12.5,
                color = 'rgb(255,0,0)',
                line = dict(
                    width=1.5
                    )
                )
            })

        items.extend(items_anomaly)

        return {"status":"success", "data": items}, 200