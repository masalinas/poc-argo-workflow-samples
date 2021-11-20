# deploy argo workflow artifact(minio) mode
argo -n argo submit --watch poc-artifact-workflow.yaml -p dataset-source="https://raw.githubusercontent.com/ec-jrc/COVID-19/master/data-by-country/jrc-covid-19-countries-latest.csv"

# deploy argo workflow volume mode
argo -n argo submit --watch poc-volume-workflow.yaml -p dataset-source="https://raw.githubusercontent.com/ec-jrc/COVID-19/master/data-by-country/jrc-covid-19-countries-latest.csv"