x = [1, 2, 3]
y = [5, 1, 3]

#y = x
m1 = 1
b1 = 0

# y = 0.5x + 1
m2 = 0.5
b2 = 1

y_predicted1 = [i*m1 + b1 for i in x]

y_predicted2 = [i*m2 + b2 for i in x]

total_loss1 = 0

for i in range(len(y)):
    num = y[i] - y_predicted1[i]
    total_loss1 += num**2


total_loss2 = 0
for i in range(len(y)):
    num = y[i] - y_predicted2[i]
    total_loss2 += num**2

print(total_loss1)
print(total_loss2)

better_fit = 0
if(total_loss1 < total_loss2):
    better_fit = total_loss1
else:
    better_fit = total_loss2
