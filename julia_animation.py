import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def julia(z, c, max_iter=100):
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter

def generate_julia_set(c, width=800, height=800, max_iter=100):
    julia_set = np.zeros((width, height))
    for x in range(width):
        for y in range(height):
            real = 4 * (x - width / 2) / width
            imag = 4 * (y - height / 2) / height
            z = complex(real, imag)
            julia_set[x, y] = julia(z, c, max_iter)
    return julia_set

def animate_julia(c_start, max_frames=100, output_file=None):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.axis('off')

    julia_set = generate_julia_set(c_start)
    im = ax.imshow(julia_set.T, cmap="twilight", extent=[-2, 2, -2, 2])

    def update(frame):
        angle = frame * 0.1
        c = complex(np.cos(angle) * 0.8, np.sin(angle) * 0.8)
        julia_set = generate_julia_set(c)
        im.set_data(julia_set.T)
        ax.set_title(f"Julia Set\nc = {c.real:.2f} + {c.imag:.2f}i", fontsize=16, fontfamily='serif', color='black')
        return [im]

    anim = FuncAnimation(fig, update, frames=max_frames, interval=50, blit=False)

    if output_file:
        anim.save(output_file, fps=20, extra_args=['-vcodec', 'libx264'])
    else:
        plt.show()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        c_real = float(sys.argv[1])
        c_imag = float(sys.argv[2])
        c_start = complex(c_real, c_imag)
    else:
        c_start = complex(-0.749, 0.175)

    animate_julia(c_start)
