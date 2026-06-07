# Roadmap v0.8 — Ruptura Espontánea de Simetría

**Estado actual:** En desarrollo  
**Objetivo:** Eliminar los nodos congelados y lograr que el semi‑vórtice de espín ½ emerja de forma espontánea en una red completamente libre.

## Motivación
La versión 0.7 demostró que la red RG puede albergar un defecto topológico de espín ½ cuando se impone una condición de semi‑vórtice. Sin embargo, el universo no tiene un programador externo que congele fases. Para que la RG sea una teoría dinámica completa, el espín debe emerger de la propia geometría de la red.

## Mecanismo propuesto
Se introducirá un **término de error quiral** en la Ecuación Maestra, inspirado en la fricción del vacío `η = π/57`. Este término actuará como un pseudo‑vector de área orientada (Ω_ijk) que rompe la simetría entre giro horario y antihorario.

### Forma matemática tentativa
Error_total = (A+B+C) - 2(a+b+c) + η * Σ Ω_ijk

text
donde Ω_ijk es el área orientada del triángulo en el espacio de fases.

## Entregables previstos
- Script `rg_v08_quiral_alpha.py` funcional.
- Validación del *winding number* 0.5 sin nodos congelados.
- Comparación de masa y espín con los valores de la v0.7 (deben coincidir asintóticamente).

## Cómo contribuir
Si eres físico, matemático o entusiasta de la simulación computacional, puedes revisar el código de la v0.8 alpha en `simulaciones_python/` y proponer mejoras mediante *pull requests* o abriendo un *issue*.