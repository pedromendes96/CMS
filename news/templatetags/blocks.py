from django import template

register = template.Library()


@register.simple_tag
def get_distinct_block_types_list(body):
    types = []
    for instance in body:
        instance_type = type(instance.block)
        if instance_type not in types:
            types.append(instance_type)
    return types


@register.simple_tag
def interact(blocks_types, index):
    return blocks_types[index]
