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
rf_interestRate = 1 + float(.05)


c_price_u = s_u - e
c_price_d = s_d - e
if(c_price_d < 0):
    c_price_d = 0

hedge_ratio = (c_price_u - c_price_d) / (s_u - s_d)

#resize proportion
def hedge_ratio_proportion(ratio):
    multiplier = 1 / ratio
    return multiplier

prop_value = hedge_ratio_proportion(hedge_ratio)

v_u = s_u -  prop_value * c_price_u
v_d = s_d - prop_value * c_price_d

if v_u!=v_d:
    print "Arbitrage Exist!"

#work on this a bit more
# c = (v_u - s_price) / (rf_interestRate) * -1


print v_u - s_price





# print c
