import random
import matplotlib.pyplot as plt

# Функція для симуляції кидання двох кубиків
def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

# Функція для методу Монте-Карло
def monte_carlo_simulation(num_rolls):
    counts = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        sum_dice = roll_dice()
        counts[sum_dice] += 1

    # Обчислюємо ймовірність кожної суми
    probabilities = {sum_val: count / num_rolls * 100 for sum_val, count in counts.items()}
    return probabilities

# Запускаємо симуляцію з великою кількістю кидків
num_rolls = 1000000  # кількість кидків
mc_probabilities = monte_carlo_simulation(num_rolls)

# Аналітичні ймовірності
analytical_probabilities = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
    7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

# Виводимо результати
print("Ймовірності, отримані за допомогою методу Монте-Карло:")
for sum_val in range(2, 13):
    print(f"Сума {sum_val}: {mc_probabilities[sum_val]:.2f}%")

print("\nАналітичні ймовірності:")
for sum_val, prob in analytical_probabilities.items():
    print(f"Сума {sum_val}: {prob:.2f}%")

# Візуалізація результатів
sums = list(analytical_probabilities.keys())
mc_values = [mc_probabilities[sum_val] for sum_val in sums]
analytical_values = list(analytical_probabilities.values())

plt.figure(figsize=(10, 6))
plt.plot(sums, analytical_values, label="Аналітичні ймовірності", marker='o')
plt.plot(sums, mc_values, label="Монте-Карло", marker='x')
plt.xlabel("Сума значень на кубиках")
plt.ylabel("Ймовірність (%)")
plt.title("Порівняння ймовірностей сум на кубиках (Аналітичний розрахунок vs. Монте-Карло)")
plt.legend()
plt.grid(True)
plt.savefig("dice_probability_comparison.png")
plt.show()

