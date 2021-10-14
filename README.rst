********************************************************
Qarnot computing Python SDK - Python2.7 partial backport
********************************************************

This is a partial backport to Python 2.7 of our `official Python SDK <https://github.com/qarnot/qarnot-sdk-python>`_.
Please have a look at that repository for documentation.

Unless you have a strong reason to use this version, you should be using the
official version targetting Python 3.6+ linked above.


Disclaimers
###########


Python 2.7 end-of-life
**********************

We kindly remind readers that Python 2.7 has seen its official end of life on
January 1, 2020. That means that from this date, no bug fix or even security fix
has been and ever will be applied to the core Python 2.7 code, unless you are
buying some extended support from a company offering it, or maintaining it yourself.


Partial feature set
*******************

This backport is supplied as a convenience to be used by some people, organisations,
or products that are still relying on Python 2.7. This is by no means an offical support
for Python 2.7, and this should not be considered as being one of our offical SDKs.

This is a **partial** backport of our official SDK which was forked from version 2.3.1. From that point:

* an arbitrary set of features, improvements or bug fixes may be missing compared to the official SDK
* an arbitrary set of features may be broken or break in the future


Install
#######

This version is not distributed on pypi, but you can install directly from git:

* manually with ``pip``::

    pip install git+https://github.com/qarnot/qarnot-sdk-python-27.git

* or in your ``requirements.txt``::

    git+https://github.com/qarnot/qarnot-sdk-python-27.git

You can also specify a given branch, tag or commit by suffixing it after an ``@``, for instance::

    git+https://github.com/qarnot/qarnot-sdk-python-27.git@36fb3d9855f71d7402e29869985853908cc45792
