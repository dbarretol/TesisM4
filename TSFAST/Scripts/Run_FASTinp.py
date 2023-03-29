# -*- coding: utf-8 -*-
#Este programa sirve para ejecutar simulaciones en TURBSIM, tiene tres opciones para ejecutar las simulaciones:
#   a) Correr un caso especifico
#   b) Correr varios casos listados en el archivo "ListFSTinp.txt"
#   c) Correr todos los casos en la carpeta ".\Simulaciones\NREL_5MW\Wind"

import os, time
import subprocess as sp
import multiprocessing as mp
from multiprocessing import Pool

#Esta línea debe actualizarse se acuerdo a en donde se ubique el ejecutable de TURBSIM
app_fst="C:/FAST/Fast V8/bin/FAST_Win32.exe"
n_cpus = mp.cpu_count()-1


#=================================================
#Función para establecer directorios de trabajo
#=================================================
def set_dirs():
    print("Estableciendo directorios de trabajo...")
    script_dir=os.path.dirname(os.path.abspath(__file__))    
    os.chdir("../")
    main_dir = os.getcwd()
    fast_dir = os.path.join(main_dir, 'Simulaciones')
    
    print("El directorio principal es:\t"+main_dir)
    print("El directorio de los scripts es:\t"+script_dir)
    print("El directorio de los archivos de entrada de FAST es:\t"+fast_dir)
    
    return main_dir, script_dir, fast_dir
    
#================================
# Función para correr turbsim
#================================
def run_fast(inp_file):
    t_start=time.time()
      
    #verificar que la extensión del input file es correcta
    if inp_file.endswith('.fst'):
        pass
    else:
        inp_file = inp_file+'.fst'
    
    #Iniciar turbsim
    fst_instance = sp.run([app_fst,inp_file], stdout=sp.PIPE, stderr=sp.STDOUT, universal_newlines=True)
    rc = fst_instance.returncode       # rc = 0 (exitoso)
    
    #Información de estado de la simulación
    sim_status = list()
    for output in fst_instance.stdout:
        sim_status.append(output)
        
    #Guardando información del estado de la simulación en un archivo externo
    info_sim = open(str(rc)+"-"+inp_file[:-4]+'.fstinfo','w+')
    for e in range(len(sim_status)):
        info_sim.write(sim_status[e])
    info_sim.close()
    
    print("La simulación del caso "+inp_file[:-4]+" demoró "+"{0:.3f}".format(time.time()-t_start)+" segundos")

#==========================================================
#Función para leer los casos en el archivo "ListFSTinp.xt"
#==========================================================
def get_cases_op2(): 
   #Leer el contenido del archivo
    with open('ListFSTinp.txt') as f: fst_cases = f.read()
    fst_cases = fst_cases.split('\n')
    
    #Verificando que incluyan la extensión .fst
    for i in range(len(fst_cases)):
        if fst_cases[i].endswith('.fst'):
            pass
        else:
            fst_cases[i] = fst_cases[i]+'.fst'
            
    return fst_cases

#==============================================================================
#Función para listar todos los casos en la carpeta '.\Simulaciones'
#==============================================================================
def get_cases_op3():
    fst_cases = os.popen("dir /b *.fst").read()
    fst_cases = fst_cases.split("\n")
    del fst_cases[-1]
    
    return fst_cases
#=========================================================
#Función para agrupar los casos en lotes de tamaño 'k'
#=========================================================
def group_cases(list_cases, k):
    new_list_cases = [list_cases[i:i+k] for i in range(0,len(list_cases),k)]
    
    return new_list_cases    

#***********************************
#PROGAMA PRINCIPAL
#***********************************

if __name__ == '__main__':
    #directorios de trabajo
    main_dir, script_dir, fast_dir = set_dirs()
    os.chdir(fast_dir)
    print("Se van a utilizar "+str(n_cpus)+" cpus")
    print("""
      ================================================
      PROGRAMA PARA EJECUTAR SIMULACIONES EN FAST
      ================================================""")
    
    print("""
      Elegir una opción:
      \t 1: Ejecutar un caso especifico
      \t 2: Ejecutar los casos del archivo 'ListFSTinp.txt'
      \t 3: Ejecutar todos los casos en la carpeta '.\Simulaciones'
      """)
    op = int(input("Ingrese su opción..."))
    l_op = [1, 2, 3]
      
    while op in l_op:
        if op == 1:
            print("Elegiste correr un caso especifico")
            run_fast(input("Indica el nombre del caso =>"))
            
        if op == 2:
            x2 = get_cases_op2()
            print("Se van a ejecutar un total de "+str(len(x2))+" casos")
            
            k = int(input("Cuantos casos en paralelo deseas ejecutar? =>"))
            new_x2 = group_cases(x2, k)
            print("Se van a ejecutar "+str(len(new_x2))+" lotes...")
            tt = time.time()
            
            for i in range(len(new_x2)):
                print("Mandando el lote n° "+str(i+1)+" de "+str(len(new_x2))+"...")
                
                t_start = time.time()
                with Pool(processes = n_cpus) as proc:
                    proc.map(run_fast,new_x2[i])
                print("Este lote demoró "+"{0:.3f}".format(time.time()-t_start)+" segundos")
            print("Las"+str(len(x2))+" simulaciones demoraron "+"{0:.3f}".format(time.time()-tt)+" segundos")
        
        if op == 3:
            x3 = get_cases_op3()
            print("Se van a ejecutar un total de "+str(len(x3))+" casos")
            
            k = int(input("Cuantos casos en paralelo deseas ejecutar? =>"))
            new_x3 = group_cases(x3, k)
            print("Se van a ejecutar "+str(len(new_x3))+" lotes...")
            tt = time.time()
            
            for j in range(len(new_x3)):
                print("Mandando el lote n° "+str(j+1)+" de "+str(len(new_x3))+"...")
                
                t_start = time.time()
                with Pool(processes = n_cpus) as proc:
                    proc.map(run_fast,new_x3[j])
                print("Este lote demoró "+"{0:.3f}".format(time.time()-t_start)+" segundos")
            print("Las"+str(len(x3))+" simulaciones demoraron "+"{0:.3f}".format(time.time()-tt)+" segundos")

        op = int(input("Tarea Finalizada. Elija una nueva opción (1, 2, 3) o  cualquier otra para salir =>"))