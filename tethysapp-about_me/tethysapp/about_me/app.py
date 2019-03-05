from tethys_sdk.base import TethysAppBase, url_map_maker


class AboutMe(TethysAppBase):
    """
    Tethys app class for An App About Me.
    """

    name = 'An App About Me'
    index = 'about_me:home'
    icon = 'about_me/images/icon.gif'
    package = 'about_me'
    root_url = 'about-me'
    color = '#e6b3ff'
    description = 'An app about Emily Andrus'
    tags = '&quot;learning&quot;,&quot;about&quot;,&quot;new&quot;'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='about-me',
                controller='about_me.controllers.home'
            ),
        )

        return url_maps
