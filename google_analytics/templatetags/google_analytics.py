# Based on https://djangosnippets.org/snippets/1656/
from django import template
from django.conf import settings

register = template.Library()


class ShowGoogleAnalyticsJS(template.Node):
    def render(self, context):
        # Get GOOGLE ANALYTICS CODE
        code = getattr(settings, "GOOGLE_ANALYTICS_CODE", False)
        if code and not settings.DEBUG:
            return """
                <script>
                  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
                  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
                  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
                  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

                  ga('create', '"""+code+"""', 'auto');
                  ga('send', 'pageview');

                </script>
                """
        else:
            if settings.DEBUG:
                return "<!-- Google Analytics doesnt load in Debug Mode -->"
            elif not code:
                return "<!-- Doesnt provide code for Google Analytics -->"


def googleanalytics(parser, token):
    return ShowGoogleAnalyticsJS()

show_common_data = register.tag(googleanalytics)