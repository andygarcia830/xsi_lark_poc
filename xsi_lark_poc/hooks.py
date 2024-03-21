app_name = "xsi_lark_poc"
app_title = "XSI Lark PoC"
app_publisher = "XSI"
app_description = "XSI Lark PoC"
app_email = "andy@xurpas.cpm"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/xsi_lark_poc/css/xsi_lark_poc.css"
# app_include_js = "/assets/xsi_lark_poc/js/xsi_lark_poc.js"

# include js, css files in header of web template
# web_include_css = "/assets/xsi_lark_poc/css/xsi_lark_poc.css"
# web_include_js = "/assets/xsi_lark_poc/js/xsi_lark_poc.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "xsi_lark_poc/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "xsi_lark_poc/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "xsi_lark_poc.utils.jinja_methods",
# 	"filters": "xsi_lark_poc.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "xsi_lark_poc.install.before_install"
# after_install = "xsi_lark_poc.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "xsi_lark_poc.uninstall.before_uninstall"
# after_uninstall = "xsi_lark_poc.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "xsi_lark_poc.utils.before_app_install"
# after_app_install = "xsi_lark_poc.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "xsi_lark_poc.utils.before_app_uninstall"
# after_app_uninstall = "xsi_lark_poc.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "xsi_lark_poc.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"xsi_lark_poc.tasks.all"
# 	],
# 	"daily": [
# 		"xsi_lark_poc.tasks.daily"
# 	],
# 	"hourly": [
# 		"xsi_lark_poc.tasks.hourly"
# 	],
# 	"weekly": [
# 		"xsi_lark_poc.tasks.weekly"
# 	],
# 	"monthly": [
# 		"xsi_lark_poc.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "xsi_lark_poc.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "xsi_lark_poc.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "xsi_lark_poc.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["xsi_lark_poc.utils.before_request"]
# after_request = ["xsi_lark_poc.utils.after_request"]

# Job Events
# ----------
# before_job = ["xsi_lark_poc.utils.before_job"]
# after_job = ["xsi_lark_poc.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"xsi_lark_poc.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

fixtures = [{"doctype": "Client Script", "filters": [["module" , "in" , ("XSI Lark PoC" )]]}]