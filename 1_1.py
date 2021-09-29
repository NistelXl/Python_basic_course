# Задание 1

duration = 400153

day = (duration) // (24 * 3600)
hour = (duration - 24 * day * 3600) // 3600
min = (duration - 24 * day * 3600 - 3600 * hour) // 60
sec = duration % 60

print(day,"дн",hour,"час",min,"мин",sec,"сек")


# Вариант с циклом для нескольких значений

duration = [53,153,4153,400153]
for n in duration:
    day = n // (24 * 3600)
    hour = (n - 24 * day * 3600) // 3600
    min = (n - 24 * day * 3600 - 3600 * hour) // 60
    sec = n % 60
    print(day, "дн", hour, "час", min, "мин", sec, "сек")

