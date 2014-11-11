Django Maintenance in Progress
==============================
**Intercept possible 500 errors when site maintenance is in progress and display a friendly page.**

.. figure:: https://travis-ci.org/praekelt/django-maintenance-in-progress.svg?branch=develop
   :align: center
   :alt: Travis

Overview
--------

During system maintenance some pages may produce errors due to eg. database upgrades. A blanket rule
would take down the entire site, which is naturally undesirable. ``maintenance_in_progress`` only displays
a maintenance message when a 500 error is encountered during the maintenance window.

Installation
------------

#. Install or add ``django-maintenance-in-progress`` to your Python path.

#. Add ``maintenance_in_progress`` to your ``INSTALLED_APPS`` setting.

#. Set ``handler500 = 'maintenance_in_progress.views.server_error'`` in ``urls.py``.


Usage
-----

Admin has a ``Maintenance In Progress Preferences`` link where you can choose to indicate
maintenance is in progress either by a flag in the database or by creating a file on the
filesystem.

