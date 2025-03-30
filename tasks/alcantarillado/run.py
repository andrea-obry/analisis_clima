# importacion de librerias 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# funciones utiles 

# funcion de carga de archivo csv, recibe path del archivo csv 
def cargar_archivo(path):
    df = pd.read_csv(path)
    return df

# funcion de validacion de datos en rango
# recibe un mensaje a presentar al usuario, un minimo y un maximo
# repite mientras el numero ingresado no se encuentre entre los limites
# cuando el numero sea valido, regresa el numero ingresado
def v_input_range(msg,min, max):
    while True:
        try:
            numero = float(input(msg))
            if numero >= min and numero <= max:
                return numero
            else:
                print("El numero ingresado esta fuera del rango. Intente nuevamente.")
        except:
            print("El numero ingresado no es valido. Intente nuevamente.")

# funcion de validacion de datos en lista
# recibe un mensaje a presentar al usuario, una lista de valores validos
# Repite mientras el valor ingresado no este en la lista
def v_input_list(msg, lista):
    while True:
        try:
            valor = float(input(msg))
            if valor in lista:
                return valor
            else:
                print("El valor ingresado no esta en la lista, intente nuevamente.")
        except:
            print("El valor ingresado no es valido. Intente nuevamente.")

# funcion de calcular el diametro de la alcantarilla
# recibe los parametros de la funcion calcular_diametro usando la ecuacion de Manning
# recive la precpitacion en mm (precipitacion_mm)
# recibe el pendiente del terreno (p_t)
# recibe el tiempo de concentracion en horas (t_c)
# recibe el área de captación en hectáreas (a_c)
# recibe el coeficiente de escorrentía (c_e)
# recibe el coeficiente de Manning (c_m)
# regresa el diametro de la alcantarilla en metros
def calcular_diametro(precipitacion_mm, p_t, t_c, a_c, c_e, c_m):
    I=(precipitacion_mm/1000)/(t_c*3600) #intensidad de lluvia
    Q=c_e*I*a_c*10000 #caudal
    R = (Q * c_m / (np.pi * p_t**(1/2)))**(3/8) #radio hidraulico
    D = 4*R #diámetro
    return D

# carga de datos del archivo csv
# las columnas del dataframe son year_month (año_mes), precipitation (precipitación_mm)
datos = cargar_archivo('data/csv/precipitation.csv')


# carga y validacion de las entradas del usuario 

p_t=v_input_range('Pendiente del terreno (m/m) [Entre 0.1 y 1]: ',0.1,1)
t_c=v_input_range('Tiempo de concentración (horas) [Entre 0.1 y 10]: ',0.1,10)
a_c=v_input_range('Area de captación (hectáreas): [Entre 0.5 y 100]: ',0.5,100)
c_e=v_input_list('Coeficiente de escorrentía '
            '\n0.6 para pavimento'
            '\n0.3 para tierra '
            '\n >>>: '
            ,[0.6,0.3])
c_m=v_input_list('Coeficiente de Manning '
          '\n0.012 para concreto liso'
          '\n0.015 para concreto rugoso'
          '\n0.009 para PVC'
          '\n0.024 para acero corrugado'
          '\n0.012 para polietileno HDPE'
          '\n0.017 para ladrillo'
          '\n0.013 para hormigón armado'
          '\n0.025 para canal de tierra'
          '\n0.035 para canal de roca'
          '\n0.030 para mamposteria de piedra'
          '\n >>>: '
          ,[0.012,0.015,0.009,0.024,0.012,0.017,0.013,0.025,0.035,0.030])

# Con los valores ingresados mas los datos del archivo calculamos el diámetro de la alcantarilla
datos['diameter']=datos['precipitation'].apply(lambda x: calcular_diametro(x,p_t,t_c,a_c,c_e,c_m))

# grafico de los datos
fig, ax1 = plt.subplots(figsize=(12, 6))
ax1.plot(datos['year_month'], datos['diameter'], 'r-', label='Diámetro (m)')
ax1.set_xlabel('Mes')
ax2 = ax1.twinx()
ax2.plot(datos['year_month'], datos['precipitation'], 'b-', label='Precipitación (mm)')
ax2.get_xaxis().set_visible(False)
ax1.grid(True)
plt.title('Precipitación vs Diámetro')
ax1.tick_params(axis='x', labelrotation=90)
fig.legend(loc='upper right')
plt.tight_layout()
plt.show()