from rest_framework.views import APIView
from rest_framework.response import Response
from . import models,serializers

class Feed(APIView):

    def get(self, request, format=None):
        
        user = request.user

        following_users = user.following.all()

        image_list = [] # 전체 이미지 리스트


        for following_user in following_users:

            user_images = following_user.images.all()[:2] # 1개로 제한

            for everyimages in user_images: # 전체 이미지 리스트에 다 집어넣음

                image_list.append(everyimages)

        sorted_image_list = sorted(image_list, key = get_key , reverse = True)
        # 이미지 정렬 첫번째 arg는 해당 list 두번재 key는 함수호출 get_key 의 return값으로 호출 
        # get_key 의 arg는 image_list의 object, 세번째 인자는 reverse : 최신순으로 정렬하기위해

        #sorted_image_list = sorted(image_list, key = lanbda x : x.createed_at , reverse = True)
        # 파이썬식 코드

        print(sorted_image_list)

        serializer = serializers.ImageSerializer(sorted_image_list, many = True)

        return Response(serializer.data)

# Create your views here.
def get_key(image):
    return image.created_at

class LikeImage(APIView):
    def get(self , request,image_id, format =None): #post는 나중에 공부


        user = request.user

        try:
            found_image = models.Image.objects.get(id = image_id)
        except models.Image.DoesNotExist:
            return Response(status =404)

        try:
            preexisiting_like =models.Like.objects.create(
                creator = user,
                image = found_image
            )

            preexisiting_like.delete()
        except models.Like.DoesNotExist:
            

        new_like.save()

        return Response(status = 200)
