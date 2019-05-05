from django.http import HttpResponse
class SimpleMiddelWare:
    def __init__(self, get_res):
        self.get_response = get_res

    def __call__(self, request):
        res = self.get_response(request)

        # res = HttpResponse("中间件更改输出")
        return res

    # 其他中间件函数  名字必特定
    def process_view(self,request, view_func, view_args, view_kwargs):
        print(request, view_func, view_args, view_kwargs, '视图信息')