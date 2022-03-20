
class ModelMapper:
    '''
        Data To Object
    '''
    def make_instance(self, instance, values):
        attributes = instance.__dict__.keys()

        for attribute in attributes:
            try:
                # field names from oracle sp are UPPER CASE
                # we want to put PIC_ID in pic_id etc.
                # setattr(instance, a, values.get(a))
                # del values.get(a)
                if attribute in values.keys():
                    setattr(instance, attribute, values.get(attribute))
                    values.pop(attribute)
            except AttributeError:
                pass
            except Exception as e:
                print(e)

        for other_key in values.keys():
            setattr(instance, other_key, values.get(other_key))

        return instance
