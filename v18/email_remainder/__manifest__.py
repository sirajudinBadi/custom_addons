{
    "name": "Email Remainder",
    "description": "Email Remainder",
    "summary": "Task email remainder for deadline and timesheet tracker.",
    "author": "John Doe",
    "website": "www.example.com",
    "license" : "LGPL-3",
    "depends": ['base','mail','project','hr_timesheet'],
    "application": False,
    "installable": True,
    "data" : [
        "security/ir.model.access.csv",
        "data/cron_task_remainder.xml",
        "data/cron_timesheet_summary.xml",
    ],
}
