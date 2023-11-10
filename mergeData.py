import pandas as pd
import numpy as np

stars = pd.read_csv("scraped_data.csv")
dwarfs = pd.read_csv("dwarf_data.csv")

stars.dropna(axis=1)
dwarfs.dropna(axis=1)

dwarfs.astype({"Mass": "float", "Radius": "float"})

dwarfs["Mass"] *= 0.102763
dwarfs["Radius"] *= 0.000954588

headers = ['id','Brown Dwarf','Constellation','Right Ascension','Declination','Apparent Magnitude','Distance','Spectral Type','Mass','Radius','Date Discovered','id','name','dist', 'mass','rad','lum']
mergeFile = pd.DataFrame(columns=headers)
mergeFile = pd.merge(dwarfs, stars)
mergeFile.to_csv("merged_data.csv")