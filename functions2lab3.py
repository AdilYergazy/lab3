# 1
def rate(movie):
    if movie['imdb'] > 5.5:
        return True
for i in movies:
    print(rate(i))

# 2
def rate2(movies):
    mov = []
    for i in movies:
        if i['imdb'] > 5.5:
            mov.append(i['name'])
    return mov
# 3
def rat3(category):
    mov = []
    for i in movies:
        if i['category'] == category:
            mov.append(i['name'])
    return mov
# 4
def rate4(movies):
    sum1 = 0
    avg = 0
    count = 0
    for i in movies:
        count += 1
        sum1 += i['imdb']
    return sum1 / count
# 5
def rat3(category):
    mov = []
    sum1 = 0
    count = 0
    for i in movies:
        if i['category'] == category:
            sum1 += i['imdb']
            count += 1
    return sum1 / count
