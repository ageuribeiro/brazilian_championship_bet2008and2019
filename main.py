#importando as bibliotecas

from datetime import datetime
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,f1_score, precision_score, recall_score
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import scale
import json

#criando o dataframe 
#dados foram extraídos do site https://www.football-data.co.uk/brazil.php onde contem informações de diversos campeonatos ao redor do mundo.
data = pd.read_csv('dados.csv')

#visualizar os dados
display(data.head())

#explorando os dados
#Base de dados dos campeonatos de 2012 a 2017
matches = data.shape[0]

features = data.shape[1]

#vitorias em casa
home_win = len(data[data.Res=='H'])

#vitorias do visitante
away_win = len(data[data.Res=='A'])

#empates
draw = len(data[data.Res=='D'])
val=[home_win, away_win, draw]

win_rate = (float(home_win)/(matches))*100

print("Total de jogos: ", matches)
print("Total de colunas: ", features)
print("Total de jogos ganho em casa: ", home_win)
print("Total de jogos ganho pelo visitante: ", away_win)
print("Total de jogos empatados: ", draw)
print('Percentual de jogos ganho em casa: , {:.2f}%'.format(win_rate))

#visualizando os dados
x = np.arange(3)
plt.bar(x,val)
plt.xticks(x,('Home','Away','Draw'))
plt.show()

#Preparando os dados

#Deixar somente as variáveis numéricas
num_data = data.drop(['Country','League','Season','Date','Time','Home','Away'],1)

#visualizar os dados limpos
display(num_data.head())

#separa as features
features = num_data.drop(['Res'],1)

#separa as labels
labels = num_data['Res']

print('Features')
print(features.head())

print('==========')

print('Labels')
print(labels.head())

#Escolhendo as melhores features com kbest

features_list = ('HG','AG','PH','PD','PA','MaxH','MaxD','MaxA','AvgH','AvgD','AvgA')

k_best_features = SelectKBest(k='all')
k_best_features.fit_transform(features, labels)
k_best_features_scores = k_best_features.scores_
raw_pairs = zip(features_list[1:], k_best_features_scores)
ordered_pairs = list(reversed(sorted(raw_pairs, key=lambda x:[1])))

k_best_features_final = dict(ordered_pairs[:15])
best_features = k_best_features_final.keys()
print('')
print("Melhores Features")
print(k_best_features_final)