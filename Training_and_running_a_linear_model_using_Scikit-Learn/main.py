import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import sklearn.linear_model




def prepare_country_stats(oecd_bli, gdp_per_capita):
    oecd_bli = oecd_bli[oecd_bli["Indicator"] == "Life satisfaction"]
    
    oecd_bli = oecd_bli.groupby(["Country", "Indicator"])["Value"].mean().reset_index()
    
    oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")

    gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
    gdp_per_capita.set_index("Country", inplace=True)

    full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita,
                                  left_index=True, right_index=True)

    full_country_stats = full_country_stats[["GDP per capita", "Life satisfaction"]].dropna()

    full_country_stats.sort_values(by="GDP per capita", inplace=True)

    return full_country_stats



oecd_bli = pd.read_csv("oecd_bli_2015.csv", thousands=",")
gdp_per_capita = pd.read_csv("gdp_per_capita.csv", thousands = ',', delimiter='\t',
                             encoding='latin1', na_values='n/a')


country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)
X = np.c_[country_stats["GDP per capita"]]
y = np.c_[country_stats["Life satisfaction"]]


country_stats.plot(kind='scatter', x= "GDP per capita", y="Life satisfaction")
plt.show()

model = sklearn.linear_model.LinearRegression()

model.fit(X,y)
x_new = [[22587]]
print(model.predict(x_new))

