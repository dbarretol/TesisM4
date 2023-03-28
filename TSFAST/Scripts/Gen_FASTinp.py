# -*- coding: utf-8 -*-
#Esta rutina sirve pra crear archivos de entrada para el programa FAST
#FAST: https://www.nrel.gov/wind/nwtc/fast.html
#Manual de uso: https://www.osti.gov/biblio/15020796

import os
import pandas as pd

#====================================
#Estableciendo carpetas de trabajo
#====================================

cwd = os.getcwd()                                           #Directorio del script
os.chdir("../")
main_dir = os.getcwd()                                      #Directorio principal de trabajo
cfg_dir = os.path.join(main_dir,'cfg_files')                #Directorio de archivos de configuración
fast_dir = os.path.join(main_dir,'Simulaciones')            #Directorio para archivos de entrada de FAST
if_dir = os.path.join(fast_dir,'NREL_5MW','InflowWind')     #Directorio para archivos de entrada de InflowWind
ts_dir = os.path.join(if_dir,'Wind')           #Directorio para archivos de entrada de TURBSIM

#===================================================
#Leyendo datos del archivo "cfg_files/Data.xlsx"
#===================================================
os.chdir(main_dir)

Data = pd.read_excel(r'./cfg_files/Data.xlsx')

Uw = Data.loc[:,"UW"].dropna()
Seed = Data.loc[:,"Seed"].dropna()

#============================================
#Textos complementarios para FAST
#============================================
os.chdir(cfg_dir)
with open('FST1.dbarretol') as f: fst_1=f.read()
with open('FST2.dbarretol') as f: fst_2=f.read()
with open('FST3.dbarretol') as f: fst_3=f.read()

#==========================================
#Textos complementarios para InflowWind
#==========================================
with open('IF1.dbarretol') as f: if_1=f.read()
with open('IF2.dbarretol') as f: if_2=f.read()

#=========================================================
#Función para determinar que archivo de ElastoDyn se 
#debe usar dependiendo de la velocidad de viento
#========================================================
def set_ED(Uw):
    if(Uw>=19):
        edyn='_pitch20.dat'
    else:
        if(Uw>=13):
            edyn='_pitch10.dat'
        else:
            edyn='_pitch0.dat'
    
    return edyn
    
#================================================
#Generar el archivo de entrada para inflowwind
#================================================
def gen_IFwind(Uw, n_seed):
    IF_file = open("Uw"+str("{0:.1f}".format(Uw))+"_S"+str(n_seed)+".dat",'w+')
    IF_content = if_1+"Wind/Uw"+str("{0:.1f}".format(Uw))+"_S"+str(n_seed)+".bts"+if_2
    IF_file.write(IF_content)
    IF_file.close()

#=================================================
#Creación de archivos de entrada de InflowWind
#===================================================
os.chdir(if_dir)

for i in range(len(Seed)):
    for j in range(len(Uw)):
        gen_IFwind(Uw[j], i+1)

#=================================================
#Creación de archivos de entrada de FAST
#===================================================
os.chdir(fast_dir)
for i in range(len(Seed)):
    for j in range(len(Uw)):
        ed_line = set_ED(Uw[j])
        if_line = "Uw"+str("{0:.1f}".format(Uw[j]))+"_S"+str(i+1)+".dat"
        fst_title = "Uw"+str("{0:.1f}".format(Uw[j]))+"_S"+str(i+1)+".fst"
        fst_content = fst_1+'Onshore_ElastoDyn'+ed_line+fst_2+'InflowWind/'+if_line+fst_3
        
        fst_file = open(fst_title,'w+')
        fst_file.write(fst_content)
        fst_file.close()
        
