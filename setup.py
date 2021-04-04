from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='sports_news_collector',
    version='0.1',
    description='Provide services by collecting various sports news',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Sangchun Ha',
    author_email='seomk9896@naver.com',
    url='https://github.com/hasangchun/sports_news_collector',
    install_requires=[
        'beautifulsoup4',
        'requests',
        'pretty_html_table',
        'pandas',
        'pororo',
    ],
    packages=find_packages(exclude=[]),
    python_requires='>=3',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)