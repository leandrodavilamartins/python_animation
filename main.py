import matplotlib.pyplot as plt 
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation 
import numpy as np 

t0 = 0
t_end = 2 
dt = 0.005

t = np.arange(t0,t_end+dt, dt)

x = 800*t

altitude = 2

y = np.ones(len(t))* altitude

#print(y)

####################################### ANIMATION ################################################

frame_amount = len(t)

def update_plot(num):
    plane_trajectory.set_data(x[0:num],y[0:num])

    return plane_trajectory,

fig = plt.figure(figsize=(16,9),dpi=120,facecolor=(0.1,0.1,0.1))
gs = gridspec.GridSpec(2,2)

#Subplot1 
ax0 = fig.add_subplot(gs[0,:],facecolor=(0.1,0.1,0.1))

ax0.set_xlabel('Distância (km)')
ax0.set_ylabel('Altitude (km)')

ax0.xaxis.label.set_color('white')        #setting up X-axis label color to yellow
ax0.yaxis.label.set_color('white')          #setting up Y-axis label color to blue

ax0.tick_params(axis='x', colors='white')    #setting up X-axis tick color to red
ax0.tick_params(axis='y', colors='white')  #setting up Y-axis tick color to black

plane_trajectory = ax0.plot([],[],'#ff3e00',linewidth=1)[0]
plt.xlim(x[0],x[-1])
plt.ylim(0,y[0] + 1)


plane_ani = animation.FuncAnimation(fig,update_plot,frames=frame_amount,interval=20,repeat=True,blit=True)
plt.show()