import numpy as np
import open3d as o3d

def getSin(N):
    u = np.linspace(0, np.pi*2, N)
    v = np.linspace(0, np.pi*2, N)
    u,v = np.meshgrid(u,v)
    x = np.cos(u).reshape(-1)
    y = np.cos(v).reshape(-1)
    z = np.cos(u+v).reshape(-1)
    return np.array([x,y,z]).T

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(getSin(500))
o3d.visualization.draw_geometries([pcd])
