from django.shortcuts import render, redirect
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ShortUrl
from .serializers import ShortURLSerialaizer


class ShortUrlView(APIView):
    def get(self, request):
        url = ShortUrl.objects.all()
        context = {
            "Short_URL": url.values(),
        }
        return Response(context)

    def post(self, request):
        url = request.data.get('Short_URL')
        serializer = ShortURLSerialaizer(data=url, many=True)
        if serializer.is_valid(raise_exception=True):
            try:
                exist_url = ShortUrl.objects.get(url=url[0]['url'])
                context = {
                    "error": f'Url {exist_url.short_url} already exist',
                }
                return Response(context)
            except:
                url_save = serializer.save()
                context = {
                    "success": f'Url {url_save[0]} created successfully',
                }
                return Response(context)

    def put(self, request):
        data = request.data.get('Short_URL')
        short = data[0]['short_url']
        saved_url = get_object_or_404(ShortUrl.objects.all(), short_url=short)
        serializer = ShortURLSerialaizer(instance=saved_url, data=data[0], partial=True)
        if serializer.is_valid(raise_exception=True):
            url_saved = serializer.save()
        return Response({
            "success": f"Url '{url_saved}' updated successfully",
        })

    def delete(self, request, format=None):
        data = request.data.get('Short_URL')
        short = data[0]['short_url']
        saved_url = get_object_or_404(ShortUrl.objects.all(), short_url=short)
        context = {
            "success": f'Url {saved_url.url} delete',
        }
        saved_url.delete()
        return Response(context)


def RedirectView(request, short_url):
    url = ShortUrl.objects.get(short_url=short_url)
    return redirect(url.url)
