=====
Usage
=====

To use Nobinobi Core in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'nobinobi_core.apps.NobinobiCoreConfig',
        ...
    )

Add Nobinobi Core's URL patterns:

.. code-block:: python

    from nobinobi_core import urls as nobinobi_core_urls


    urlpatterns = [
        ...
        path('', include(nobinobi_core_urls)),
        ...
    ]
