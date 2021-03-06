========================================================================================================================
Quickstart
========================================================================================================================

------------------------------------------------------------------------------------------------------------------------
Install
------------------------------------------------------------------------------------------------------------------------

.. code::

    pip install highton


------------------------------------------------------------------------------------------------------------------------
Setup
------------------------------------------------------------------------------------------------------------------------

Just setup highton by defining a singleton in your application.
You don't have to store this singleton in a variable.

.. code:: python

    from highton.highton_settings import HightonSettings

    HightonSettings(username='<your_username>', api_key='<your_API_KEY>')


------------------------------------------------------------------------------------------------------------------------
Retrieve data
------------------------------------------------------------------------------------------------------------------------

If you have defined the 'USERNAME' and 'API_KEY', you can start to retrieve data:

.. code:: python

    from highton.models import Deal

    deals = Deal.list()


------------------------------------------------------------------------------------------------------------------------
Get a single object
------------------------------------------------------------------------------------------------------------------------

.. code:: python

    from highton.models import Deal

    deal_object = Deal.get(12345)

------------------------------------------------------------------------------------------------------------------------
Create data
------------------------------------------------------------------------------------------------------------------------

.. code:: python

    from highton.models import Deal

    new_deal_object = Deal(name='new deal').create()

------------------------------------------------------------------------------------------------------------------------
Update data
------------------------------------------------------------------------------------------------------------------------

.. code:: python

    from highton.models import Deal

    deal_object = Deal.get(12345)
    deal_object.name = 'new name'
    deal_object.update()

------------------------------------------------------------------------------------------------------------------------
Delete data
------------------------------------------------------------------------------------------------------------------------

.. code:: python

    from highton.models import Deal

    deal_object = Deal.get(12345)
    deal_object.delete()

