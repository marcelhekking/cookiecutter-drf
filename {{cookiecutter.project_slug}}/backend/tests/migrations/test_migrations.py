from io import StringIO

import pytest
from django.core.management import call_command
from django.test import override_settings


@pytest.mark.django_db
@override_settings(MIGRATION_MODULES={})
def test_for_missing_migrations():
    output = StringIO()
    call_command("makemigrations", no_input=True, dry_run=True, stdout=output)
    assert output.getvalue().strip() == "No changes detected", (
        "There are missing migrations:\n %s" % output.getvalue()
    )
