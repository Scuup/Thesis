import pandas as pd
df = pd.read_csv('Ratinkaantov2Converted.txt',sep=",",error_bad_lines=False)
df.to_csv('log.csv')
