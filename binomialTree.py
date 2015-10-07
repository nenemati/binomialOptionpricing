import math

# print "Input Stock Price"
# s_price = int(raw_input())
# print "Input Stock Price Up"
# s_u = int(raw_input())
# print "Input Stock Price Down"
# s_d = int(raw_input())
# print "Input Strike Price"
# e = int(raw_input())
s_price = float(30)
s_u = float(35)
s_d = float(25)
e = float(30)
rf_interestRate = float(.05)

c_price_u = s_u - e
c_price_d = s_d - e
if(c_price_d <0):
    c_price_d = 0

hedge_ratio = (c_price_u - c_price_d) / (s_u - s_d)

#resize proportion
def hedge_ratio_proportion(ratio):
    multiplier = 1 / ratio
    return multiplier

V_u = s_u - hedge_ratio_proportion(hedge_ratio) * c_price_u

print V_u
