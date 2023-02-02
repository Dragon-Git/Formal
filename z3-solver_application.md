# z3求解器应用

## 求解代数方程

可以求解代数方程：  

相应代码为：
```python
from z3 import *

x, y, z = Reals('x y z')
s = Solver()
s.add(3*x + 2*y - z == 1)
s.add(2*x - 2*y + 4*z == -2)
s.add(-x + 0.5*y - z == 0)
print(s.check())
print(s.model())
```
计算结果为：
```bash
sat
[y = -2, x = 1, z = -2]
```
**注意**：该求解器可以求解多项式方程组，但不能求解指数方程
## 最优化问题

一个工厂有很多13米×6米的原料钢板，客户同时需要800片5米×4米的钢板X和400片3米×2米的钢板Y，如何切割才能使使用的原料钢板最少？

将一块原料钢板切成目标钢板的方式有4种，分别为：
- A:3×X 和 1×Y
- B:2×X 和 2×Y
- C:1×X 和 9×Y
- D:0×x 和 13×Y

则有
$$\left \{
    \begin{array}{lcr}
        3*A+2*B+C=800 \\
        A+2*B+9*C+13*D=400 \\
        A,B,C,D>=0 
    \end{array}
\right.
$$

目标函数为
$$Y=min(A+B+C+D)$$
相应代码为：
```python
from z3 import *
s=Optimize()
workpieces_total=Int('workpieces_total')
cut_A , cut_B , cut_C , cut_D=Ints('cut_A cut_B cut_C cut_D')
out_A , out_B=Ints('out_A out_B')
s.add(workpieces_total==cut_A+cut_B+cut_C+cut_D)
s.add(cut_A >=0)
s.add(cut_B >=0)
s.add(cut_C >=0)
s.add(cut_D >=0)
s.add(out_A==cut_A*3 + cut_B*2 + cut_C*1)
s.add(out_B==cut_A*1 + cut_B*6 + cut_C*9 + cut_D*13)
s.add(out_A==800)
s.add(out_B==400)
s.minimize(workpieces_total)
print(s.check())
print(s.model())
```
计算结果为：
```bash
sat
[cut_B = 25,
cut_D = 0,
cut_A = 250,
out_B = 400,
out_A = 800,
workpieces_total = 275,
cut_C = 0]
```
## 子集和
在计算机科学中，在复杂理论和密码学中子集和是一个重要问题，该问题问为：给定一个整数集合，是否有非空子集的和为0 。

## 模的逆元

## 求解数独
```python
#!/usr/bin/env python3
from z3 import (Solver, Int, Distinct)

def sudoku_solver(puzzle:str):
    s=Solver()
    # using Python list comprehension , construct array of arrays of Int instances:
    cells=[[Int('cell%d%d' % (r, c)) for c in range(9)] for r in range(9)]
    for r in range(9):
        for c in range(9):
            # process text line:
            if puzzle[r*9+c] != '.':
                s.add(cells[r][c]==int(puzzle[r*9+c]))
            # 0< =cell value <=9
            s.add(cells[r][c]>=1, cells[r][c]<=9)
    # for all 9 rows
    s.add(*[Distinct(*r) for r in cells])
    # for all 9 columns
    s.add(*[Distinct(*c) for c in zip(*cells)])
    # enumerate all 9 squares
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
        # add constraints for each 3*3 square:
            s.add(Distinct(*[cells[r+rr][c+cc] for rr in range(3) for cc in range(3)]))

    if s.check().__repr__() == "sat":
        m=s.model()
        for r in range(9):
            print([m[cells[r][c]] for c in range(9)])
    else:
        print(s.check())

# http://www.norvig.com/sudoku.html
# http://www.mirror.co.uk/news/weird-news/worlds-hardest-sudoku-can-you-242294
puzzle0="..53.....8......2..7..1.5..4....53...1..7...6..32...8..6.5....9..4....3......97.."
puzzle1=".....6....59.....82....8....45........3........6..3.54...325..6.................."
puzzle2=".....5.8....6.1.43..........1.5........1.6...3.......553.....61........4........."
sudoku_solver(puzzle0)
sudoku_solver(puzzle1)
sudoku_solver(puzzle2)

```
## 解魔方
![三阶魔方](https://bkimg.cdn.bcebos.com/pic/b2de9c82d158ccbf6c81ac8b7d92ab3eb13533faeb62?x-bce-process=image/resize,m_lfit,w_536,limit_1)

---
**Solving Rubik’s cube is not a problem, finding shortest solution is**

--- 

假设魔方有6种颜色: white, green, blue, orange, red, yellow. 
将魔方的6个面记为:front, up, down, left, right, back.

## 求解二阶积分的逆
**问题** 二阶积分的表达式为:
$$y=\sum\limits^n_{i=0} i*x_i$$
下面求解二阶64次积分的逆
```python
from z3 import (Solver,Int,Sum)

t = [Int("t_%d" % i) for i in range(64)]
d = [(t.index(i)+1)*i for i in t]

s = Solver()
for i in t:
    s.add(i>=0, i<=15)

s.add(Sum(*d)==23231)
c = s.check()
m = s.model()
print(c, m)
```
可以得到：
```bash
sat [t_1 = 0,
 t_45 = 0,
 t_44 = 15,
 t_51 = 15,
 t_5 = 0,
 t_22 = 15,
 t_19 = 15,
 t_48 = 15,
 t_56 = 15,
 t_21 = 0,
 t_10 = 0,
 t_37 = 0,
 t_57 = 15,
 t_58 = 15,
 t_30 = 4,
 t_40 = 15,
 t_62 = 15,
 t_13 = 0,
 t_31 = 0,
 t_60 = 15,
 t_27 = 15,
 t_34 = 15,
 t_6 = 15,
 t_7 = 0,
 t_63 = 15,
 t_46 = 15,
 t_41 = 15,
 t_2 = 15,
 t_20 = 0,
 t_43 = 15,
 t_11 = 15,
 t_4 = 0,
 t_29 = 0,
 t_61 = 15,
 t_47 = 0,
 t_23 = 15,
 t_9 = 0,
 t_14 = 15,
 t_17 = 0,
 t_18 = 0,
 t_35 = 15,
 t_28 = 0,
 t_8 = 0,
 t_33 = 15,
 t_42 = 15,
 t_52 = 15,
 t_53 = 15,
 t_50 = 15,
 t_49 = 15,
 t_32 = 0,
 t_54 = 15,
 t_36 = 15,
 t_55 = 15,
 t_59 = 15,
 t_24 = 0,
 t_39 = 15,
 t_15 = 0,
 t_16 = 15,
 t_26 = 0,
 t_38 = 0,
 t_25 = 15,
 t_12 = 15,
 t_3 = 15,
 t_0 = 7]
```
## 求解扫雷

## 破解LGC（随机数算法）
