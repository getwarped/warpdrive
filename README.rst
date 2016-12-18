The ``warpdrive`` project provide the scripts for implementing a build and
deployment system for Python web applications using Docker. The scripts can
be integrated into a suitable Docker base image to provide a more
structured way for incorporating a Python web application into a Docker
image, with ``warpdrive`` doing all the hard work of co-ordinating the
build of the Docker image containing your application. The ``warpdrive``
scripts will also handle the startup of the Python web application when the
container is run.

As well as basic support for working with Docker directly, the ``warpdrive``
project also provides ``assemble`` and ``run`` scripts suitable for use
with the `Source-to-Image`_ (S2I) project. This allows a Docker image to be
enabled as a S2I builder for constructing Docker images for your
application without you needing to even know how to build Docker
containers. Any S2I enabled Docker image would also be able to be used as a
S2I builder with any Docker based PaaS with S2I support built in, such as
OpenShift.

For additional documentation on ``warpdrive`` including examples of use
see:

  * http://warpdrive.readthedocs.io

For examples of Docker images which incorporate the ``warpdrive`` scripts
see:

  * `warp0-debian8-python`_
  * `warp0-centos7-python`_

If you would like to try ``warpdrive`` with OpenShift, but would like to
use the default OpenShift Python images as a base, templates are provided
which use the standard Python images, but where the existing S2I scripts
will be overridden. To load these templates use the command::

    oc create -f https://raw.githubusercontent.com/GrahamDumpleton/warpdrive/master/openshift/warpdrive-python.json

This will create the following templates in OpenShift::

    warpdrive-python27
    warpdrive-python33
    warpdrive-python34
    warpdrive-python35

.. _`Source-to-Image`: https://github.com/openshift/source-to-image
.. _`warp0-debian8-python`: https://github.com/GrahamDumpleton/warp0-debian8-python
.. _`warp0-centos7-python`: https://github.com/GrahamDumpleton/warp0-centos7-python
