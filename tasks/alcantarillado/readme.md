
# 1. Estimación de Alcantarillas con el Coeficiente de Manning

Este script en Python estima el diámetro necesario de una alcantarilla para manejar el flujo de agua de lluvia, basado en registros históricos de precipitación mensual y el coeficiente de Manning.

---



### **Datos a utilizar**

Para obtener los registros históricos de precipitación mensual, utilizar el archivo CSV en `data/csv/precipitation.csv`.

### Coeficiente de escorrentía

| Material              | Coeficiente de escorrentía (C) |
| --------------------- | -------------------------- |
| Pavimento             | 0.6                      |
| Tierra                | 0.3                      |


Selección del material de la alcantarilla (mostrar una lista de opciones y validar que el usuario seleccione uno de ellos de la siguiente lista).

### Coeficiente de Manning


| Material              | Coeficiente de Manning (n) |
| --------------------- | -------------------------- |
| Concreto liso         | 0.012                      |
| Concreto rugoso       | 0.015                      |
| PVC                   | 0.009                      |
| Acero corrugado       | 0.024                      |
| Polietileno HDPE      | 0.012                      |
| Ladrillo              | 0.017                      |
| Hormigón armado       | 0.013                      |
| Canal de tierra       | 0.025                      |
| Canal de roca         | 0.035                      |
| Mampostería de piedra | 0.030                      |

---

### **Cálculos Requeridos**

#### **Cálculo del caudal (Q) usando el Método Racional:**

$$
Q = C \times I \times A
$$

Donde:

- \(Q\) = caudal (m³/s)
- \(C\) = coeficiente de escorrentía (0.6 para pavimento, 0.3 para tierra)
- \(I\) = intensidad de lluvia ( m/s)
- \(A\) = área de captación (m²) (factor de conversión: 1 ha = 10,000 m² )

La intensidad de lluvia \(I\) se calcula como:

$$
I = \frac{P}{T_c}
$$

Donde:

- \(P\) = precipitación diaria promedio (metros)
- \(T_c\) = tiempo de concentración (segundos)

#### **Cálculo del diámetro de la alcantarilla usando la ecuación de Manning:**

$$
Q = \frac{1}{n} A (R)^{2/3} p^{1/2}
$$

Donde:

- \(Q\) = caudal (m³/s)
- \(n\) = coeficiente de Manning
- \(p\) = Pendiente del terreno (m/m) (adimencional)
- \(R\) = Radio hidraulico de la alcantarilla (m)
- \(A\) = área equivalente (m²) = $(pi \times R^2)$

Donde el diámetro \(D\) para una alcantarilla circular se se obtiene de la ecuación:

$$
R = \frac{D}{4}
$$

Siendo \(D\) el diámetro de la alcantarilla y \(R\) el radio hidraulico .

