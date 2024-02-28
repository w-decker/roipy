from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

def animate_(func, frames: int, fname: str, interval:int, figsize=(5, 5), save=True):

    fig = plt.figure(figsize=figsize)

    def update(frame):
        plt.clf()
        return func(frame)

    anim = FuncAnimation(fig, update, frames=frames, blit=False, repeat=False, interval=interval)

    return anim

