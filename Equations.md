# Equations

#### The initial positions

$$
\begin{equation}
f_1(id, n, d) = -\frac{(n-1) \times d}{2} + d \times (id-1)
\end{equation}
$$

#### Go to any position in straight path

$$
f_2(x_1,y_1,x_2,y_2,v, t) = \begin{cases}
x_1 + \frac{v \times (x_2-x_1)}{\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}} \times t &{(\left|  \frac{v \times (x_2-x_1)}{\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}} \times t \right| < \left|x_2 - x_1\right|)},\\
x_2 &{(\left|  \frac{v \times (x_2-x_1)}{\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}} \times t \right| \geq \left|x_2 - x_1\right|)}\\
\end{cases}
$$

$$
f_3(x_1,y_1,x_2,y_2,v, t) = \begin{cases}
y_1 + \frac{v \times (y_2-y_1)}{\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}} \times t &{(\left|  \frac{v \times (y_2-y_1)}{\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}} \times t \right| < \left|y_2 - y_1\right|)},\\
y_2 &{(\left|  \frac{v \times (y_2-y_1)}{\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}} \times t \right| \geq \left|y_2 - y_1\right|)}\\
\end{cases}
$$

#### Wait then go to a position

$$
f_4(x_1,y_1,x_2,y_2, v,t,w) = \begin{cases}
x_1 &(t<w),\\
f_2(x_1,y_1,x_2,y_2,v,(t-w)) &(t \geq w)
\end{cases}
$$

$$
f_5(x_1,y_1,x_2,y_2, v,t,w) = \begin{cases}
y_1 &(t<w),\\
f_3(x_1,y_1,x_2,y_2,v,(t-w)) &(t \geq w)
\end{cases}
$$



#### The position each drone should be of the Ferris Wheel

$$
x_{id, n, x,r,v, t} = x - r \times cos(\frac{id}{n} \times 2 \pi + \frac{v}{r} \times t)
$$

$$
y_{id, n, y,r,v,t} = y - r \times sin(\frac{id}{n} \times 2 \pi + \frac{v}{r} \times t)
$$

#### Process

asjdlkfa

