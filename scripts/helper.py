import numpy


def mandelbrot(c, maxiter):
    output = numpy.zeros_like(c, dtype=numpy.int32)
    z = numpy.zeros_like(c, dtype=numpy.complex64)
    for n in range(maxiter):
        mask = numpy.less(z.real**2 + z.imag**2, 4.0)
        output[mask] = n
        z[mask] = z[mask]**2 + c[mask]
    output[output == maxiter - 1] = 0
    return output


def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, maxiter):
    x = numpy.linspace(xmin, xmax, num=width)
    y = numpy.linspace(ymin, ymax, num=height)
    X, Y = numpy.meshgrid(x, y)
    c = X + 1j * Y
    n = mandelbrot(c, maxiter)
    return x, y, n
