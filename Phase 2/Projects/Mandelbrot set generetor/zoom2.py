from PIL import Image
import numpy as np
from numba import njit, prange
import time


@njit(parallel=True, fastmath=True)
def mandelbrot_gen(
    image_width,
    image_height,
    x_min,
    x_max,
    y_min,
    y_max,
    max_iterations,
):

    grid = np.zeros((image_height, image_width, 3), dtype=np.uint8)

    for row in prange(image_height):

        imag = y_min + row * (y_max - y_min) / (image_height - 1)

        for col in range(image_width):

            real = x_min + col * (x_max - x_min) / (image_width - 1)

            zr = 0.0
            zi = 0.0

            iteration = 0

            while iteration < max_iterations:

                zr2 = zr * zr
                zi2 = zi * zi

                if zr2 + zi2 > 4.0:
                    break

                zi = 2.0 * zr * zi + imag
                zr = zr2 - zi2 + real

                iteration += 1

            if iteration == max_iterations:

                grid[row, col, 0] = 0
                grid[row, col, 1] = 0
                grid[row, col, 2] = 0

            else:

                t = iteration / max_iterations

                r = int(9 * (1 - t) * t * t * t * 255)
                g = int(15 * (1 - t) * (1 - t) * t * t * 255)
                b = int(8.5 * (1 - t) * (1 - t) * (1 - t) * t * 255)

                grid[row, col, 0] = r
                grid[row, col, 1] = g
                grid[row, col, 2] = b

    return grid


def create_zoom_animation(
    image_width,
    image_height,
    total_frames=2,
    zoom_factor=0.97,
):

    x_min = -2.0
    x_max = 1.0

    y_min = -1.5
    y_max = 1.5

    center_x = -0.743643887037151
    center_y = 0.131825904205330

    max_iterations = 500

    for frame in range(total_frames):

        image = mandelbrot_gen(
            image_width,
            image_height,
            x_min,
            x_max,
            y_min,
            y_max,
            max_iterations,
        )

        Image.fromarray(image).save(
            f"Phase 2/Projects\Mandelbrot set generetor/frames/frame_{frame:04d}.png"
        )

        width = (x_max - x_min) * zoom_factor
        height = (y_max - y_min) * zoom_factor

        x_min = center_x - width / 2
        x_max = center_x + width / 2

        y_min = center_y - height / 2
        y_max = center_y + height / 2

        max_iterations = int(max_iterations * 1.01)

        print(f"Frame {frame+1}/{total_frames}")


start = time.perf_counter()

create_zoom_animation(
    1920,
    1080,
    total_frames=1000
)

end = time.perf_counter()

print(f"Time : {end-start:.2f} seconds")