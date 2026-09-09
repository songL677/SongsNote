import numpy as np
import matplotlib.pyplot as plt

# =========================
# 1. 定义原函数 f(x)
# =========================
def f(x):
    return x**2

# 选择两个端点
a = 1
c = 3

# =========================
# 2. 计算割线斜率
# =========================
k = (f(c) - f(a)) / (c - a)

# 割线
def L(x):
    return f(a) + k * (x - a)

# 构造 g(x)
def g(x):
    return f(x) - k * (x - a)

# =========================
# 3. 输出关键数值
# =========================
print("f(a) =", f(a))
print("f(c) =", f(c))
print("割线斜率 k =", k)

print("g(a) =", g(a))
print("g(c) =", g(c))

# =========================
# 4. 准备绘图
# =========================
x = np.linspace(0, 4, 400)

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# -------------------------
# 左图：原函数 + 割线
# -------------------------
ax[0].plot(x, f(x), label="f(x)")
ax[0].plot(x, L(x), "--", label="Secant line L(x)")

ax[0].scatter([a, c], [f(a), f(c)], s=60)

ax[0].annotate(
    f"A=({a},{f(a)})",
    (a, f(a)),
    xytext=(a-0.7, f(a)+1)
)

ax[0].annotate(
    f"C=({c},{f(c)})",
    (c, f(c)),
    xytext=(c-0.3, f(c)+1)
)

ax[0].set_title("Original function f(x)")
ax[0].axhline(0, linewidth=0.8)
ax[0].axvline(0, linewidth=0.8)
ax[0].grid(alpha=0.3)
ax[0].legend()

# -------------------------
# 右图：变换后的 g
# -------------------------
ax[1].plot(x, g(x), label="g(x)")

# 水平线 y = f(a)
ax[1].axhline(
    f(a),
    linestyle="--",
    label="y = f(a)"
)

ax[1].scatter(
    [a, c],
    [g(a), g(c)],
    s=60
)

ax[1].annotate(
    f"g(a)={g(a):.1f}",
    (a, g(a)),
    xytext=(a-0.7, g(a)+1)
)

ax[1].annotate(
    f"g(c)={g(c):.1f}",
    (c, g(c)),
    xytext=(c-0.3, g(c)+1)
)

ax[1].set_title("Transformed function g(x)")
ax[1].axhline(0, linewidth=0.8)
ax[1].axvline(0, linewidth=0.8)
ax[1].grid(alpha=0.3)
ax[1].legend()

plt.tight_layout()
plt.show()