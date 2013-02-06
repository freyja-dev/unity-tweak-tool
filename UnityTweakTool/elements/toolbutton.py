class OverviewToolButton:
    def __init__(self,section,page,id,notebook):
        self.section=section
        self.id=id
        self.page=page
        self.notebook=notebook
    def handler(self,*args,**kwargs):
        self.notebook.get_nth_page(self.section).set_current_page(self.page)
    def register(self,handler):
        handler['on_%s_clicked'%self.id]=self.handler
