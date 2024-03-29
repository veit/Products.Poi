# -*- coding: utf-8 -*-
#
# File: Issue.py
#
# Copyright (c) 2006 by Copyright (c) 2004 Martin Aspeli
# Generator: ArchGenXML Version 1.5.1-svn
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

__author__ = """Martin Aspeli <optilude@gmx.net>"""
__docformat__ = 'plaintext'

from Interface import Base


class Issue(Base):
    """Marker interface for Poi Issues
    """

    # Methods

    def toggleWatching():
        """
        Add or remove the current authenticated member from the list of
        watchers.
        """

    def isWatching():
        """
        Determine if the current user is watching this issue or not.
        """

    def getLastModificationUser():
        """
        Get the user id of the user who last modified the issue, either
        by
        creating, editing or adding a response to it. May return None if
        the user is unknown.
        """


# end of class Issue
