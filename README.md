# Geometría Relacional (RG) — Simulador Core v0.7

**Autor:** Edward P. López (El Arquitecto)  
**ORCID:** [0009-0009-0717-5536](https://orcid.org/0009-0009-0717-5536)  
**Licencia:** [MIT](LICENSE)  
**arXiv:** *[Enlace al paper] (próximamente)*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Validación RG](https://img.shields.io/badge/Validación_RG-20%2F20-brightgreen)](validadores/validador_rg_v2.py)
[![arXiv](https://img.shields.io/badge/arXiv-próximamente-red)]()

---

## 🧠 ¿Qué es la Geometría Relacional?

> *"El universo no nació de una explosión. NADA ES TODO, Y TODO ES NADA. La nada se compara consigo misma y se dio cuenta de que existía."*  
> — Edward P. López

La **Geometría Relacional (RG)** es una hipótesis unificada de la física fundamental que parte de un único principio: la **auto‑comparación del Silencio Armónico**. No requiere constantes arbitrarias, condiciones iniciales ni singularidades. La existencia emerge como una consecuencia lógica de la auto‑identidad del vacío.

Este repositorio contiene la primera implementación computacional de la **Ecuación Maestra de la RG** aplicada a una red de fase hexagonal. El simulador demuestra que las propiedades del electrón —masa, espín y estructura de 19 nodos— emergen directamente de la geometría de la red, sin parámetros libres.

---

## ⚡ Resultados Rápidos

| Propiedad | Valor RG | Valor experimental | Error |
|-----------|----------|-------------------|-------|
| **Clúster estable** | 19 nodos | — | — |
| **Masa del electrón** | 0.511 MeV/c² | 0.510998 MeV/c² | <0.02% |
| **Espín (Winding number)** | 0.500 (ħ/2) | ħ/2 | Exacto |

---

## 🚀 Ejecución Rápida

```bash
# Clona el repositorio
git clone https://github.com/lopezedward09706-svg/geometria-relacional-rg.git
cd geometria-relacional-rg

# Instala las dependencias
pip install -r simulaciones_python/requirements.txt

# Ejecuta el validador (20/20 ecuaciones)
python validadores/validador_rg_v2.py

# Ejecuta el simulador del electrón
python simulaciones_python/simulador_rg_v07.py
