clear all
clc

%Variables fijas
ind = 4801; %indice desde donde se toman los valores
columna = 2; %2 es velocidad de viento, puede cambiar

%Obtener la ruta de la carpeta
rutaCarpeta = uigetdir();
cd(rutaCarpeta);
[~, xls_name, ~] = fileparts(rutaCarpeta); %Capturar nombre de carpeta elegida

%Obtener los nombres de los archivos en la carpeta
archivos = dir(fullfile(rutaCarpeta,'*.outb'));

%Crear matrices vacias
datos_serie = [];
datos_serie_red = [];
cases_name = [];

%Iterar sobre los nombres de los archivos
for i = 1:length(archivos)
    outb_name = archivos(i).name;
    rutaCompleta = fullfile(rutaCarpeta,outb_name);
    
    %Llamar a la funcion ReadFASTbinary
    [Channels, ~, ~, ~, ~] = ReadFASTbinary(rutaCompleta);
    
    %Procesar Channels
    param = Channels(:, columna);
    param_red = Channels(ind:end,columna);
    
    vec = [mean(param) std(param) max(param) min(param)];
    vec_red = [mean(param_red) std(param_red) max(param_red) min(param_red)];
    
    datos_serie = vertcat(datos_serie, vec);
    datos_serie_red = vertcat(datos_serie_red, vec_red);
    cases_name = vertcat({outb_name},cases_name);
end

xlswrite([xls_name '_' num2str(columna) '_cases.xlsx'], cases_name,1, 'A1')
xlswrite([xls_name '_' num2str(columna) '_mean.std.max.min.xlsx'], datos_serie,1, 'A1')
xlswrite([xls_name '_' num2str(columna) '_mean.std.max.min_red.xlsx'], datos_serie_red,1, 'A1')
