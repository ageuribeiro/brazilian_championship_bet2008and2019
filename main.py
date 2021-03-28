from datetime import datetime
import pandas as pd
import numpy as np
import json

#criando o dataframe 
df = pd.read_csv('dados.csv')

#visualizar os dados
df.head(5)