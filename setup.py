from setuptools import setup


setup(
      name='my_custom_sklearn_transformations',
      version='1.0',
      description='''
            This is a sample python package for encapsulating custom
            tranforms from scikit-learn into Watson Machine Learning
      ''',
      url='https://github.com/Alextnetto/watson-sklearn-tranformations',
      author='Alexandro T. Netto',
      author_email='alex.t.netto@gmail.com',
      license='BSD',
      packages=[
            'my_custom_sklearn_transformations'
      ],
      install_requires=[
          'pandas',
      ],
      zip_safe=False
)
