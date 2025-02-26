# The current exchange by the date of 14/02/2025 is: 
# 1 usd = 4121 Colombian pesos
# 1 usd = 3.72 Peruvian soles
# 1 usd = 5.74 Brazilian reais



P = int(input("What do you have left in pesos? ")) # 4121
S = float(input("What do you have left in soles? ")) # 3.72
R = float(input("What do you have left in reais? ")) # 5.74

P = P / 4121
S = S / 3.72
R = R / 5.74

total_dollars = P + S + R

print(total_dollars)