# -*- coding: utf-8 -*-

"""
Django settings for leprikonweb project.
"""

from django.utils.translation import ugettext_lazy as _
from cms_site.settings import *

ADMINS = (('Jakub Dorňák', 'jakub.dornak@misli.cz'),)
MANAGERS = ADMINS
SERVER_EMAIL = 'Leprikón @ {} <admin@leprikon.cz>'.format(os.uname()[1])

GANALYTICS_TRACKING_CODE = 'UA-78897621-1'

CONTAINER_TEMPLATES = {
    'collapse': {
        'label': _('collapse'),
    },
}
