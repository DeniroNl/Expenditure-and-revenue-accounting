#!/usr/bin/python3

from setuptools import setup, find_packages

setup(
    name='course_lib',
    version='0.0.1',
    packages=find_packages("."),
    scripts=["bin/task_course.py"],
    url='https://github.com/DeniroNl/Expenditure-and-revenue-accounting',
    license='Apache-2.0',
    author='Бут Денис Олегович',
    author_email='denibutfuture@gmail.com',
    description='Пакет для ведения учёта расходов и доходов',
    include_package_data=True,
    install_requires=["datetime"],
)