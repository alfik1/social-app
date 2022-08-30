from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from api.serializers import PostSerializer
from rest_framework.response import Response
from api.models import Posts
# Create your views here.

#view To list all Posts
class PostView(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Posts.objects.all()
        serailizer=PostSerializer(qs,many=True)
        return Response(data=serailizer.data)
#create new Post
    def create(self,request,*args,**kwargs):
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Posts.objects.get(id=id)
        serializer=PostSerializer(qs)
        return Response(data=serializer.data)

    def update(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        instance=Posts.objects.get(id=id)
        serializer=PostSerializer(instance=instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        instance=Posts.objects.get(id=id)
        instance.delete()
        return Response({"message":"Deleted"})
