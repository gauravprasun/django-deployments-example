#all custom filters here
from django import template
#create an instance of the template library
register = template.Library()

#register using decorator
@register.filter(name='cut')
#user-defined filter
def cut(value,arg):
    """
    This cuts out all values of "arg" form the string!
    """
    return value.replace(arg,'')

#register.filter('name_by_which_youcall_the_filter',name_of_the_function)
# register.filter('cut',cut)
