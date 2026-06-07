# ============================================================
# EJECUCIÓN DE PRUEBA
# ============================================================
if __name__ == "__main__":
    red = RedRG()

    print("=" * 60)
    print("GEOMETRÍA RELACIONAL (RG) — PRUEBA COMPLETA")
    print("=" * 60)

    # --- Paso 1: Ecuación Primordial ---
    print(f"\n1. Entero Primordial: {red.ecuacion_primordial()}")

    # --- Paso 2: Roles ---
    print(f"\n2. Roles primarios: A={red.A}, B={red.B}, a={red.a}, b={red.b}, c={red.c}, C={red.C}")

    # --- Paso 3: Ecuación Maestra ---
    izq, der, ok = red.ec_maestra_suma()
    print(f"\n3. Ecuación Maestra: {izq} = {der} → {'✅' if ok else '❌'}")

    # --- Paso 4: Deuda ---
    print(f"\n4. Deuda de Información 𝔇 = {red.Deuda}")

    # --- Paso 5: Electrón ---
    m_ur, m_MeV = red.masa_electron()
    print(f"\n5. Masa del electrón: {m_ur:.4f} u.r. = {m_MeV:.3f} MeV/c²")
    print(f"   Espín (prueba angular): demanda {red.spin_electron()[0]}° - oferta {red.spin_electron()[1]}° = {red.spin_electron()[2]}° → ħ/2")

    # --- Paso 6: Constantes ---
    print(f"\n6. Acoplamiento fino λ = 1/18 = {red.lambda_acop:.4f}")
    print(f"   Fricción topológica η = π/57 = {red.eta:.4f}")
    print(f"   α⁻¹ (RG) = {red.alpha_inv():.4f} (exp. 137.036, error {abs(red.alpha_inv()-137.036)/137.036*100:.3f}%)")

    # --- Paso 7: Métrica de Fase ---
    print(f"\n7. Métrica de Fase:")
    print(f"   D(1,2) = {red.metrica_fase(1,2):.4f}  (√2 = {np.sqrt(2):.4f})")
    print(f"   D(1/2,1) = {red.metrica_fase(0.5,1):.4f}  (2^(1/4) = {2**0.25:.4f})")
    print(f"   D(1/2,√2) = {red.metrica_fase(0.5,np.sqrt(2)):.4f}  (φ = {(1+np.sqrt(5))/2:.4f})")

    # --- Paso 8: Fábrica de partículas ---
    print(f"\n8. Fábrica de Partículas (Ecuación Maestra Extendida):")
    masa_e_ur, masa_e_MeV = red.masa_particula(X=1.0, Y=0.5, Z=1/18)
    print(f"   Electrón (c=1, a=0.5, λ=1/18): {masa_e_MeV:.3f} MeV/c²")
    # Otros ejemplos
    masa_mu_ur, masa_mu_MeV = red.masa_particula(X=2.0, Y=0.5, Z=1/18)
    print(f"   Muón (X=2, Y=0.5, Z=1/18): {masa_mu_MeV:.1f} MeV/c² (exp. 105.66)")
    masa_tau_ur, masa_tau_MeV = red.masa_particula(X=3.0, Y=0.5, Z=1/18)
    print(f"   Tau (X=3, Y=0.5, Z=1/18): {masa_tau_MeV:.1f} MeV/c² (exp. 1776.8)")

    # --- Paso 9: Cosmología ---
    cosm = red.cosmologia()
    print(f"\n9. Cosmología:")
    print(f"   H₀ = {cosm['H0 (km/s/Mpc)']} km/s/Mpc")
    print(f"   w_vac ≈ {cosm['w_vac']}")
    print(f"   w_infl = {cosm['w_infl']:.3f} (debe ser < -1/3)")

    # --- Paso 10: Cargas de quarks ---
    print(f"\n10. Cargas de quarks (energía fractal):")
    print(f"    Quark down: 3/9 = 1/3")
    print(f"    Quark up: 6/9 = 2/3")

    print("\n" + "=" * 60)
    print("PRUEBA COMPLETA FINALIZADA. PUEDE MODIFICAR LOS PARÁMETROS.")
    print("=" * 60)
```