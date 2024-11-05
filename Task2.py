import turtle
import math

def draw_tree(t, branch_length, angle, level):
    if level == 0:
        return

    # Малюємо стовбур дерева
    t.forward(branch_length)

    # Переходимо до лівої гілки
    t.left(angle)
    draw_tree(t, branch_length * 0.7, angle, level - 1)
    
    # Повертаємося до стовбура та малюємо праву гілку
    t.right(2 * angle)
    draw_tree(t, branch_length * 0.7, angle, level - 1)
    
    # Повертаємося назад до стовбура
    t.left(angle)
    t.backward(branch_length)

# Основна функція для налаштування дерева
def pythagoras_tree(level):
    screen = turtle.Screen()
    screen.title("Дерево Піфагора")
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)  # Повертаємо черепашку вгору
    t.color("brown")

    # Параметри дерева
    branch_length = 100
    angle = 30

    draw_tree(t, branch_length, angle, level)
    screen.mainloop()

# Вводимо рівень рекурсії від користувача
try:
    level = int(input("Введіть рівень рекурсії для дерева Піфагора: "))
    if level > 0:
        pythagoras_tree(level)
    else:
        print("Рівень рекурсії повинен бути більше 0")
except ValueError:
    print("Будь ласка, введіть ціле число.")
