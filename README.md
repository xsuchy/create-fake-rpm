create-fake-rpm
---------------
Generate fake rpm.

This script creates empty RPM package to satisfy the dependencies.

It may be useful when you install some library/module/application manually - without having an RPM package.
E.g., when you

    pip install somepackage

And when some RPM package `Requires: python-somepackage` then /usr/bin/rpm refuses to install such package,
because `python-somepackage` is not present on your system.
RPMDB does not know what you know. So you can run:

    create-fake-rpm --build python-somepackage 'python3dist(somepackage)'

This create package `fake-python-somepackage-0-0.noarch.rpm` which provides: "python-somepackage" and "python3dist(somepackage)".
You can install it using:

    dnf install fake-python-somepackage-0-0.noarch.rpm

!!!! WARNING !!!!

This is a big gun. You can easily shot yourself in a leg.
Do not use this tool unless you know what you are doing.
And if you know what you are doing - then think twice before you use it.
You can easily destroy your machine with this tool.

## Packaging status

![create-fake-rpm versions](https://repology.org/badge/vertical-allrepos/create-fake-rpm.svg?exclude_unsupported=1&header=create-fake-rpm)

LICENSE
-------

GPLv2+
