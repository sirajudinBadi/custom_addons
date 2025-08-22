{
    "name" : "Custom Web",
    "description" : "Custom Website for practice purpose.",
    "summary" : """This module will act as the custom website for Backend Exercise Purpose.""",
    "author" : "John Doe",
    "license" : "LGPL-3",
    "version" : "18.0.0.1",
    "application" : False,
    "installable" : True,
    "depends" : ["base","website","crm"],
    "website" : "www.example.com",
    "data" : [
        "views/custom_web_menus.xml",
        "views/crm_lead_list_template.xml",
        "views/crm_lead_form_template.xml",
        "views/crm_lead_edit_template.xml",

    ],
    "sequence" : "6"
}