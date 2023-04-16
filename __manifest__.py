# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################
{
  "name"                 :  "Website Date-Of-Birth On Signup Form",
  "summary"              :  "Odoo Website Date-Of-Birth On Signup Form adds a mandatory field for users to share their date of birth during the sign up.",
  "category"             :  "Website",
  "version"              :  "1.0.0",
  "sequence"             :  1,
  "author"               :  "Webkul Software Pvt. Ltd.",
  "license"              :  "Other proprietary",
  "website"              :  "https://store.webkul.com/Odoo.html",
  "description"          :  """Odoo Website Date-Of-Birth On Signup Form
Website Date-Of-Birth On Signup Form
Date-Of-Birth On Signup Form in Odoo Website
Date of birth on signup form
Enter DOB on Signup form
Add Date of birth option
Add DOB in Sign up form""",
  "live_test_url"        :  "http://odoodemo.webkul.com/?module=account_sign_up_details",
  "depends"              :  [
                             'auth_signup',
                             'website',
                            ],
  "data"                 :  [
                             'views/res_partner_view.xml',
                             'views/account_details_template.xml',
                            ],
  "images"               :  ['static/description/Banner.png'],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
}