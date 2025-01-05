def solution(ineq, eq, n, m):
    sign = ineq + eq
    if (sign == ">="):
        return int(n >= m)
    elif (sign == "<="):
        return int(n <= m)
    elif (sign == ">!"):
        return int(n > m)
    else:
        return int(n < m)