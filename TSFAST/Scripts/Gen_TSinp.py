#Esta rutina sirve para crear archivos de entrada para el programa TURBSIM.
#TURBSIM: https://www.nrel.gov/wind/nwtc/turbsim.html
#Manual de uso: https://www.nrel.gov/wind/nwtc/assets/downloads/TurbSim/TurbSim_v2.00.pdf

import os
import pandas as pd

#===================================
#Estableciendo carpetas de trabajo
#===================================
cwd = os.getcwd()                                             #Directorio actual de trabajo
os.chdir("../")
main_dir = os.getcwd()                                        #Directorio principal de trabajo
cfg_dir = os.path.join(main_dir,'cfg_files')                  #Directorio de los archivos de configuración
ts_dir = os.path.join(main_dir,'Simulaciones','NREL_5MW','InflowWind','Wind')   #Directorio de archivos input para TURBSIM

#======================================================
#PASO 1: Leer datos del archivo "cfg_files/Data.xlsx"
#======================================================
os.chdir(main_dir)

Datos = pd.read_excel(r'./cfg_files/Data.xlsx')

Uw = Datos.loc[:,"UW"].dropna()
Seed = Datos.loc[:,"Seed"].dropna()

#==================================================
#PASO 2: Crear archivos input *.inp para TURBSIM
#==================================================
os.chdir(cfg_dir)
with open('TS1.dbarretol') as f: ts_1=f.read()
with open('TS2.dbarretol') as f: ts_2=f.read()
with open('TS3.dbarretol') as f: ts_3=f.read()
txt1='RandSeed1       - First random seed  (-2147483648 to 2147483647)\n'
txt2='URef            - Mean (total) wind speed at the reference height [m/s]\n' 

os.chdir(ts_dir)
for i in range(len(Seed)):
    for j in range(len(Uw)):
        TS_title="Uw"+str("{0:.1f}".format(Uw[j]))+"_S"+str(i+1)                
        TS_content=ts_1+str(int(Seed[i]))+'\t\t\t'+txt1+ts_2+str(Uw[j])+'\t\t\t'+txt2+ts_3
                
        TS_file=open(TS_title+".inp",'w+')
        TS_file.write(TS_content)
        TS_file.close()
print("Trabajo finalizado. Se crearon "+str(len(Seed)*len(Uw))+" archivos con extensión *.inp en "+ts_dir)