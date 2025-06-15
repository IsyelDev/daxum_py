import pandas as pd
import numpy as np

estudiantes = pd.DataFrame({
    "nombre":["elmer","manuel","erika"],
    "edad":[list(np.arange(0,2)) for _ in range(3)]
})
estudiantes.to_csv("papu.csv",index=False)

print(estudiantes)