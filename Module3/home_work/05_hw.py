
# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
l=0
for name in names:
    if len(name)>l:
        l=len(name)
        name_max=name
print(name_max)
        
