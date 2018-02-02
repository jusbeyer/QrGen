from setuptools import setup

setup(
    name='QrGen',
    version='1.0.0',
    packages=['QrGen'],
    url='',
    license='',
    author='Justin Beyer',
    author_email='jusbeyer@gmail.com',
    description='Utilizes qrcode and Pillow (PIL fork) to generate a QR code',
    install_requires=['pillow', 'qrcode']
)
