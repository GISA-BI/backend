import pandas


class DataFrameService:
    def __init__(self, path: str):
        self.df = pandas.read_csv(path, delimiter=";")

    def get_obitos_ra(self):

        self.df["Data"] = pandas.to_datetime(self.df["Data"], errors="coerce")
        self.df["Ano"] = self.df["Data"].dt.year
        df_obitos = self.df[self.df["Óbito"] == "Sim"]

        obitos_por_regiao_ano = (
            df_obitos.groupby(["RA", "Ano"]).size().reset_index(name="Óbitos")
        )

        return obitos_por_regiao_ano
