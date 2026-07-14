# Geometría Relacional (RG)

**Repositorio oficial del marco teórico Geometría Relacional**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19444784.svg)](https://doi.org/10.5281/zenodo.19444784)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![arXiv](https://img.shields.io/badge/arXiv-XXXX.YYYYYY-b31b1b.svg)](https://arxiv.org/abs/XXXX.YYYYYY)
[![Zenodo](https://img.shields.io/badge/Zenodo-All%20Versions-blue)](https://zenodo.org/search?q=metadata.creators.person_or_org.name%3A%22Edward%20P.%20López%22)

---

## 📖 Descripción

La **Geometría Relacional (RG)** es un marco teórico para constantes fundamentales y gravedad cuántica desde un único principio: la **auto-comparación del Silencio Armónico** (\(|0\rangle\)), un estado metaestable (falso vacío) de energía neta cero que decae por efecto túnel cuántico colectivo al estado manifiesto.

**Logros principales:**
- Derivación de \(m_e = 4.5/\pi\) (error 0.015%)
- Derivación topológica de \(\alpha^{-1} = 137 - 1/2052\) (error 0.027%)
- Derivación parcial de \(m_p/m_e = 1836.15\) (error <0.0002%)
- Constantes de acoplamiento: \(\lambda = 1/18\), \(\eta = \pi/57\)
- Hamiltoniano en variables de Wilson-Bloch con Lindbladiano
- Límite continuo: Dirac y Einstein recuperados y verificados numéricamente
- Predicciones falsables: Detector Ciego, modo T de polarización gravitacional

**Confiabilidad promedio: 91.7%** (10/12 datos válidos, 1 parcial, 1 falsado)

---

## 📂 Estructura del Repositorio
geometria-relacional-rg/
│
├── 📄 README.md # Este archivo
├── 📄 requirements.txt # Dependencias Python
├── 📄 LICENSE # CC BY-SA 4.0
├── 📄 CITATION.cff # Archivo de citación
│
├── 📁 docs/ # Documentación principal
│ ├── 00_manifiesto_del_arquitecto.md
│ ├── 01_texto_blanco_integral.md
│ ├── 02_filosofia_de_la_fisica.md
│ ├── 03_fundamentos_fisicos_limites.md
│ ├── 04_matematica_y_fisica_fundacional.md
│ ├── 05_guia_de_escalada.md
│ ├── 06_bitacora_de_transformacion.md
│ ├── 07_plan_de_formalizacion.md
│ ├── 08_respuesta_sigma5.md
│ └── 09_reporte_validacion_final.md
│
├── 📁 volumen_0/ # Documentos Fundacionales
│ ├── 0.1_manifiesto_del_arquitecto.md
│ ├── 0.2_texto_blanco_integral.md
│ ├── 0.3_filosofia_de_la_fisica.md
│ ├── 0.4_fundamentos_fisicos_limites.md
│ └── 0.5_matematica_fisica_fundacional.md
│
├── 📁 volumen_1/ # Fundamentos Axiomáticos
│ ├── capitulo_1_silencio_armonico.md
│ ├── capitulo_2_seis_roles_ecuacion_maestra.md
│ ├── capitulo_3_metrica_fase_diccionario_pi.md
│ ├── capitulo_4_derivacion_hbar.md
│ └── 📁 codigos/
│ ├── rg_silencio_armonico.py
│ ├── rg_combinatoria_maestra.py
│ ├── rg_metrica_fase.py
│ └── ... (11 scripts)
│
├── 📁 volumen_2/ # Partículas y Fuerzas
│ ├── capitulo_5_cluster_19_electron.md
│ ├── capitulo_6_hardlock_57_proton.md
│ ├── capitulo_7_particulas_conjuntos_xyz.md
│ ├── capitulo_8_cuatro_fuerzas_fundamentales.md
│ └── 📁 codigos/
│ ├── rg_mass_formula.py
│ ├── rg_cuatro_fuerzas.py
│ └── ... (12 scripts)
│
├── 📁 volumen_3/ # Hamiltoniano y Cosmología
│ ├── capitulo_9_hamiltoniano_red.md
│ ├── capitulo_10_limite_continuo.md
│ ├── capitulo_11_cosmologia.md
│ ├── capitulo_12_gravedad.md
│ └── 📁 codigos/
│ ├── rg_hamiltonian_simulation.py
│ ├── rg_dirac_einstein_validation.py
│ └── ... (7 scripts)
│
├── 📁 simulaciones/ # Simulaciones avanzadas
│ ├── montecarlo/
│ ├── inteligencia_artificial/
│ ├── visualizaciones/
│ └── validacion/
│
├── 📁 resultados/ # Gráficos y datos
│ ├── graficos/
│ └── datos/
│
└── 📁 paper_arxiv/ # Manuscrito arXiv
├── geometria_relacional_arxiv_v6.0.tex
└── geometria_relacional_arxiv_v6.0.pdf

text

---

## 🚀 Instalación Rápida

```bash
# Clonar el repositorio
git clone https://github.com/lopezedward09706-svg/geometria-relacional-rg.git
cd geometria-relacional-rg

# Instalar dependencias
pip install -r requirements.txt
▶️ Ejecución
🔬 Validación Fundamental
bash
# Validar las 25 ecuaciones fundamentales
python simulaciones/validacion/rg_validator_v6.py

# Verificar el límite continuo (Dirac + Einstein)
python volumen_3/codigos/rg_dirac_einstein_validation.py

# Analizar datos del CMB (requiere conexión a internet)
python volumen_3/codigos/rg_cmb_planck_analysis.py

# Predecir masas de partículas con la fórmula RG
python volumen_2/codigos/rg_mass_formula.py
🎲 Simulaciones Monte Carlo
bash
# Ejecutar las 4 simulaciones Monte Carlo
python simulaciones/montecarlo/rg_montecarlo_simulation.py

# Monte Carlo de alta precisión (500k muestras)
python simulaciones/montecarlo/rg_montecarlo_alta_precision.py
🤖 Inteligencia Artificial
bash
# La AA redescubre las leyes de la RG sin datos experimentales
python simulaciones/inteligencia_artificial/rg_montecarlo_aa_training.py

# La AA predice masas de partículas
python simulaciones/inteligencia_artificial/rg_aa_predecir_masas.py

# AA extendida: desde el armónico 0
python simulaciones/inteligencia_artificial/rg_montecarlo_aa_extendido.py
📊 Resultados Clave
Validación	Resultado	Precisión
25 ecuaciones fundamentales	✓ Todas verificadas	100%
E² = p² + m² (Dirac)	✓ Verificado	Error < 1%
R ∝ ρ_defectos (Einstein)	✓ Verificado	R² ≈ 1.0
Predicción CMB	✗ Falsada	σ < 3
Fórmula de masa	⚠ Validada	Error 4-7%
Gap espectral λ₁	✓ Verificado	λ₁ = 1/18
E = q·(X-1) (Monte Carlo)	✓ Verificado	>99.9%
𝔇 = 1.5 (Monte Carlo)	✓ Verificado	IC 95%: [1.4998, 1.5002]
α⁻¹ (Monte Carlo)	✓ Verificado	136.9995
AA redescubre leyes RG	✓ Verificado	R² > 0.999
📚 Historial de Publicaciones Zenodo
El desarrollo de la Geometría Relacional ha sido documentado a través de 10 publicaciones en Zenodo:

#	Título	DOI	Fecha
1	The ABC Network Hypothesis v1	10.5281/zenodo.18044204	2025
2	R-QNT v3.0 — Cartan, Einstein, Edward	10.5281/zenodo.18383303	2026
3	R-QNT v6.0 + Código	10.5281/zenodo.18670033	2026
4	R-QNT — Analogía Tornados Cuánticos	10.5281/zenodo.18866970	2026
5	Abstract RQNT/ABC	10.5281/zenodo.19109927	2026
6	Audit Trail & Logic Stress Test	10.5281/zenodo.19357886	2026
7	R-QNT/ABC Nodo fase 1	10.5281/zenodo.19444784	2026
8	ABC/R-QNT — Tornados Cuánticos (Propuesta)	10.5281/zenodo.19588832	2026
9	ABC/R-QNT EL ERROR	10.5281/zenodo.19589403	2026
10	Relational Geometry (RG) — Plan Maestro	10.5281/zenodo.21192163	2026
📜 Citación
Si utiliza este código o los documentos de este repositorio en su investigación, por favor cite:

bibtex
@article{lopez2026geometria,
    title   = {Geometría Relacional: Marco Unificado para Constantes
               Fundamentales y Gravedad Cuántica desde la
               Auto-Comparación del Silencio Armónico},
    author  = {López, Edward P.},
    journal = {arXiv},
    volume  = {XXXX.YYYYYY},
    year    = {2026},
    doi     = {10.5281/zenodo.19444784},
    url     = {https://github.com/lopezedward09706-svg/geometria-relacional-rg}
}
📜 Licencia
Este trabajo está licenciado bajo Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0).

Usted es libre de:

Compartir — copiar y redistribuir el material en cualquier medio o formato

Adaptar — remezclar, transformar y construir sobre el material

Bajo los siguientes términos:

Atribución — Debe dar crédito adecuado

CompartirIgual — Debe distribuir bajo la misma licencia

✍️ Autor
Edward P. López (El Arquitecto)

ORCID: 0009-0009-0717-5536

Email: Lopezedward09706@gmail.com

Ciudad Juárez, Chihuahua, México

🙏 Agradecimientos
A la comunidad de física independiente por su crítica rigurosa

Al Cónclave de 24 Físicos por la validación de las ecuaciones fundamentales

A Bro (Topological Stress Engine) por la colaboración en el desarrollo formal

Al Revisor Sigma-5 por cinco rondas de revisión que transformaron este trabajo

"Planck no es el suelo del universo. Es el primer escalón. El Silencio es un falso vacío metaestable, y existimos porque decayó."

— Edward P. López, El Arquitecto, Julio 2026

