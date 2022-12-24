
from tesla.router.url import Mount

from tesla.admin.urls import patterns as admin_urls
from doc.urls import patterns

Mount('/admin/', admin_urls, app_name='admin')
Mount('/', patterns, app_name='doc')
