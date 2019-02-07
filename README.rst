==========
CRONTAB-PY
==========

Description
===========

Read file defined by ``crontab`` and run job according to the specified schedule.

Crontab module for reading crontab file. Schedule module for scheduling the jobs.

============= =========== ================= =================== =============
Field Name    Mandatory   Allowed Values    Special Characters  Extra Values
============= =========== ================= =================== =============
Minutes       Yes         0-59              \* / , -             < >
Hours         Yes         0-23              \* / , -             < >
Day of month  Yes         1-31              \* / , -             < >
Month         Yes         1-12 or JAN-DEC   \* / , -             < >
Day of week   Yes         0-6 or SUN-SAT    \* / , -             < >
============= =========== ================= =================== =============

Extra Values are '<' for minimum value, such as 0 for minutes or 1 for months.
And '>' for maximum value, such as 23 for hours or 12 for months.

Supported special cases allow crontab lines to not use fields.
These are the supported aliases which are not available in SystemV mode:

=========== ===========
Case        Meaning
=========== ===========
@reboot     Every boot
@hourly     0 * * * *
@daily      0 0 * * *
@weekly     0 0 * * 0
@monthly    0 0 1 * *
@yearly     0 0 1 1 *
@annually   0 0 1 1 *
@midnight   0 0 * * *
=========== ===========
