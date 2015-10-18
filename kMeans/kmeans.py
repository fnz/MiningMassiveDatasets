import numpy as np


def kmeans_clusters(points, centroids, iterations):
    for t in range(0, iterations):
        clusters = {}
        for index, centroid in centroids.items():
            clusters[index] = list()
            clusters[index].append(centroid)

        for p in points:
            kc = -1
            kmin = float("inf")
            for i in range(0, len(centroids)):
                d = np.linalg.norm(p - centroids[i])
                if d < kmin:
                    kc = i
                    kmin = d

            clusters[kc].append(p)

        for i in range(0, len(centroids)):
            centroid = np.array((0.0, 0.0))
            for p in clusters[i]:
                centroid += p

            centroid /= len(clusters[i])
            centroids[i] = centroid

    return clusters, centroids


def main():
    points = [(28, 145), (38, 115), (50, 130), (55, 118), (65, 140), (43, 83), (50, 90), (63, 88), (50, 60), (50, 30)]
    points = [np.array(p).astype(float) for p in points]

    centroids_ = [(25, 125), (44, 105), (29, 97), (35, 63), (55, 63), (42, 57), (23, 40), (64, 37), (33, 22), (55, 20)]
    centroids_ = [np.array(p).astype(float) for p in centroids_]

    centroids = {}
    for i in range(0, len(centroids_)):
        centroids[i] = centroids_[i]

    clusters, centroids = kmeans_clusters(points, centroids, 2)

    print 'Centroids:'
    for k, v in centroids.items():
        print k, v

    print 'Clusters:'
    for k, v in clusters.items():
        print k, v


if __name__ == '__main__':
    main()