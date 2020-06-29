from driver import driver
from viddyoze import login, render_all_logo_templates, render_template_by_name
import os

login()
render_template_by_name(
    'Water Splash', 'www.plexus.market', 'assets/apple.jpg')
