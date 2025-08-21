{
    "name": "Project Custom",
    "description": "Custom Project Module",
    "summary": """Custom Project Module for Inheritance practice purpose.""",
    "category": "Project",
    "sequence": 1,
    "author": "John Doe",
    "license": "LGPL-3",
    "application": True,
    "installable": True,
    "website": "www.example.com",
    "depends": ["base", "project", "report_xlsx"],
    "data": [
        "security/ir.model.access.csv",

        # wizard first (so report can reference it later)
        "wizard/project_task_report_wizard_views.xml",
        "wizard/project_task_report_wizard_actions.xml",

        # report files next
        "report/project_task_report_actions.xml",
        "report/project_task_report_menus.xml",
        "report/project_task_report_pdf_template.xml",

        # checklist & other views
        "views/project_task_checklist_views.xml",
        "views/project_task_checklist_actions.xml",
        "views/project_task_checklist_menus.xml",
        "views/project_task_inherit_view.xml",
    ],
    "images": ["static/description/icon.png"],
}
