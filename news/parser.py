import json
import logging
from html.parser import HTMLParser

logger = logging.getLogger("news")


class JsonParserException(Exception):
    pass


class DummyExtraParamsTag(object):
    def __init__(self, info_tag):
        self.info_tag = info_tag

    def get_extra_info(self):
        return {}


class ExtraParamsImg(DummyExtraParamsTag):
    def get_extra_info(self):
        # here for example i could return the size
        # extension, etc...
        # a url of a small one
        pass


class ExtraParamsFactory(object):
    TAG = "tag"
    factory_instances = {
        "img": ExtraParamsImg
    }

    def get_instance(self, info_tag):
        return self.factory_instances.get("", DummyExtraParamsTag)(info_tag[self.TAG])


class JsonHtmlParser(HTMLParser):
    CHILDREN = "children"
    TAG = "tag"
    ATTRIBUTES = "ATTRIBUTES"
    DATA = "data"

    def __init__(self, *args, **kwargs):
        super(JsonHtmlParser, self).__init__(*args, **kwargs)
        self.deep = 0
        self.content = []
        self.convert_charrefs = True

    def error(self, message):
        raise JsonParserException("Error trying to parse the HTML Content")

    def _follow_order(self):
        context = self.content
        for index in range(self.deep):
            context = context if index == 0 else context[-1][self.CHILDREN]
        return context

    # Overridable -- finish processing of start+end tag: <tag.../>
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    # Overridable -- handle start tag
    def handle_starttag(self, tag, attrs):
        info = dict()
        info[self.TAG] = tag
        info_attrs = dict()
        for attr in attrs:
            info_attrs[attr[0]] = attr[1]
        info[self.ATTRIBUTES] = info_attrs
        info[self.CHILDREN] = []
        info[self.DATA] = ""
        if len(self.content) == 0:
            self.content.append(info)
        else:
            children = self._follow_order()
            if len(children) != 0:
                children[-1][self.CHILDREN].append(info)
        self.deep += 1

    # Overridable -- handle end tag
    def handle_endtag(self, tag):
        self.deep -= 1

    # Overridable -- handle data
    def handle_data(self, data):
        if len(self.content) == 0:
            return
        children = self._follow_order()
        if len(children) > 0:
            tag_info = children[-1]
            tag_info[self.DATA] = data

    def get_content(self):
        return json.dumps(self.content)
