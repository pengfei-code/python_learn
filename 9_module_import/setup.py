from distutils.core import setup

setup(
    name = "songhannuo",
    version = "1.0",
    description = "This module is implement a hannuota",
    author = "songpengfei",
    url = " http://www.songpengfei.com",
    license = " LGPL ",
    author_email = "spf_tay@163.com",
    # packages = ["modulea","modulea.a","modulea.a.aa"]
    # These packages are better placed under the same package
    py_modules = ["songtest.hannuota"]
)

#You can use the pip3 to install twine
#and use twine upload *.tar.gz  ，then input the username - password to upload


