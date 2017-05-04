from django.shortcuts import render,HttpResponse
from app01.models import MyUser
from django.contrib.auth.models import Group

# Create your views here.


def index(request):
    # user = MyUser.objects.get(username='admin')
    # # print user.get_group_permissions()
    # # print user
    # user_permissions = request.user.user_permissions.all()
    # for p in user_permissions:
    #     print p
    #
    #
    # group_permissions = request.user.get_group_permissions()
    # for p in group_permissions:
    #     print p
    # current_group_set = Group.objects.get(user=user)
    # print current_group_set.get_group_permissions.all
    # print user.groups,2222
    # print user.get_all_permissions()
    # print user.has_perm('app01.access_log')
    # from django.contrib.auth import authenticate
    # user = authenticate(username='admin', password='rootroot')
    # # print user.groups.all()
    # print user.get_all_permissions()
    # print user.has_perm('admin.delete_logentry')
    user = request.user
    print user.get_group_permissions()
    print user.get_all_permissions()
    # print user.groups.all()[0].url
    # print user.groups.all()[0].detail
    return HttpResponse("app01 index")
