from setuptools import setup, find_packages

setup(
    name='chatgpt_automation_mac',
    version='0.1',
    author='Your Name',
    author_email='your.email@example.com',
    description='A package for automating interactions with OpenAI ChatGPT using Selenium WebDriver on macOS',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/chatgpt_automation_mac',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
    ],
    python_requires='>=3.6',
    install_requires=[
        'selenium',
    ],
)
