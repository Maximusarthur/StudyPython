def TriangleArea(*, a, b, c):
    if a+b > c and b+c > a and a+c > b:    # 判断三角形是否合法
        s = (a+b+c)/2                      # 计算半周长和面积
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        return area
    else:
        print("无法构成三角形")

area = TriangleArea(a = 8, b = 3, c = 6)
print("三角形面积:\n", area)