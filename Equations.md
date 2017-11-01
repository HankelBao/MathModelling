# Equations

#### The initial positions

$$
\begin{equation}
f(id, x, n, d) = x-\frac{(n-1) \times d}{2} + d \times (id-1)
\end{equation}
$$

We call $f(id,n,d)$ as $f_{InitialPos}$ 

id is the id of each drone

x is the initial x position

n is number of drones

d is the distance between drones

#### The waiting time

$$
\begin{equation}
f(id, t) = id \times (t-1)
\end{equation}
$$

We call $f(id, t)$ as $f_{WaitTime}$

id is the id of each drone

t is the input time

#### Go to any position in straight path

$$
f_1(x_1,y_1,x_2,y_2,v, t) = \begin{cases}
x_1 + \frac{v \times (x_2-x_1)}{\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}} \times t &{(\left|  \frac{v \times (x_2-x_1)}{\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}} \times t \right| < \left|x_2 - x_1\right|)},\\
x_2 &{(\left|  \frac{v \times (x_2-x_1)}{\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}} \times t \right| \geq \left|x_2 - x_1\right|)}\\
\end{cases}
$$

$$
f_2(x_1,y_1,x_2,y_2,v, t) = \begin{cases}
y_1 + \frac{v \times (y_2-y_1)}{\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}} \times t &{(\left|  \frac{v \times (y_2-y_1)}{\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}} \times t \right| < \left|y_2 - y_1\right|)},\\
y_2 &{(\left|  \frac{v \times (y_2-y_1)}{\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}} \times t \right| \geq \left|y_2 - y_1\right|)}\\
\end{cases}
$$

We call $f_1(x_1,y_1,x_2,y_2,v,t)$ as $f_{ApproachPosX}$, $f_2(x_1,y_1,x_2,y_2,v,t)$ as $f_{ApproachPosY}$

($x_1$,$y_1$) is the initial position

($x_2$, $y_2$) is the final position

v is the speed

t is the input time

#### Wait then go to a position

$$
f_1(x_1,y_1,x_2,y_2, v,t,w)= \begin{cases}
x_1 &(t<w),\\
f_{ApproachPosX}(x_1,y_1,x_2,y_2,v,(t-w)) &(t \geq w)
\end{cases}
$$

$$
f_2(x_1,y_1,x_2,y_2, v,t,w) = \begin{cases}
y_1 &(t<w),\\
f_{ApproachPosY}(x_1,y_1,x_2,y_2,v,(t-w)) &(t \geq w)
\end{cases}
$$

We call $f_1(x_1,y_1,x_2,y_2, v,t,w)$ as $f_{WaitAndApproachPosX}$, $f_2(x_1,y_1,x_2,y_2, v,t,w)$ as $f_{WaitAndApproachPosY}$

($x_1$,$y_1$) is the initial position

($x_2$, $y_2$) is the final position

v is the speed

t is the input time

w is the time the drone should be waiting

#### The position each drone should be of the Ferris Wheel

$$
f_1(id, n, x,r,v, t) = x + r \times cos(\frac{id}{n} \times 2 \pi + \frac{v}{r} \times t)
$$

$$
f_2(id, n, y,r,v,t) = y + r \times sin(\frac{id}{n} \times 2 \pi + \frac{v}{r} \times t)
$$

We call $f_1(id, n, x,r,v, t)$ as $f_{WheelPosX}$, $f_2(id, n, y,r,v, t)$ as $f_{WheelPosY}$

id is the drone id

n is the number of drones

x is the x of the center of circle

r is the radius of the circle

v is the speed

t is the time

#### Time taken for going to the right position in Ferries

$$
\begin{equation}
f(n, y, r, d, v) = \frac{\sqrt{(y+r)^2 +  (f_{InitialPos(\frac{n}{4}, 0, n, d)})^2}}{v} + f_{WaitTime}(\frac{n}{4}, 0)
\end{equation}
$$

We call $f$ as $f_{ArriveTime}$

#### Time taken for a complete circle

$$
\begin{equation}
f(r, v) = \frac{2  \pi r}{v}
\end{equation}
$$

We call $f(r, v) $ as $f_{CircleTime}$

r is the radius

v is speed

#### The final equation of the Ferris Show

$$
f(id, t, n,x,d, y, r, v, cn) = \begin{cases}
f_{WaitAndApproachPosX}(f_{InitialPos}(id, x, n,d), 0 , f_{WheelPosX}(id, n, x, r, i, 0),  f_{WheelPosY}(id, n, y, r, i, 0), v, t, f_{WaitTime}(id, t)) &{t < f_{ArriveTime}}, \\
f_{WheelPosX}(id, n, x, r, v, t-f_{ArriveTime}) &{f_{ArriveTime} < t < f_{ArriveTime}+ f_{CircleTime}*cn}, \\
f_{WaitAndApproachPosX}(f_{WheelPosX}(id, n, x, r, i, 0),  f_{WheelPosY}(id, n, y, r, i, 0),f_{InitialPos}(id, x, n,d), 0, v, t-f_{ArriveTime}-f_{CircleTime}, f_{WaitTime}(id,t)) & {f_{ArriveTime}+f_{CircleTime}*cn < t < 2*f_{ArriveTime}+f_{CircleTime}*cn}
\end{cases}
$$



