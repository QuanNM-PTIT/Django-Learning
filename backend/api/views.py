from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerializer


@api_view(['GET', 'POST'])
def api_home(request, *args, **kwargs):
    if request.method == "GET":
        model_data = Product.objects.all().order_by("?").first()
        data = {}
        if model_data:
            # model_to_dict(model_data, fields=["title", "price"])
            data = ProductSerializer(model_data).data
        return Response(data)
    else:
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
