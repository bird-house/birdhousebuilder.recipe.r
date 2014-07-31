*************************
birdhousebuilder.recipe.r
*************************

.. contents::

Introduction
************

``birdhousebuilder.recipe.r`` is a `Buildout`_ recipe to install r packages with `Anaconda`_.

.. _`Buildout`: http://buildout.org/
.. _`Anaconda`: http://continuum.io/

Usage
*****

Supported options
=================

Example usage
=============

Example usage in your ``buildout.cfg`` to install ``R`` with Anaconda and the additional ``R`` packages from a ``R`` repository::

   [r_pkgs]
   recipe = birdhousebuilder.recipe.r
   repo = http://ftp5.gwdg.de/pub/misc/cran
   pkgs = sp raster ncdf PresenceAbsence

