
from tesla.router.url import Mount

from tesla.admin.urls import patterns as admin_urls
from doc.urls import patterns
from portfolio.urls import patterns as urls
Mount('/admin/', admin_urls, app_name='admin')
Mount('/me', urls, app_name='me')
Mount('/', patterns, app_name='doc')
