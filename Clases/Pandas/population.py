#Python interactive Window
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np


# %%
df_pob=pd.read_csv('poblacion.csv')
df_pob


# %%
df_pob['year']=pd.Categorical(df_pob['year'].apply(str))


# %%
df_pob.dtypes


# %%
idx_filtro = df_pob['Country'].isin(['Aruba','Colombia'])
idx_filtro


# %%
df_sample = df_pob[idx_filtro]
df_sample


# %%
df_sample=df_sample.set_index(['Country','year']).sort_index()
df_sample


# %%
df_sample.loc['Colombia',:]


# %%
df_sample.loc['Colombia',:].loc['2018',:]


# %%
df_countries = df_pob.set_index(['Country','year']).sort_index()


# %%
df_countries = df_pob.set_index(['Country','year']).sort_index()
df_countries


# %%
ids = pd.IndexSlice
df_countries.loc[ids['Aruba':'Austria','2015':'2017'],:].sort_index()


# %%
df_countries.index.get_level_values(0)


# %%
df_countries['pop']['Colombia']['2018']


# %%
df_countries.sum(level='year')


# %%
df_sample.unstack('year')


# %%
df_sample.unstack('Country')


