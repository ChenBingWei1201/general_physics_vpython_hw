from vpython import *
A, N, omega = 0.10, 50, 2*pi/1.0
size, m, k, d = 0.06, 0.1, 10.0, 0.4 # d為兩顆球的距離
scene = canvas(title='Spring Wave', width=800, height=300, background=vec(0.5,0.5,0), center = vec((N-1)*d/2, 0, 0))
balls = [sphere(radius=size, color=color.red, pos=vector(i*d, 0, 0), v=vector(0,0,0)) for i in range(N)] # 0 --> N-1 (N個球)
springs = [helix(radius = size/2.0, thickness = d/15.0, pos=vector(i*d, 0, 0), axis=vector(d,0,0)) for i in range(N-1)] # 0 --> N-2 (N-1個彈簧)
t, dt = 0, 0.001                                                              # 彈簧向右延伸一個d 
while True:
 rate(1000)
 t += dt
 balls[0].pos = vector(A * sin(omega * t ), 0, 0) # 第一顆球隨時間震動
 for i in range(N-1): # 0 --> N-2
    springs[i].pos = balls[i].pos 
    springs[i].axis = balls[i+1].pos - balls[i].pos
 for i in range(1, N):
    if i == N-1: 
       balls[-1].v += - k * vector((springs[-1].axis.mag-d),0,0)/m*dt # the last ball is connected to one only spring
    else:                     # the right-hand-side one                      # the left-hand-side one
       balls[i].v += k* vector((springs[i].axis.mag-d),0,0)/m*dt - k* vector((springs[i-1].axis.mag-d),0,0)/m*dt # other balls
    balls[i].pos += balls[i].v*dt