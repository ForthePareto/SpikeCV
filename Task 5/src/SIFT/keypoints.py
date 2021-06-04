import numpy as np
import numpy.linalg as LA


def get_candidate_keypoints(D, w=16):
    candidates = []

    D[:, :, 0] = 0
    D[:, :, -1] = 0

    for i in range(w//2+1, D.shape[0]-w//2-1):
        for j in range(w//2+1, D.shape[1]-w//2-1):
            for k in range(1, D.shape[2]-1):
                patch = D[i-1:i+2, j-1:j+2, k-1:k+2]
                if np.argmax(patch) == 13 or np.argmin(patch) == 13:
                    candidates.append([i, j, k])

    return candidates


def localize_keypoint(D, x, y, s):
    dx = (D[y, x+1, s]-D[y, x-1, s])/2.
    dy = (D[y+1, x, s]-D[y-1, x, s])/2.
    ds = (D[y, x, s+1]-D[y, x, s-1])/2.

    dxx = D[y, x+1, s]-2*D[y, x, s]+D[y, x-1, s]
    dxy = ((D[y+1, x+1, s]-D[y+1, x-1, s]) -
           (D[y-1, x+1, s]-D[y-1, x-1, s]))/4.
    dxs = ((D[y, x+1, s+1]-D[y, x-1, s+1]) -
           (D[y, x+1, s-1]-D[y, x-1, s-1]))/4.
    dyy = D[y+1, x, s]-2*D[y, x, s]+D[y-1, x, s]
    dys = ((D[y+1, x, s+1]-D[y-1, x, s+1]) -
           (D[y+1, x, s-1]-D[y-1, x, s-1]))/4.
    dss = D[y, x, s+1]-2*D[y, x, s]+D[y, x, s-1]

    J = np.array([dx, dy, ds])
    HD = np.array([
        [dxx, dxy, dxs],
        [dxy, dyy, dys],
        [dxs, dys, dss]])

    offset = -LA.inv(HD).dot(J)
    return offset, J, HD[:2, :2], x, y, s


def find_keypoints_for_DoG_octave(D, R_th, t_c, w):
    candidates = get_candidate_keypoints(D, w)

    keypoints = []

    for i, cand in enumerate(candidates):
        y, x, s = cand[0], cand[1], cand[2]
        offset, J, H, x, y, s = localize_keypoint(D, x, y, s)

        contrast = D[y, x, s] + .5*J.dot(offset)
        if abs(contrast) < t_c:
            continue

        w, v = LA.eig(H)
        r = w[1]/w[0]
        R = (r+1)**2 / r
        if R > R_th:
            continue

        kp = np.array([x, y, s]) + offset
        if kp[1] >= D.shape[0] or kp[0] >= D.shape[1]:
            continue

        keypoints.append(kp)

    return np.array(keypoints)


def get_keypoints(DoG_pyr, R_th, t_c, w):
    kps = []
    print(R_th, t_c, w)

    from Corners import findCorners

    for D in DoG_pyr:
        img, points = findCorners(D)
        # kps.append(find_keypoints_for_DoG_octave(D, R_th, t_c, w))
        kps.append(points)

    return kps
