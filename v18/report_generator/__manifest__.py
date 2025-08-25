{
    "name" : "Report Generator",
    "description" : "Custom PDF Report Generator.",
    "summary" : """This module will generate custom QWeb Reports.""",
    "installable" : True,
    "application" : True,
    "depends" : ["base", "web", "sale",],
    "license" : "LGPL-3",
    "version" : "18.0.0.1",
    "data" : [
        "report_customer_action.xml",
        "views/res_partner_menus.xml",
    ],
}