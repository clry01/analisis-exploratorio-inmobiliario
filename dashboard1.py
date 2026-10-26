
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# ==========================================
# PROYECTO: ANALISIS DE DATOS INMOBILIARIOS
# DIA 21 - ANALISIS EXPLORATORIO (EDA)
# ==========================================

# 1. CARGA DE DATOS
df = pd.read_csv(
    "ventas_excel.csv",
    encoding="latin1",
    sep=";"
)

# 2. PREPARACION Y VALIDACION DE DATOS
df["dFechaVenta"] = pd.to_datetime(
    df["dFechaVenta"],
    format="%d/%m/%Y",
    errors="coerce"
)

print("\n========== EXPLORACION INICIAL ==========")
print("Dimensiones:", df.shape)
print("\nTipos de datos:")
print(df.dtypes)

print("\nValores faltantes por columna:")
print(df.isna().sum())

print("\nFechas no validas:", df["dFechaVenta"].isna().sum())
print("Contratos duplicados:", df["nIdContrato"].duplicated().sum())
print("Montos iguales a cero:", (df["nMontoFinanciado"] == 0).sum())
print("Montos negativos:", (df["nMontoFinanciado"] < 0).sum())

# Revisar montos faltantes sin mostrar nombres de clientes
print("\n--- CONTRATOS SIN MONTO ---")
print(
    df.loc[
        df["nMontoFinanciado"].isna(),
        ["nIdContrato", "dFechaVenta", "Proyecto"]
    ].to_string(index=False)
)

# Revisar montos cero o negativos
print("\n--- MONTOS QUE REQUIEREN REVISION ---")
casos_revisar = df[df["nMontoFinanciado"] <= 0]

print(
    casos_revisar[
        ["nIdContrato", "dFechaVenta", "Proyecto", "nMontoFinanciado"]
    ].to_string(index=False)
)

# 3. RESUMEN GENERAL
print("\n========== RESUMEN GENERAL ==========")

print("Total de registros:", len(df))
print("Proyectos:", df["Proyecto"].nunique())
print("Contratos unicos:", df["nIdContrato"].nunique())
print("Montos faltantes:", df["nMontoFinanciado"].isna().sum())

print(
    "Monto financiado total:",
    f"S/ {df['nMontoFinanciado'].sum():,.2f}"
)
print(
    "Monto financiado promedio:",
    f"S/ {df['nMontoFinanciado'].mean():,.2f}"
)
print(
    "Mediana del monto financiado:",
    f"S/ {df['nMontoFinanciado'].median():,.2f}"
)

print(
    "Periodo analizado:",
    df["dFechaVenta"].min().strftime("%d/%m/%Y"),
    "al",
    df["dFechaVenta"].max().strftime("%d/%m/%Y")
)

# Estadisticas descriptivas
print("\n--- ESTADISTICAS DE MONTOS ---")
print(df["nMontoFinanciado"].describe().round(2))

# 4. ANALISIS POR PROYECTO
resumen_proyectos = (
    df.groupby("Proyecto")
    .agg(
        Cantidad_Contratos=("nIdContrato", "count"),
        Monto_Total=("nMontoFinanciado", "sum"),
        Monto_Promedio=("nMontoFinanciado", "mean")
    )
    .sort_values("Monto_Total", ascending=False)
)

print("\n========== RESUMEN POR PROYECTO ==========")
print(
    resumen_proyectos.to_string(
        formatters={
            "Monto_Total": lambda x: f"S/ {x:,.2f}",
            "Monto_Promedio": lambda x: f"S/ {x:,.2f}"
        }
    )
)

# 5. ANALISIS TEMPORAL
df["AnioVenta"] = df["dFechaVenta"].dt.year

contratos_anio = (
    df.groupby("AnioVenta")["nIdContrato"]
    .count()
    .sort_index()
)

monto_anual = (
    df.groupby("AnioVenta")["nMontoFinanciado"]
    .sum()
    .sort_index()
)

print("\n--- CONTRATOS POR AÑO ---")
print(contratos_anio)

print("\n--- MONTO FINANCIADO POR AÑO ---")
print(monto_anual.map(lambda x: f"S/ {x:,.2f}"))

# 6. PREPARAR CARPETA PARA LOS GRAFICOS
os.makedirs("graficos", exist_ok=True)

# Formato de soles para los ejes
formato_soles = FuncFormatter(lambda x, pos: f"S/ {x:,.0f}")

# 7. GRAFICO: MONTO TOTAL POR PROYECTO
ax = resumen_proyectos["Monto_Total"].sort_values().plot(
    kind="barh",
    figsize=(10, 5)
)
ax.xaxis.set_major_formatter(formato_soles)
plt.title("Monto financiado total por proyecto")
plt.xlabel("Monto financiado (S/)")
plt.ylabel("Proyecto")
plt.tight_layout()
plt.savefig("graficos/monto_total_proyecto.png", dpi=150)
plt.show()
plt.close()

# 8. GRAFICO: CONTRATOS POR PROYECTO
ax = resumen_proyectos["Cantidad_Contratos"].sort_values().plot(
    kind="barh",
    figsize=(10, 5)
)
plt.title("Cantidad de contratos por proyecto")
plt.xlabel("Numero de contratos")
plt.ylabel("Proyecto")
plt.tight_layout()
plt.savefig("graficos/contratos_proyecto.png", dpi=150)
plt.show()
plt.close()

# 9. GRAFICO: MONTO PROMEDIO POR PROYECTO
ax = resumen_proyectos["Monto_Promedio"].sort_values().plot(
    kind="barh",
    figsize=(10, 5)
)
ax.xaxis.set_major_formatter(formato_soles)
plt.title("Monto financiado promedio por proyecto")
plt.xlabel("Monto promedio (S/)")
plt.ylabel("Proyecto")
plt.tight_layout()
plt.savefig("graficos/promedio_proyecto.png", dpi=150)
plt.show()
plt.close()

# 10. GRAFICO: EVOLUCION DE CONTRATOS
contratos_anio.plot(
    kind="line",
    marker="o",
    figsize=(9, 5)
)
plt.title("Evolucion anual de contratos")
plt.xlabel("Año")
plt.ylabel("Cantidad de contratos")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("graficos/contratos_por_anio.png", dpi=150)
plt.show()
plt.close()

# 11. GRAFICO: EVOLUCION DEL MONTO FINANCIADO
ax = monto_anual.plot(
    kind="line",
    marker="o",
    figsize=(10, 5)
)
ax.yaxis.set_major_formatter(
    FuncFormatter(lambda x, pos: f"S/ {x / 1_000_000:.0f} M")
)
plt.title("Evolucion anual del monto financiado")
plt.xlabel("Año")
plt.ylabel("Monto financiado (millones de S/)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("graficos/monto_por_anio.png", dpi=150)
plt.show()
plt.close()

# 12. GRAFICO: DISTRIBUCION DE MONTOS
plt.figure(figsize=(9, 5))
plt.boxplot(df["nMontoFinanciado"].dropna())
plt.title("Distribucion de montos financiados")
plt.ylabel("Monto financiado (S/)")
plt.gca().yaxis.set_major_formatter(
    FuncFormatter(lambda x, pos: f"{x / 1_000_000:.1f} M")
)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("graficos/distribucion_montos.png", dpi=150)
plt.show()
plt.close()

# 13. EXPORTAR RESULTADOS
resumen_proyectos.to_csv(
    "resumen_proyectos.csv",
    encoding="utf-8-sig"
)

print("\n========== PROCESO FINALIZADO ==========")
print("Resumen exportado: resumen_proyectos.csv")
print("Graficos guardados en la carpeta: graficos")
