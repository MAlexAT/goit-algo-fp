# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм: максимізація співвідношення калорій до вартості
def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0
    
    for item, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            selected_items.append(item)
            total_cost += info["cost"]
            total_calories += info["calories"]
    
    return selected_items, total_cost, total_calories

# Динамічне програмування: максимізація калорійності при обмеженому бюджеті
def dynamic_programming(items, budget):
    # Ініціалізуємо таблицю dp розміром (бюджет + 1)
    dp = [0] * (budget + 1)
    item_selection = [[] for _ in range(budget + 1)]
    
    for item, info in items.items():
        cost = info["cost"]
        calories = info["calories"]
        # Проходимо бюджет у зворотному порядку, щоб уникнути повторного вибору страв
        for j in range(budget, cost - 1, -1):
            if dp[j - cost] + calories > dp[j]:
                dp[j] = dp[j - cost] + calories
                item_selection[j] = item_selection[j - cost] + [item]
    
    max_calories = dp[budget]
    selected_items = item_selection[budget]
    
    return selected_items, max_calories

# Приклад використання функцій
budget = 100

# Виконання жадібного алгоритму
greedy_items, greedy_cost, greedy_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", greedy_items)
print("Загальна вартість:", greedy_cost)
print("Загальна калорійність:", greedy_calories)

# Виконання алгоритму динамічного програмування
dp_items, dp_calories = dynamic_programming(items, budget)
print("\nДинамічне програмування:")
print("Вибрані страви:", dp_items)
print("Максимальна калорійність:", dp_calories)
