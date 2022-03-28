def get_gradient_at_b(x, y, m, b):
    diff = 0
    N = len(x)
    for i in range(N):
        y_val = y[i]
        x_val = x[i]
        diff += (y_val - ((m * x_val) + b))
    b_gradient = -2/N * diff
    return b_gradient


def get_gradient_at_m(x, y, m, b):
    diff = 0
    N = len(x)
    for i in range(N):
        num = x[i]*(y[i] - (m*x[i]+b))
        diff += num
    m_gradient = -2/N * diff
    return m_gradient
