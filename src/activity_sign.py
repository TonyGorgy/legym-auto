# -*- coding: UTF-8 -*-

import os
import legym_api

username = '15181126466'
password = 'Tt123123'
keyword = os.environ.get('KEYWORD')

user = legym_api.login(username, password)
user.signup_activities(keyword)
user.signin_activities(keyword)
