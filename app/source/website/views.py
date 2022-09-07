from django.views.generic import TemplateView

class IndexView(TemplateView):
	template_name = "index.html"

	def get_context_data(self):
		ctxt = super().get_context_data()
		ctxt["username"]="太郎"
		return ctxt


class AboutView(TemplateView):
	template_name = "about.html"

	def get_context_data(self):
		ctxt = super().get_context_data()
		ctxt["worked_company"]="ネクサスエージェント"
		ctxt["worked_num"]=123456
		ctxt["skills"]=[
			"Python",
			"C",
			"Java",
			"SQL",
		]
		return ctxt