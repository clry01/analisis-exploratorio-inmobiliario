# Análisis Exploratorio de Datos Inmobiliarios con Python

## Descripción del proyecto

Este proyecto realiza un análisis exploratorio de datos (EDA) de contratos de venta inmobiliaria. El objetivo es examinar los montos financiados, comparar proyectos y analizar la evolución anual de los contratos.

Los datos utilizados provienen de una base de datos inmobiliaria y se han procesado con Python y Pandas.

## Objetivos

- Examinar la calidad y estructura de los datos.
- Identificar valores faltantes, contratos duplicados y montos que requieren revisión.
- Comparar los proyectos por cantidad de contratos, monto financiado total y monto promedio.
- Analizar la evolución anual de los contratos y montos financiados.
- Comunicar los resultados mediante visualizaciones.

## Herramientas utilizadas

- Python
- Pandas
- Matplotlib
- CSV

## Proceso de análisis

1. Carga e inspección de los datos.
2. Conversión y validación de fechas.
3. Revisión de valores faltantes, duplicados y montos no positivos.
4. Cálculo de indicadores generales y comparativos por proyecto.
5. Análisis temporal de contratos y montos financiados.
6. Creación y exportación de gráficos.
7. Exportación de un resumen de indicadores por proyecto.

## Resultados generales

- **Registros analizados:** 6,240.
- **Proyectos identificados:** 5.
- **Contratos únicos:** 6,240.
- **Monto financiado total registrado:** S/ 212,805,584.82.
- **Monto financiado promedio:** S/ 34,125.33.
- **Mediana del monto financiado:** S/ 34,800.00.
- **Periodo analizado:** del 12 de junio de 2017 al 18 de octubre de 2025.

Se identificaron cuatro registros sin monto financiado, diez con monto igual a cero y dos con monto negativo. Estos casos requieren revisión antes de considerarlos errores o excluirlos del análisis.

## Estructura del proyecto

- `dashboard1.py`: código del análisis.
- `resumen_proyectos.csv`: indicadores agregados por proyecto.
- `graficos/`: visualizaciones generadas por el script.

## Consideraciones

El monto financiado no equivale necesariamente a ingresos cobrados ni a rentabilidad. Los resultados describen los registros disponibles y no permiten, por sí solos, determinar las causas de las variaciones entre proyectos o años.

Los datos originales contienen información de clientes y no forman parte de los archivos públicos del repositorio.

## Autor

Proyecto personal de práctica para desarrollar habilidades de análisis de datos con Python.
