from netwizard.widgets.layout import dock, widget


layout = {
        '':
     (
            dock('Header', (
                widget('StaticHtml', value='Webwizard-CMS'),
                )
            ),
            dock('Sidebar', (
                widget('Menu', value='MAIN', id='TopMenu'),
                widget('Menu'),
                )
            ),
            dock('Content', (
                widget('MainContent'),
                )
            ),
            dock('Footer', (
                widget('StaticHtml', value='Copyright (c) 2009 netwizard.pl'),
	            )
	        ),
    ),
}
