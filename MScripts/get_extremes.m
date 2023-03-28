%Script para obtener los valores extremos globales de los archvios outb
clear all
clc
%Variables de control
%=======================================================
columna = 31; %Columna del parametro a extraer el maximo 31 para Fx, 35 para My
ind = 4801; %Limita el inicio de la srie de tiempo a tomar

% Elegir carpeta de los OUTB y obtener nombre de los archivos
filePath = uigetdir();  %Elegir carpeta
cd(filePath);           %Cambiar carpeta de trabajo  a dicha carpeta
[~, xls_name,~] = fileparts(filePath); %Obtener nombre de la carpeta elegida

outbFiles = dir(fullfile(filePath,'*.outb')); %Obtenienedo nombre de los archivos OUTB

%Crear matrices vacias
datos_Fx = [];
datos_My = [];

%Procesar
for i = 1:length(outbFiles)
    outbName = outbFiles(i).name;
    outbFullpath = fullfile(filePath,outbName);
    
    %Llamando a la funcion ReadFASTbinary
    [Channels, ~, ~, ~, ~] = ReadFASTbinary(outbFullpath);
    
    %Obteniendo valores extremos
    TS_Fx = Channels(ind:end,32); %serie de tiempo de Fx
    TS_My = Channels(ind:end,36); %serie de tiempo de My
    
    vecFx = [mean(TS_Fx) std(TS_Fx) max(TS_Fx)];
    vecMy = [mean(TS_My) std(TS_My) max(TS_My)];   
    
    datos_Fx = vertcat(datos_Fx, vecFx);    
    datos_My = vertcat(datos_My, vecMy);    
end

xlswrite([xls_name '_Fx.xlsx'], datos_Fx, 'A1')
xlswrite([xls_name '_My.xlsx'], datos_My, 'A1')
