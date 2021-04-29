import numpy as np
import collections

def p1(string):
    dims = string.split('\n')
    sdims = [list(map(int, dim.split('x'))) for dim in dims]
    conv_dims = [[[l, w], [w, h], [h, l]] for l, w, h in sdims]
    conv_dims = np.array(conv_dims)
    conv_dims = np.product(conv_dims, axis=2)
    sum_min_sides = np.sum(np.min(conv_dims, axis=1))
    areas = np.sum(conv_dims, axis=1) 
    tarea = np.sum(areas)
    print(tarea * 2 + sum_min_sides)

def main(string):
    dims = string.split('\n')
    sdims = [list(map(int, dim.split('x'))) for dim in dims]
    max_sdims = np.max(sdims, axis = 1)
    print(max_sdims)
    print(2*( np.sum(sdims) - np.sum(max_sdims) ) + np.sum(np.product(sdims, axis=1)))
        

        

if __name__ == '__main__':
    with open('day2.input', 'r') as f:
        string = f.read()
    main(string)