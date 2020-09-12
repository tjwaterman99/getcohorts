.. GetCohorts documentation master file, created by
   sphinx-quickstart on Thu Sep 10 20:07:38 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
   :hidden:

   install
   reference


GetCohorts
==========

GetCohorts enables random, idempotent allocations of a user to an experiment's cohort.

.. code-block::

   >>> from getcohorts import get_cohort
   >>> get_cohort('userid-6', 'homepage-test', cohorts=['experimental', 'control'])
   'experimental'

