#Importaciones de módulos estándar de Python.
import warnings

#Importaciones de bibliotecas de terceros.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Importaciones de módulos locales o específicos del proyecto.
#No hay aun.

df_top_countries = pd.DataFrame()

def covid_time_series(df: pd.DataFrame):

    warnings.filterwarnings("ignore", category=FutureWarning)

    sns.lineplot(
        data=df, 
        x="date", 
        y="value", 
        hue="country_region")

    plt.xticks(rotation=15)
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Latam covid time series")
    plt.show()

def top_n_countries(df, list_countries, n):
    global n_top
    n_top = n
    top_n_countries_df = (
        df.select_columns(["country_region", "value"])
        .groupby(["country_region"])
        .aggregate("sum")
        .sort_values("value", ascending=False)
        .reset_index()
        .head(n_top)
        .transform_column(
            column_name="country_region",
            function=lambda country: "red" if country in list_countries else "lightblue",
            dest_column_name="color",
    ))
    return top_n_countries_df.head(n_top)


def plot_bars(df: pd.DataFrame):
    
    warnings.filterwarnings("ignore", category=FutureWarning)

    sns.barplot(
        data=df, 
        x="value", 
        y="country_region", 
        palette=df.color
    )

    plt.xlabel("Value")
    plt.ylabel("Country Region")
    plt.title(f"Top {n_top} - Selected Countries in a global context")
    plt.show()