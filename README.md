# brazilian_championship_bet2008and2019

Analysis of data from the Brazilian championship between 2009 and 2018 for studies of analysis techniques with Python

![DataScience](https://github.com/ageuribeiro/brazilian_championship_bet2008and2019/blob/main/datascience.gif)

## Notas para dados de futebol

Todos os dados estão em formato csv, prontos para uso em aplicativos de planilha padrão. Tenha em atenção que algumas abreviaturas já não são utilizadas (em particular as probabilidades de casas de apostas específicas que já não são utilizadas) e referem-se a dados recolhidos em temporadas anteriores. Para obter uma lista atualizada das casas de apostas incluídas no conjunto de dados, visite http://www.football-data.co.uk/matches.php

## Chave para dados de resultados:

Div = Divisão da Liga
Data = Data da Partida (dd / mm / aa)
Tempo = Hora do início da partida
HomeTeam = Home Team
Equipe Away = Equipe Away
FTHG e HG = Gols em tempo integral da equipe da casa
FTAG e AG = Gols em tempo integral fora da equipe
FTR e Res = Resultado em tempo integral (H = Vitória em casa, D = Empate, A = Vitória em casa)
HTHG = Gols da equipe da casa no intervalo
HTAG = Gols da equipe no intervalo
HTR = Resultado do intervalo (H = Vitória da casa, D = Empate, A = Vitória fora)

## Estatísticas da partida (quando disponíveis)
Presença = Presença da multidão
Árbitro = Árbitro da Partida
HS = Shots da equipe da casa
AS = Tiros fora de equipe
HST = chutes da equipe da casa no alvo
AST = Tiros fora de equipe no alvo
HHW = Home Team Hit Woodwork
AHW = Equipe ausente bateu em madeira
HC = Cantos da Equipe da Casa
AC = Cantos da Equipe Fora
HF = Faltas da equipe da casa cometidas
AF = Faltas de equipe fora cometidas
HFKC = Chutes livres da equipe da casa concedidos
AFKC = chutes livres concedidos por equipe fora
HO = Offsides da equipe da casa
AO = fora da equipe fora
HY = Cartões amarelos da equipe da casa
AY = Cartões amarelos da equipe ausente
HR = cartões vermelhos da equipe da casa
AR = Cartões vermelhos da equipe ausente
HBP = Pontos de reservas da equipe da casa (10 = amarelo, 25 = vermelho)
ABP = Pontos de reserva de equipe ausente (10 = amarelo, 25 = vermelho)

Observe que os Free Kicks Concebidos incluem faltas, offsides e qualquer outra infração cometida e sempre será igual ou superior ao número de faltas. As faltas constituem a grande maioria dos chutes livres concedidos. Os chutes livres concedidos são mostrados quando dados específicos sobre faltas não estão disponíveis (França 2ª, Bélgica 1ª e Grécia 1ª divisões).

Observe também que os cartões amarelos ingleses e escoceses não incluem o cartão amarelo inicial quando um segundo é mostrado para um jogador convertendo-o em vermelho, mas isso é incluído como amarelo (mais vermelho) para jogos europeus.


## Chave para dados de probabilidades de apostas 1X2 (correspondência):

B365H = probabilidades de vitória em casa do Bet365
B365D = probabilidades de empate Bet365
B365A = Probabilidades de vitória fora do Bet365
BSH = Probabilidades de vitória em casa no Blue Square
BSD = probabilidades de empate no quadrado azul
BSA = Probabilidades de vitória fora da Praça Azul
BWH = Probabilidades de ganhar em casa apostar e ganhar
BWD = probabilidades de sorteio de aposta e vitória
BWA = Aposte e ganhe chances de vitória fora
GBH = Probabilidades de vitória em casa do Gamebookers
GBD = Gamebookers empatam probabilidades
GBA = Probabilidades de vitória fora do Gamebookers
IWH = Probabilidades de vitória em casa da Interwetten
IWD = probabilidades de empate da Interwetten
IWA = Probabilidades de vitória fora da Interwetten
LBH = Probabilidades de vitória em casa da Ladbrokes
LBD = sorteio de probabilidades da Ladbrokes
LBA = Probabilidades de vitória fora da Ladbrokes
PSH e PH = Probabilidades de vitória em casa da Pinnacle
PSD e PD = probabilidades de empate Pinnacle
PSA e PA = Probabilidades de vitória fora da Pinnacle
SOH = Odds do Sporting para vencer em casa
SOD = odds desportivas empate odds
SOA = Odds do Sporting - odds de vitória fora
SBH = Probabilidades de vitória em casa da Sportingbet
SBD = probabilidades de empate da Sportingbet
SBA = Probabilidades de vitória fora da Sportingbet
SJH = Probabilidades de vitória em casa de Stan James
SJD = Stan James empata as probabilidades
SJA = Probabilidades de vitória fora de Stan James
SYH = Probabilidades de vitória em casa do Stanleybet
SYD = probabilidades de empate Stanleybet
SYA = Probabilidades de vitória fora de Stanleybet
VCH = Probabilidades de vitória em casa da VC Bet
VCD = probabilidades de sorteio de aposta VC
VCA = VC Aposta fora de chances de vitória
WHH = Probabilidades de vitória em casa da William Hill
WHD = sorte de sorte da William Hill
WHA = Probabilidades de vitória fora da William Hill

Bb1X2 = Número de bookmakers BetBrain usados ​​para calcular as médias e máximas das probabilidades de jogo
BbMxH = Probabilidades máximas de vitória em casa do Betbrain
BbAvH = Probabilidades médias de vitória em casa do Betbrain
BbMxD = probabilidades máximas de empate Betbrain
BbAvD = Probabilidades médias de vitória de empate do Betbrain
BbMxA = Probabilidades máximas de vitória fora do Betbrain
BbAvA = Probabilidades médias de vitória fora do Betbrain

MaxH = Probabilidades máximas de vitória em casa no mercado
MaxD = odds máximas de ganho de sorteio do mercado
MaxA = Probabilidades de vitória máxima fora do mercado
AvgH = Odds médias de mercado de vitória em casa
AvgD = Odds de vitória de empate média do mercado
AvgA = Odds de vitória média fora do mercado



## Chave para odds totais de apostas de gols:

BbOU = Número de bookmakers BetBrain usados ​​para calcular médias e máximos acima / abaixo de 2,5 gols (total de gols)
BbMx> 2,5 = máximo do Betbrain acima de 2,5 gols
BbAv> 2,5 = Média do Betbrain acima de 2,5 gols
BbMx <2,5 = Betbrain máximo abaixo de 2,5 gols
BbAv <2,5 = Média do Betbrain abaixo de 2,5 gols

GB> 2,5 = Gamebookers com mais de 2,5 gols
GB <2,5 = Gamebookers com menos de 2,5 gols
B365> 2,5 = Bet365 com mais de 2,5 gols
B365 <2,5 = Bet365 com menos de 2,5 gols
P> 2,5 = Auge em 2,5 gols
P <2,5 = Pinnacle abaixo de 2,5 gols
Máx> 2,5 = Mercado máximo acima de 2,5 metas
Máx <2,5 = Mercado máximo abaixo de 2,5 metas
Média> 2,5 = Média do mercado acima de 2,5 metas
Média <2,5 = Média do mercado abaixo de 2,5 metas



## Chave para as probabilidades de apostas com handicap asiático:

BbAH = Número de casas de apostas BetBrain utilizadas para médias e máximos de handicap asiáticos
BbAHh = tamanho do handicap Betbrain (time da casa)
AHh = Tamanho de mercado do handicap (time da casa) (desde 2019/2020)
BbMxAHH = Odds máximas da equipe da casa com handicap asiático Betbrain
BbAvAHH = Odds médias da equipe da casa com handicap asiático Betbrain
BbMxAHA = Odds máximas para time visitante com handicap asiático Betbrain
BbAvAHA = Odds médias da equipe visitante com handicap asiático do Betbrain

GBAHH = Chá caseiro para jogadores asiáticos para deficientes físicosm probabilidades
GBAHA = Probabilidades de time visitante com handicap asiático do Gamebookers
GBAH = tamanho do handicap do Gamebookers (time da casa)
LBAHH = Odds da equipa da casa com handicap asiático da Ladbrokes
LBAHA = Odds da equipa visitante com handicap asiático da Ladbrokes
LBAH = tamanho do handicap da Ladbrokes (time da casa)
B365AHH = Odds da equipe da casa com handicap asiático Bet365
B365AHA = Odds da equipe visitante com handicap asiático Bet365
B365AH = tamanho do handicap Bet365 (time da casa)
PAHH = Odds da equipe da casa com handicap asiático Pinnacle
PAHA = Odds da equipe visitante com handicap asiático no Pinnacle
MaxAHH = Odds máximas de mercado da equipe da casa com handicap asiático
MaxAHA = Odds máximas de mercado para times de handicap asiáticos
AvgAHH = Odds média de mercado da equipe da casa com handicap asiático
AvgAHA = Odds médias de mercado da equipe visitante com handicap asiático



## Probabilidades de fechamento (últimas chances antes do início da partida)

Como acima, mas com um caractere "C" adicional após a abreviatura do bookmaker / Max / Avg
A Football-Data gostaria de agradecer as seguintes fontes, que foram utilizadas na compilação dos arquivos de resultados e odds da Football-Data.


## Resultados atuais (tempo integral, intervalo)
Xcores - http: //www.xcores .com

## Estatísticas da partida
BBC, ESPN Soccer, Bundesliga.de, Gazzetta.it e Football.fr

## Probabilidades de apostas de casas de apostas
Bookmakers individuais

As probabilidades de aposta para jogos de fim de semana são coletadas nas tardes de sexta-feira e nas tardes de terça-feira para jogos no meio da semana.

Estatísticas adicionais da partida (cantos, chutes, marcações, árbitro, etc.) para as temporadas de 2000/01 e 2001/02 para as ligas inglesa, escocesa e alemã foram fornecidas pela Sports.com (agora sob nova administração e não mais disponível).
