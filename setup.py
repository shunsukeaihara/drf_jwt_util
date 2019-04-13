from setuptools import setup, find_packages

setup(
    name="drf_jwt_util",
    version="0.1",
    description="drf jwt util",
    author='Shunsuke Aihara',
    author_email='aihara@argmax.jp',
    url='https://github.com/shunsukeaihara/drf_jwt_util',
    packages=find_packages(),
    include_package_data=True,
    install_requires=["django", "djangorestframework", "djangorestframework-jwt"],
    tests_require=["tox", "factory_boy"],
    license="MIT License",
)
