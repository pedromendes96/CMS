class OrderObject(object):
    def __init__(self, item, order_key):
        for key, element in item.items():
            setattr(self, key, element)
        self.order_key = order_key

    def to_array(self):
        context = []
        for key in vars(self).keys():
            if key != "order_key":
                context.append(str(getattr(self, key)))
        return context

    def to_json(self):
        context = dict()
        for key in vars(self).keys():
            if key == "order_key":
                continue
            context[key] = str(getattr(self, key))
        return context
