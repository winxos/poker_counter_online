from datetime import datetime, timedelta
from random import randint

now = datetime.now()
print(now.strftime("%y/%m/%d %H:%M:%S"))
time_data = []
for i in range(100):
    time_data.append((now + timedelta(seconds=i * 100)).strftime("%Y/%m/%d %H:%M:%S"))


# print(time_data)


class Round:
    @staticmethod
    def play():
        dz = randint(0, 2)
        bombs = randint(0, 6)
        win = randint(0, 1)
        dz_score = 2 * 2 ** bombs * (win * 2 - 1)
        scores = [-dz_score // 2, -dz_score // 2, -dz_score // 2]
        scores[dz] = dz_score
        return scores


zx = [0]
ry = [0]
wv = [0]
for i in range(100):
    a, b, c = Round.play()
    zx.append(a + zx[i])
    ry.append(b + ry[i])
    wv.append(c + wv[i])
print(zx)
print(ry)
print(wv)
