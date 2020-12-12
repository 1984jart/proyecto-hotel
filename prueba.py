from datetime import datetime, date

fechai = datetime.strptime("2020-10-10","%Y-%m-%d")
fechaf = datetime.strptime("2020-10-05","%Y-%m-%d")

fecha=date.today()
fechahoy = datetime.strptime(str(fecha),"%Y-%m-%d")
dias= (fechaf-fechai).days
valor=150000*dias

if(fechaf<fechai):
    print("La fecha de finalizacion de la reserva debe ser superior o igual a la fecha inicial")

if(fechai<fechahoy):
    print("La fecha inicial de la reserva debe ser superior a la fecha actual")   

