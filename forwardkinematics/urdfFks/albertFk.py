import numpy as np
import casadi as ca
from forwardKinematics.urdfFks.urdfFk import URDFForwardKinematics


class AlbertFk(URDFForwardKinematics):

    def __init__(self, n):
        fileName = 'albert.urdf'
        relevantLinks = ['panda_link' + str(i) for i in [0, 3, 4, 5, 6, 7, 8, 9]]
        super().__init__(fileName, relevantLinks, 'panda_link0', 7)


if __name__ == "__main__":
    q_ca = ca.SX.sym("q_ca", 10)
    pfk = AlbertFk(10)
    fkCasadi = pfk.fk(q_ca, 10)
    q_np = np.array([-0.01026582, -0.28908, 0.00922652, -1.3468, -0.026000, 2.074019, 0.06062268, 0.0, 0.0, 0.0])
    fkNumpy = pfk.fk(q_np, 7, positionOnly=True)
    print(fkNumpy)