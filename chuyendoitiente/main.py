import math
usd = float(input("Nhập số USD cần đổi: "))
tg = float(input("Nhập tỉ giá USD/VND: "))
vnd = tg*usd
print("Với {usd} USD sẽ đổi ra được {vnd} VND".format(usd=usd, vnd=vnd))