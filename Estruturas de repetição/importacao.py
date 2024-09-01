from datetime import datetime,timedelta
data_atual = datetime.now()
um_dia = timedelta(days = 1)
data_anterior = data_atual - um_dia
data_posterior = data_atual + um_dia
#data_formatada = data_atual.strftime("%d/%m/%Y")
print(data_anterior)
print(data_posterior)

