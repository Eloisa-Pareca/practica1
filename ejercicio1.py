import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#----4----
#x = np.ones( 4 ) 
#print(x.ndim) 
#print(x.shape) 
#print(x.size)
#print(x.dtype)
#------- pandas-------
#personas = { 
#"peso": pd.Series([68, 83, 112], index = ["maria", "mario", "memo"]),
# "cumpleanhos": pd.Series([1994, 1995, 2002], index = ["mario", "maria", "memo"], name = "anho"),
# "hijos": pd.Series([0, 3], index = ["memo", "mario"]),
# "actividades": pd.Series(["Biking", "Dancing"], index = ["maria", "mario"]),
#}

#print(personas)
#persona = pd.DataFrame(personas)
#persona[persona["cumpleanhos"] < 2000]
#print(persona)
#-------matplotlib-------
x = np.arange(-10,10,0.1)
y = x**2
plt.plot(x,y)
plt.show() 