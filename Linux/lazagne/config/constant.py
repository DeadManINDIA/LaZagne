#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import time

date = time.strftime("%d%m%Y_%H%M%S")


class constant():
    folder_name         = 'results_{current_time}'.format(current_time=date)
    file_name_results   = 'credentials'  # The extension is added depending on the user output choice
    max_help   = 27
    CURRENT_VERSION     = '2.4.3'
    output              = None
    file_logger         = None
    verbose             = False
    nb_password_found     = 0  # Total password found
    password_found       = []
    stdout_result       = [] # Tab containing all results by user
    finalResults        = {}
    quiet_mode          = False
    st                  = None  # Standard output
    modules_dic         = {}
    chrome_storage      = [] # Retrieved from libsecrets module
    chrome_dirs         = [
     u'.config/google-chrome',
     u'.config/chromium',
     u'.config/BraveSoftware/Brave-Browser'
    ]
