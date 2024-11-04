import numpy as np

profits = np.array([
    [200, 300, 150],
    [750, 200, 350],
    [250, 80, 350],
    [800, 500, 450]
])

P = np.array([0.1, 0.5, 0.4])

V = np.array([2, 1])

expected_losses = []
for i in range(profits.shape[0]):
    expected_loss = np.dot(P, profits[i])
    expected_losses.append(expected_loss)
expected_losses = np.array(expected_losses)

variances = []
for i in range(profits.shape[0]):
    mean_profit = np.dot(P, profits[i])
    variance = np.dot(P, (profits[i] - mean_profit) ** 2)
    variances.append(variance)
variances = np.array(variances)

compromise_scores = V[0] * expected_losses + V[1] * variances

optimal_index = np.argmin(compromise_scores)

print("Очікувані збитки для кожного рішення:", expected_losses)
print("Дисперсія для кожного рішення:", variances)
print("Компромісні оцінки для кожного рішення:", compromise_scores)
print("Оптимальне рішення за компромісним критерієм:")
print("  Номер рішення:", optimal_index + 1)
print("  Очікувані збитки:", expected_losses[optimal_index])
print("  Дисперсія:", variances[optimal_index])
