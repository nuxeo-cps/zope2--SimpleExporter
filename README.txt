Purpose
-------

To export simple Zope objects (files, folder, documents...) as a simple
hierarchy in the filesystem, with properties as Python dictionaries in
<filename>.properties files.

How to use it
-------------

1. Create an external method "export" with parameters:

id: export
module: SimpleExporter.export
function: export

2. Run it

3. You will get your content as a hierarchy of directories and files in
<your instance>/var/simple_export/...
