import numpy as np
import time
import theano
import theano.tensor as T
from theano import sparse
from collections import Counter
from scipy.sparse import coo_matrix

vert_to_id = {}
id_to_vert = {}


def get_M(web_graph):
    print 'Reading counts'

    d = Counter()

    verts = set([])

    with open(web_graph) as f:
        for line in f:
            if '#' in line:
                continue
            else:
                values = [int(x) for x in line.split()]
                d[values[0]] += 1
                verts.add(values[0])
                verts.add(values[1])
        f.close()

    verts = list(verts)
    for i in range(0, len(verts)):
        vert_to_id[verts[i]] = i
        id_to_vert[i] = verts[i]

    one_div_d = {}
    for k in d.keys():
        one_div_d[k] = 1.0 / d[k]

    print 'Reading links'

    rows = []
    cols = []
    data = []

    with open(web_graph) as f:
        for line in f:
            values = [int(x) for x in line.split()]
            rows.append(vert_to_id[values[1]])
            cols.append(vert_to_id[values[0]])
            data.append(one_div_d[values[0]])
        f.close()

    print 'Constructing sparse matrix'

    return coo_matrix((data, (rows, cols))).tocsr()


def main():
    eps = 1.0e-9

    M_ = get_M('web-Google.txt')
    N = M_.shape[0]

    one_div_N = 1.0 / float(N)
    one_div_N_vector_ = np.repeat(one_div_N, N)
    one_div_N_vector = theano.shared(one_div_N_vector_)

    beta = 0.8

    M = theano.shared(M_)
    r = np.repeat(one_div_N, N)

    r_ = T.dvector()
    update_r = theano.function([r_], beta * theano.sparse.basic.dot(M, r_))

    rj_ = T.dvector()
    fix_r = theano.function([rj_], rj_ + (1.0 - rj_.sum()) * one_div_N_vector)

    r_new_ = T.dvector()
    error = theano.function([r_, r_new_], abs(r_new_ - r_).sum())

    start = time.time()

    i = 1
    while True:
        print 'Iteration ', i
        i += 1
        rj = update_r(r)
        r_new = fix_r(rj)
        if error(r_new, r) < eps:
            break
        r = r_new

    end = time.time()

    print 'Elapsed time =', end - start

    print r[vert_to_id[99]]


if __name__ == '__main__':
    main()