from .settings import *


INSTALLED_APPS += [
    "django_extensions",
]

SHELL_PLUS = "ipython"
SHELL_PLUS_PRINT_SQL = True

NOTEBOOK_ARGUMENTS = [
    "--ip",
    "0.0.0.0",
    "--port",
    "8010",
    "--allow-root",
    "--no-browser",
]

IPYTHON_ARGUMENTS = [
    "--ext",
    "django_extensions.management.notebook_extension",
    "--debug",
]

IPYTHON_KERNEL_DISPLAY_NAME = "Django Shell-Plus"

SHELL_PLUS_POST_IMPORTS = [
    ("decimal", ("Decimal",)),
    ("datetime", ('datetime', 'date', 'time', 'timedelta')),
    ('django.template.loader', ('get_template', 'render_to_string',)),
    ('django.db.models', ('Count', 'Subquery',
     'Max', 'Min', 'Q', 'F', 'Value', 'CharField', 'IntegerField', 'BooleanField', 'DateField',
                          'Case', 'When', 'OuterRef', 'Exists',)),
    ('django.db.models.functions', ('Coalesce', )),

]

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"


def skip_static_requests(record):
    if record.args[0].startswith('GET /static/'):  # filter whatever you want
        return False
    return True
