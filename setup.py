from setuptools  import setup,  find_packages

setup(
    name = 'pyjosa',
    version = '0.0.8',
    description = '한국어 조사 처리 패키지',
    author = 'sehwan.kim',
    author_email = 'sehwan.kim@ingkle.com',
    url = 'https://github.com/kimsehwan96/pyjosa',
    packages = find_packages(exclude=[]),
    license='MIT',
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3.7'
    ],
    package_data = {},
    zip_safe=False,
    keyword = ['pypi', 'korea'],
)