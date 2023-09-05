import os.path as osp

from setuptools import find_packages, setup

requirements = ["hydra-core", "pytorch-lightning", "numpy", "msgpack-numpy""lmdb","h5py","ninja","hydra-core","pointnet2_ops_lib"]


exec(open(osp.join("pointnet2", "_version.py")).read())

setup(
    name="pointnet2",
    version=__version__,
    author="Erik Wijmans",
    packages=find_packages(),
    install_requires=requirements,
)
