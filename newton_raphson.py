import numpy as np
import math
import cmath

# 1. Definindo uma matriz 6x6 (exemplo com valores aleatórios)


Zpu12 = 0.0020+0.0070j#0.0178+0.0626j #0.0059 + 0.0209j
Zpu23 = 0.01+0.06j
Zpu34 = 0.0220+0.0773j#0.1976+0.6960j #0.0659 + 0.2320j

Y = [
        [1/Zpu12, -1/Zpu12, 0, 0],
        [-1/Zpu12, 1/Zpu12, -1/Zpu23, 0],
        [0, -1/Zpu23, 1/Zpu23, -1/Zpu34],
        [0, 0, -1/Zpu34, 1/Zpu34]
]
Y11 = cmath.polar(Y[0][0])
Y12 = cmath.polar(Y[0][1])
Y13 = cmath.polar(Y[0][2])
Y14 = cmath.polar(Y[0][3])

Y21 = cmath.polar(Y[1][0])
Y22 = cmath.polar(Y[1][1])
Y23 = cmath.polar(Y[1][2])
Y24 = cmath.polar(Y[1][3])

Y31 = cmath.polar(Y[2][0])
Y32 = cmath.polar(Y[2][1])
Y33 = cmath.polar(Y[2][2])
Y34 = cmath.polar(Y[2][3])

Y41 = cmath.polar(Y[3][0])
Y42 = cmath.polar(Y[3][1])
Y43 = cmath.polar(Y[3][2])
Y44 = cmath.polar(Y[3][3])

print(f'Y11= {cmath.rect(Y11[0], Y11[1]):.3f}')#{Y11[0]:.3f}∠{math.degrees(Y11[1]):.3f}°')
print(f'Y12= {cmath.rect(Y12[0], Y12[1]):.3f}')#{Y12[0]:.3f}∠{math.degrees(Y12[1]):.3f}°')
print(f'Y13= {cmath.rect(Y13[0], Y13[1]):.3f}')#{Y13[0]:.3f}∠{math.degrees(Y13[1]):.3f}°')
print(f'Y14= {cmath.rect(Y14[0], Y14[1]):.3f}')#{Y14[0]:.3f}∠{math.degrees(Y14[1]):.3f}°')
print(f'Y21= {cmath.rect(Y21[0], Y21[1]):.3f}')#{Y21[0]:.3f}∠{math.degrees(Y21[1]):.3f}°')
print(f'Y22= {cmath.rect(Y22[0], Y22[1]):.3f}')#{Y22[0]:.3f}∠{math.degrees(Y22[1]):.3f}°')
print(f'Y23= {cmath.rect(Y23[0], Y23[1]):.3f}')#{Y23[0]:.3f}∠{math.degrees(Y23[1]):.3f}°')
print(f'Y24= {cmath.rect(Y24[0], Y24[1]):.3f}')#{Y24[0]:.3f}∠{math.degrees(Y24[1]):.3f}°')
print(f'Y31= {cmath.rect(Y31[0], Y31[1]):.3f}')#{Y31[0]:.3f}∠{math.degrees(Y31[1]):.3f}°')
print(f'Y32= {cmath.rect(Y32[0], Y32[1]):.3f}')#{Y32[0]:.3f}∠{math.degrees(Y32[1]):.3f}°')
print(f'Y33= {cmath.rect(Y33[0], Y33[1]):.3f}')#{Y33[0]:.3f}∠{math.degrees(Y33[1]):.3f}°')
print(f'Y34= {cmath.rect(Y34[0], Y34[1]):.3f}')#{Y34[0]:.3f}∠{math.degrees(Y34[1]):.3f}°')
print(f'Y41= {cmath.rect(Y41[0], Y41[1]):.3f}')#{Y41[0]:.3f}∠{math.degrees(Y41[1]):.3f}°')
print(f'Y42= {cmath.rect(Y42[0], Y42[1]):.3f}')#{Y42[0]:.3f}∠{math.degrees(Y42[1]):.3f}°')
print(f'Y43= {cmath.rect(Y43[0], Y43[1]):.3f}')#{Y43[0]:.3f}∠{math.degrees(Y43[1]):.3f}°')
print(f'Y44= {cmath.rect(Y44[0], Y44[1]):.3f}')#{Y44[0]:.3f}∠{math.degrees(Y44[1]):.3f}°')
V1 = cmath.polar(1 + 0j)
V2 = cmath.polar(1 + 0j)
V3 = cmath.polar(1 + 0j)
V4 = cmath.polar(1 + 0j)

rad = (math.pi / 180)

P2 = 0
P3 = 0
P4 = 0.3# 0,9000
Q2 = 0
Q3 = 0
Q4 = 0.1453 # 0,4359
count = 0
P2_old = P2
P3_old = P3
P4_old = P4
Q2_old = Q2
Q3_old = Q3
Q4_old = Q4
while True:
    P2_old = P2
    P3_old = P3
    P4_old = P4
    Q2_old = Q2
    Q3_old = Q3
    Q4_old = Q4
    V2_old = V2
    V3_old = V3
    V4_old = V4

    P2 = (
        abs(V1[0]*V2[0]*Y21[0])*math.cos(V1[1] - V2[1] + Y21[1]) +
        abs(V2[0]*V3[0]*Y23[0])*math.cos(V3[1] - V2[1] + Y23[1]) +
        abs(V2[0]*V4[0]*Y24[0])*math.cos(V4[1] - V2[1] + Y24[1]) +
        abs(V2[0]**2 * Y22[0])*math.cos(Y22[1])
    )

    P3 = (
        abs(V1[0]*V3[0]*Y31[0])*math.cos(V1[1] - V3[1] + Y31[1]) +
        abs(V2[0]*V3[0]*Y32[0])*math.cos(V2[1] - V3[1] + Y32[1]) +
        abs(V3[0]*V4[0]*Y34[0])*math.cos(V4[1] - V3[1] + Y34[1]) +
        abs(V3[0]**2 * Y33[0])*math.cos(Y33[1])
    )

    P4 = (
        abs(V1[0]*V4[0]*Y41[0])*math.cos(V1[1] - V4[1] + Y41[1]) +
        abs(V2[0]*V4[0]*Y42[0])*math.cos(V2[1] - V4[1] + Y42[1]) +
        abs(V3[0]*V4[0]*Y43[0])*math.cos(V3[1] - V4[1] + Y43[1]) +
        abs(V4[0]**2 * Y44[0])*math.cos(Y44[1])
    )

    # --- POTÊNCIAS REATIVAS ---
    Q2 = -(
        abs(V1[0]*V2[0]*Y21[0])*math.sin(V1[1] - V2[1] + Y21[1]) +
        abs(V2[0]*V3[0]*Y23[0])*math.sin(V3[1] - V2[1] + Y23[1]) +
        abs(V2[0]*V4[0]*Y24[0])*math.sin(V4[1] - V2[1] + Y24[1]) +
        abs(V2[0]**2 * Y22[0])*math.sin(Y22[1])
    )

    Q3 = -(
        abs(V1[0]*V3[0]*Y31[0])*math.sin(V1[1] - V3[1] + Y31[1]) +
        abs(V2[0]*V3[0]*Y32[0])*math.sin(V2[1] - V3[1] + Y32[1]) +
        abs(V3[0]*V4[0]*Y34[0])*math.sin(V4[1] - V3[1] + Y34[1]) +
        abs(V3[0]**2 * Y33[0])*math.sin(Y33[1])
    )

    Q4 = -(
        abs(V1[0]*V4[0]*Y41[0])*math.sin(V1[1] - V4[1] + Y41[1]) +
        abs(V2[0]*V4[0]*Y42[0])*math.sin(V2[1] - V4[1] + Y42[1]) +
        abs(V3[0]*V4[0]*Y43[0])*math.sin(V3[1] - V4[1] + Y43[1]) +
        abs(V4[0]**2 * Y44[0])*math.sin(Y44[1])
    )

    # --- DERIVADAS DE P2 ---
    dP2_ddelta2 = (
        V1[0]*V2[0]*Y21[0]*math.sin(V1[1] - V2[1] + Y21[1]) +
        V2[0]*V3[0]*Y23[0]*math.sin(V3[1] - V2[1] + Y23[1]) +
        V2[0]*V4[0]*Y24[0]*math.sin(V4[1] - V2[1] + Y24[1])
    )
    dP2_ddelta3 = -V2[0]*V3[0]*Y23[0]*math.sin(V3[1] - V2[1] + Y23[1])
    dP2_ddelta4 = -V2[0]*V4[0]*Y24[0]*math.sin(V4[1] - V2[1] + Y24[1])
    dP2_dV2 = (
        V1[0]*Y21[0]*math.cos(V1[1] - V2[1] + Y21[1]) +
        2*V2[0]*Y22[0]*math.cos(Y22[1]) +
        V3[0]*Y23[0]*math.cos(V3[1] - V2[1] + Y23[1]) +
        V4[0]*Y24[0]*math.cos(V4[1] - V2[1] + Y24[1])
    )
    dP2_dV3 = V2[0]*Y23[0]*math.cos(V3[1] - V2[1] + Y23[1])
    dP2_dV4 = V2[0]*Y24[0]*math.cos(V4[1] - V2[1] + Y24[1])

    # --- DERIVADAS DE Q2 ---
    dQ2_ddelta2 = (
        -V1[0]*V2[0]*Y21[0]*math.cos(V1[1] - V2[1] + Y21[1]) -
        V2[0]*V3[0]*Y23[0]*math.cos(V3[1] - V2[1] + Y23[1]) -
        V2[0]*V4[0]*Y24[0]*math.cos(V4[1] - V2[1] + Y24[1])
    )
    dQ2_ddelta3 = V2[0]*V3[0]*Y23[0]*math.cos(V3[1] - V2[1] + Y23[1])
    dQ2_ddelta4 = V2[0]*V4[0]*Y24[0]*math.cos(V4[1] - V2[1] + Y24[1])
    dQ2_dV2 = (
        V1[0]*Y21[0]*math.sin(V1[1] - V2[1] + Y21[1]) +
        2*V2[0]*Y22[0]*math.sin(Y22[1]) +
        V3[0]*Y23[0]*math.sin(V3[1] - V2[1] + Y23[1]) +
        V4[0]*Y24[0]*math.sin(V4[1] - V2[1] + Y24[1])
    )
    dQ2_dV3 = V2[0]*Y23[0]*math.sin(V3[1] - V2[1] + Y23[1])
    dQ2_dV4 = V2[0]*Y24[0]*math.sin(V4[1] - V2[1] + Y24[1])

    # --- DERIVADAS DE P3 ---
    dP3_ddelta2 = -V2[0]*V3[0]*Y32[0]*math.sin(V2[1] - V3[1] + Y32[1])
    dP3_ddelta3 = (
        V1[0]*V3[0]*Y31[0]*math.sin(V1[1] - V3[1] + Y31[1]) +
        V2[0]*V3[0]*Y32[0]*math.sin(V2[1] - V3[1] + Y32[1]) +
        V3[0]*V4[0]*Y34[0]*math.sin(V4[1] - V3[1] + Y34[1])
    )
    dP3_ddelta4 = -V3[0]*V4[0]*Y34[0]*math.sin(V4[1] - V3[1] + Y34[1])
    dP3_dV2 = V3[0]*Y32[0]*math.cos(V2[1] - V3[1] + Y32[1])
    dP3_dV3 = (
        V1[0]*Y31[0]*math.cos(V1[1] - V3[1] + Y31[1]) +
        V2[0]*Y32[0]*math.cos(V2[1] - V3[1] + Y32[1]) +
        2*V3[0]*Y33[0]*math.cos(Y33[1]) +
        V4[0]*Y34[0]*math.cos(V4[1] - V3[1] + Y34[1])
    )
    dP3_dV4 = V3[0]*Y34[0]*math.cos(V4[1] - V3[1] + Y34[1])

    # --- DERIVADAS DE Q3 ---
    dQ3_ddelta2 = V2[0]*V3[0]*Y32[0]*math.cos(V2[1] - V3[1] + Y32[1])
    dQ3_ddelta3 = (
        -V1[0]*V3[0]*Y31[0]*math.cos(V1[1] - V3[1] + Y31[1]) -
        V2[0]*V3[0]*Y32[0]*math.cos(V2[1] - V3[1] + Y32[1]) -
        V3[0]*V4[0]*Y34[0]*math.cos(V4[1] - V3[1] + Y34[1])
    )
    dQ3_ddelta4 = V3[0]*V4[0]*Y34[0]*math.cos(V4[1] - V3[1] + Y34[1])
    dQ3_dV2 = V3[0]*Y32[0]*math.sin(V2[1] - V3[1] + Y32[1])
    dQ3_dV3 = (
        V1[0]*Y31[0]*math.sin(V1[1] - V3[1] + Y31[1]) +
        V2[0]*Y32[0]*math.sin(V2[1] - V3[1] + Y32[1]) +
        2*V3[0]*Y33[0]*math.sin(Y33[1]) +
        V4[0]*Y34[0]*math.sin(V4[1] - V3[1] + Y34[1])
    )
    dQ3_dV4 = V3[0]*Y34[0]*math.sin(V4[1] - V3[1] + Y34[1])

    # --- DERIVADAS DE P4 ---
    dP4_ddelta2 = -V2[0]*V4[0]*Y42[0]*math.sin(V2[1] - V4[1] + Y42[1])
    dP4_ddelta3 = -V3[0]*V4[0]*Y43[0]*math.sin(V3[1] - V4[1] + Y43[1])
    dP4_ddelta4 = (
        V1[0]*V4[0]*Y41[0]*math.sin(V1[1] - V4[1] + Y41[1]) +
        V2[0]*V4[0]*Y42[0]*math.sin(V2[1] - V4[1] + Y42[1]) +
        V3[0]*V4[0]*Y43[0]*math.sin(V3[1] - V4[1] + Y43[1])
    )

    dP4_dV2 = V4[0]*Y42[0]*math.cos(V2[1] - V4[1] + Y42[1])
    dP4_dV3 = V4[0]*Y43[0]*math.cos(V3[1] - V4[1] + Y43[1])
    dP4_dV4 = (
        V1[0]*Y41[0]*math.cos(V1[1] - V4[1] + Y41[1]) +
        V2[0]*Y42[0]*math.cos(V2[1] - V4[1] + Y42[1]) +
        V3[0]*Y43[0]*math.cos(V3[1] - V4[1] + Y43[1]) +
        2*V4[0]*Y44[0]*math.cos(Y44[1])
    )

    # --- DERIVADAS DE Q4 ---
    dQ4_ddelta2 = V2[0]*V4[0]*Y42[0]*math.cos(V2[1] - V4[1] + Y42[1])
    dQ4_ddelta3 = V3[0]*V4[0]*Y43[0]*math.cos(V3[1] - V4[1] + Y43[1])
    dQ4_ddelta4 = (
        -V1[0]*V4[0]*Y41[0]*math.cos(V1[1] - V4[1] + Y41[1]) -
        V2[0]*V4[0]*Y42[0]*math.cos(V2[1] - V4[1] + Y42[1]) -
        V3[0]*V4[0]*Y43[0]*math.cos(V3[1] - V4[1] + Y43[1])
    )

    dQ4_dV2 = V4[0]*Y42[0]*math.sin(V2[1] - V4[1] + Y42[1])
    dQ4_dV3 = V4[0]*Y43[0]*math.sin(V3[1] - V4[1] + Y43[1])
    dQ4_dV4 = (
        V1[0]*Y41[0]*math.sin(V1[1] - V4[1] + Y41[1]) +
        V2[0]*Y42[0]*math.sin(V2[1] - V4[1] + Y42[1]) +
        V3[0]*Y43[0]*math.sin(V3[1] - V4[1] + Y43[1]) +
        2*V4[0]*Y44[0]*math.sin(Y44[1])
    )


    J = np.array([
        [dP2_ddelta2, dP2_ddelta3, dP2_ddelta4, -V2[0] * dP2_dV2, -V3[0] * dP2_dV3, -V4[0] * dP2_dV4],
        [dP3_ddelta2, dP3_ddelta3, dP3_ddelta4, -V2[0] * dP3_dV2, -V3[0] * dP3_dV3, -V4[0] * dP3_dV4],
        [dP4_ddelta2, dP4_ddelta3, dP4_ddelta4, -V2[0] * dP4_dV2, -V3[0] * dP4_dV3, -V4[0] * dP4_dV4],
        [dQ2_ddelta2, dQ2_ddelta3, dQ2_ddelta4, -V2[0] * dQ2_dV2, -V3[0] * dQ2_dV3, -V4[0] * dQ2_dV4],
        [dQ3_ddelta2, dQ3_ddelta3, dQ3_ddelta4, -V2[0] * dQ3_dV2, -V3[0] * dQ3_dV3, -V4[0] * dQ3_dV4],
        [dQ4_ddelta2, dQ4_ddelta3, dQ4_ddelta4, -V2[0] * dQ4_dV2, -V3[0] * dQ4_dV3, -V4[0] * dQ4_dV4],
    ])

    #P2 = 0
    #P3 = 0
    #Q2 = 0
    #Q3 = 0

    #print(J)
    dP2 = P2_old - P2
    dP3 = P3_old - P3
    dP4 = P4_old - P4
    dQ2 = Q2_old - Q2
    dQ3 = Q3_old - Q3
    dQ4 = Q4_old - Q4

    d = np.array([
        [dP2],
        [dP3],
        [dP4],
        [dQ2],
        [dQ3],
        [dQ4],
    ])

    J_inv = np.linalg.inv(J)

    result = J_inv @ d

    #print(result)
    V2 = (V2[0] + result[3][0], V2[1] + result[0][0])
    V3 = (V3[0] + result[4][0], V3[1] + result[1][0])
    V4 = (V4[0] + result[5][0], V4[1] + result[2][0])
    count += 1
    print(f"Iteração {count}")
    print(f"V2 = {V2[0]:.3f}∠{math.degrees(V2[1]):.3f}")
    print(f"V3 = {V3[0]:.3f}∠{math.degrees(V3[1]):.3f}")
    print(f"V4 = {V4[0]:.3f}∠{math.degrees(V4[1]):.3f}")
    error_mag = max(abs(V2[0] - V2_old[0]), abs(V3[0] - V3_old[0]), abs(V4[0] - V4_old[0]))
    error_pha = max(abs(V2[1] - V2_old[1]), abs(V3[1] - V3_old[1]), abs(V4[1] - V4_old[1]))
    #print(f"Erro max {error_mag}, error fase {error_pha}")
    print(f'Δp2={d[0][0]}')
    if count > 2:
        break