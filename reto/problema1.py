# Cálculo del despegue de un F-16 en José María Córdova

# ---- Datos iniciales ----
masa = 10200            # kg (F-16 limpio con medio combustible)
g = 9.81                # m/s^2
W = masa * g            # Peso en Newton
S = 28                  # m^2 (área alar)
CL_max = 1.8            # coeficiente de sustentación en despegue
rho = 0.992             # kg/m^3 (densidad aire a 2142 m)

# ---- Velocidad mínima de despegue ----
V_despegue = ((2 * W) / (rho * S * CL_max)) ** 0.5  # m/s

# ---- Suposición de aceleración ----
a = 6.3   # m/s^2 (aceleración constante con postcombustión)

# ---- Tiempo para alcanzar la velocidad ----
tiempo = V_despegue / a   # s

# ---- Distancia recorrida hasta el despegue ----
distancia = 0.5 * a * (tiempo ** 2)   # m

# ---- Resultados ----
print("Velocidad de despegue necesaria: ", round(V_despegue, 1), "m/s")
print("Tiempo para despegar: ", round(tiempo, 1), "segundos")
print("Distancia recorrida: ", round(distancia, 1), "metros")

