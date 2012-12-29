from distutils.core import setup

setup(
    name='mechanig',
    description='A One-stop configuration tool for Unity',
    url='https://github.com/jokerdino/mechanig',
    version='0.0.1',
    author='Barneedhar Vigneshwar',
    author_email='barneedhar@ubuntu.com',
    license='GPLv3+',
    packages=['mechanig'],
    scripts=['mechanig-gtk'],
    package_data={'mechanig': ['data/*.ui','data/*.png',
                                'data/icons/24/*.svg','data/icons/36/*.svg','data/icons/48/*.svg']},
    data_files=[
        ('share/applications',
            ['mechanig.desktop']
        ),
    ]
)
