
num_aproximacoes = 15

pi_aproximado = 3.0

for i in range(2, 2 + num_aproximacoes * 2, 2):
    pi_aproximado += 4.0 / (i * (i + 1) * (i + 2))
    print(f"Aproximação: {pi_aproximado:.10f}")
