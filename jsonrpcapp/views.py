import json

from django.shortcuts import render
from .forms import JSONRPCForm
from .jsonrpc_client import JSONRPCClient


def jsonrpc_view(request):
    result = None
    if request.method == 'POST':
        form = JSONRPCForm(request.POST)
        if form.is_valid():
            method = form.cleaned_data['method']
            params = form.cleaned_data['params']
            try:
                params = json.loads(params)
            except json.JSONDecodeError:
                params = {}
            client = JSONRPCClient(endpoint='https://slb.medv.ru/api/v2/')
            result = client.call_method(method, params)
    else:
        form = JSONRPCForm()
    return render(request, 'form.html', {'form': form, 'result': result})
