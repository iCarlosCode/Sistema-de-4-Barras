import math
import cmath 

class barra:
    def __init__(self, tipo, v=1+0j, p=0, q=0):
        self.tipo = tipo  # 'REF', 'PQ', 'PV'
        self.v = v
        self.p = p
        self.q = q

    def atualizar(self, k, Y, barras):
        if self.tipo == 'PQ':
            soma = 0
            for n in range(len(barras)):
                if n != k:
                    soma += Y[k][n] * barras[n].v
            termo = (self.p - self.q*1j) / self.v.conjugate()
            v_novo = (1 / Y[k][k]) * (termo - soma)
            erro = abs(abs(v_novo) - abs(self.v))
            self.v = v_novo
            return erro
        
        elif self.tipo == 'PV':
            # manter o módulo da tensão fixo (ex: 1.02)
            # atualiza apenas o Q para manter isso
            soma = 0
            for n in range(len(barras)):
                if n != k:
                    soma += Y[k][n] * barras[n].v
            corrente = soma + Y[k][k] * self.v
            s = self.v * corrente.conjugate()
            self.q = -s.imag  # apenas atualiza Q
            return 0
        
        elif self.tipo == 'REF':
            return 0


#Matrizes para resolver o problema de fluxo de potência de N barras
Y = [
    [14.1543 - 49.0041j, -14.1543 + 49.0041j, 0, 0],
    [-14.1543 + 49.0041j, 16.8210 - 65.0041j, -2.6667 + 16.0000j, 0],
    [0, -2.6667 + 16.0000j, 4.1851 - 21.0343j, -1.5184 + 5.0343j],
    [0, 0, -1.5184 + 5.0343j, 1.5184 - 5.0343j]
]

#matriz de admitâncias do sistema NxN

barras = [
    barra('REF', v=1+0j, p=0, q=0),                # Barra 1
    barra('PQ', p=0, q=0),                         # Barra 2
    barra('PQ', p=0, q=0),                         # Barra 3
    barra('PQ', p=-0.3, q=-0.1453)    # Barra 4
]
#LISTA de barra que específica a tensão e potência aparente líquida, do tipo: Barra('REF', v=1+0j),Barra('PQ', p=-0.5, q=-0.3099), Barra('PQ', p=-1.7, q=-1.0535), Barra('PV', v=1.02+0j, p=3.18)

#parâmetros para o método iterativo

erro_max = 0.001
erro = erro_max*1.01
it = 0

#loop

while erro >= erro_max:
    erro = 0
    it += 1
    print(f"Iteração {it}")

    for k in range(1, len(barras)):  #pula a barra 0 (referência)
        erro_k = barras[k].atualizar(k, Y, barras)
        erro = max(erro, erro_k)
        print(f"Barra {k+1}: |V| = {abs(barras[k].v):.6f}, ∠ = {math.degrees(cmath.phase(barras[k].v)):.2f}°")
        if barras[k].tipo == 'PV':
            print(f"  → Q calculado: {barras[k].q:.6f} pu")
        print(f"Erro na barra {k+1}: {erro_k:.6f}")

print(f"Convergência atingida em {it} iterações")