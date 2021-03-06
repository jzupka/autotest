from django.conf.urls import defaults
try:
    import autotest.common as common
except ImportError:
    import common
from autotest_lib.frontend import settings, urls_common
from autotest_lib.frontend.tko import resources

urlpatterns, debug_patterns = (
        urls_common.generate_patterns('frontend.tko', 'TkoClient'))

resource_patterns = defaults.patterns(
        '',
        (r'^/?$', resources.ResourceDirectory.dispatch_request),
        (r'^test_results/?$', resources.TestResultCollection.dispatch_request),
        (r'^test_results/(?P<test_id>\d+)/?$',
         resources.TestResult.dispatch_request),
        )

urlpatterns += defaults.patterns(
        '',
        (r'^jsonp_rpc/', 'frontend.tko.views.handle_jsonp_rpc'),
        (r'^csv/', 'frontend.tko.views.handle_csv'),
        (r'^plot/', 'frontend.tko.views.handle_plot'),

        (r'^resources/', defaults.include(resource_patterns)))

if settings.DEBUG:
    urlpatterns += debug_patterns
