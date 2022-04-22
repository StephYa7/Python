# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат


x=1
y=1
z=1

print(not(x and y and z) == (not x) or (not y) or (not z))