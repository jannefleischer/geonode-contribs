# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2019 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################
import io
from os.path import (
    dirname,
    join,
)
from setuptools import (
    find_packages,
    setup
)


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf-8")
    ).read()


setup(
    name="geonode_ldap",
    version="1.0.0",
    description="GeoNode contrib app for integrating with django_auth_ldap",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Ricardo Garcia Silva",
    author_email="ricardo.garcia.silva@gmail.com",
    url="https://github.com/GeoNode/geonode-contribs",
    license="GPL",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django-auth-ldap",
        "geonode<=4.0",
        "python-ldap",
    ],
)
