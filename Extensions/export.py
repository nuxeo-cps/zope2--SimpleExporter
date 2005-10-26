import pprint, os.path
from types import StringType


class SimpleExporter:
    def __init__(self, root):
        self.root = root
        self.export_home = os.path.join(INSTANCE_HOME, "var", "simple_export")
        try:
            os.mkdir(self.export_home)
        except OSError:
            pass

    def exportRoot(self):
        self.exportObject(self.root, "")

    def exportObject(self, object, path):
        object_id = object.getId()
        object_path = os.path.join(path, object_id)
        sub_items = []
        try:
            sub_items = object.objectValues()
        except:
            pass

        if sub_items:
            try:
                os.mkdir(os.path.join(self.export_home, object_path))
            except OSError:
                pass

        else:
            object_data = ''
            if hasattr(object, 'document_src'):
                try:
                    object_data = object.document_src()
                except:
                    print "Error on object", object_path
                    print "Proceeding anyway"
            elif hasattr(object, 'data'):
                object_data =str(object.data)
                if type(object_data) != StringType:
                    print object_path, type(object_data)
            fd = open(os.path.join(self.export_home, object_path), "wc")
            fd.write(object_data)

        properties_dump = []
        if hasattr(object, "propertyMap"):
            for prop_map in object.propertyMap():
                prop_id = prop_map['id']
                d = prop_map.copy()
                d['value'] = getattr(object, prop_id, None)
                if d['value']:
                    properties_dump.append(d)
            fd = open(os.path.join(self.export_home, object_path + ".properties"), "wc")
            fd.write(pprint.pformat(properties_dump))

        for sub_item in sub_items:
            self.exportObject(sub_item, object_path)

def export(self):
    exporter = SimpleExporter(self)
    exporter.exportRoot()

