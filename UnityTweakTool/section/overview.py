from UnityTweakTool.section.skeletonpage import Section,Tab
from UnityTweakTool.elements.toolbutton import OverviewToolButton

class Overview(Tab,Section):
    def __init__(self,notebook):
        Section.__init__(self,ui='startpage.ui',id='box_startpage')
        self.sections={
            1:{ 0:'tool_launcher',
                1:'tool_dash',
                2:'tool_panel',
                3:'tool_unity_switcher',
                4:'tool_unity_webapps',
                5:'tool_additional'},
            2:{ 0:'tool_general',
                1:'tool_compiz_switcher',
                2:'tool_windows_spread',
                3:'tool_windows_snapping',
                4:'tool_hotcorners',
                5:'tool_wm_additional'},
            3:{ 0:'tool_system',
                1:'tool_icons',
                2:'tool_cursors',
                3:'tool_fonts',
                4:'tool_window_controls'},
            4:{ 0:'tool_desktop_icons',
                1:'tool_desktop_security',
                2:'tool_desktop_scrolling'}
        }

        Tab.__init__(self,[OverviewToolButton(
                            section=section,page=page,id=id,notebook=notebook)
                    for section,set in self.sections.items()
                        for page,id in set.items()
            ]
        )

        self.register_tab(self.handler)
        self.register()
