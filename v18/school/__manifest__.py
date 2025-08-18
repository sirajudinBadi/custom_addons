{
    "name": "School",
    "summary": "School Management System",
    "description": """This module will cover Student, Teacher, Parent, Classroom, Subject and Academic Year related operations.""",
    "version": "18.0.1.1",
    "depends": ["base"],
    "author": "Sirajudin Badi",
    "category": "Education",
    "website": "www.example.com",
    "license": "LGPL-3",
    "application": True,
    "installable": True,
    "sequence": 3,

    "data": [
        # "security/school_security.xml",
        "security/ir.model.access.csv",
        "data/school_sequence.xml",
        "views/school_actions.xml",
        "views/school_menus.xml",
        "views/school_student_views.xml",
        "views/school_teacher_views.xml",
        "views/school_classroom_views.xml",
        "views/school_subject_views.xml",
        "views/school_schedule_views.xml",
        "views/school_class_schedule_views.xml",
        "views/school_teacher_profile_views.xml",
        "views/school_student_health_inherit_views.xml",
        "wizard/student_complaint_view.xml",
        "data/school_cron_jobs.xml",
        # "data/school_student_complaint_email_template.xml"

    ],
    'images': ['static/description/icon.png'],

    'assets': {
        'web.assets_backend': [
            'school/static/src/css/styles.css',
        ],
    }
}
