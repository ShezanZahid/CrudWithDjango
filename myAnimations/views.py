
from django.http.response import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Comment, MyAnimations
from .form import CommentCreateForm, MyAnimationCreateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models import Profile
from users.deocrators import allowed_users
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    animation_list=MyAnimations.objects.filter(status="Approved")
    usergroupList= request.user.groups.values_list('name',flat=True)
    groupexists= usergroupList.filter(name='Admin').exists()
    context={
        'animation_list':animation_list,
        'groupexists':groupexists,
    }
  
    return render(request,'myAnimations/index.html',context)

@login_required
def selfindex(request):
    if hasattr(request.user,'profile'):
        animation_list=MyAnimations.objects.filter(animation_user=request.user.profile.id)
        context={
            'animation_list':animation_list,
        }
        return render(request,'myAnimations/selfindex.html',context)
        
    else:
        messages.info(request,f'{request.user.username},Please create Profile before adding content')
        return redirect('profile')
        

def details(request,item_id):
    item=get_object_or_404(MyAnimations,id=item_id)
    comments = item.comment_post.filter(status=True)
    usergroupList= request.user.groups.values_list('name',flat=True)
    groupexists= usergroupList.filter(name='Admin').exists()
    user_comment = None
    print(request.user.post_user.values())
    if request.method == 'POST':
        comment_form = CommentCreateForm(request.POST)
        if comment_form.is_valid:
            user_comment = comment_form.save(commit=False)
            user_comment.post = item
            user_comment.user = request.user
            user_comment.save()
            return HttpResponseRedirect(reverse('details', args=(item.id,)))
    else:
        comment_form = CommentCreateForm()
    context={
        'item':item,
        'groupexists':groupexists,
        'comments':user_comment,
        'comments':comments,
        'comment_form':comment_form,
    }
    
    return render(request,'myAnimations/details.html',context)


@login_required
@csrf_exempt
def like(request):
    if request.POST.get('action')=='post':
        result=""
        id=int(request.POST.get('postid'))
        post=get_object_or_404(MyAnimations,id=id)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            post.like_count -=1 
            result=post.like_count
            post.save()
        else:
            post.likes.add(request.user)
            post.like_count +=1 
            result=post.like_count
            post.save()
        
        return JsonResponse({'result':result,})

    
@login_required    
def create(request):
    if request.method == 'POST':
        form=MyAnimationCreateForm(request.POST, request.FILES)
        current_profile=Profile.objects.get(user=request.user.id)
       
        if form.is_valid():
            instance = form.save(commit=False)
            instance.animation_user=current_profile
            form.save()
            animation_name = form.cleaned_data.get('animation_name')
            messages.success(request,f'{animation_name} Content Successfully Created')
            return redirect('selfindex')
    else:
        form=MyAnimationCreateForm()
        return render(request,'myAnimations/create.html',{'form':form})
@login_required
def update(request,id):
    item=MyAnimations.objects.get(id=id)
    if request.method == 'POST':
        form = MyAnimationCreateForm(request.POST,request.FILES,instance=item)

        if form.is_valid():
            item.status = 'Pending'
            form.save()
            animation_name = form.cleaned_data.get('animation_name')
            messages.success(request,f'{animation_name} Content Successfully Created')
            
            return redirect('selfindex')
    else:
        form = MyAnimationCreateForm(request.POST or None,instance=item)
        return render(request,'myAnimations/create.html',{'form':form,'item':item}) 
@login_required
def delete(request,id):
    item = MyAnimations.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('selfindex')

    return render(request,'myAnimations/delete.html',{'item':item})

@login_required
def allindex(request):
    usergroupList= request.user.groups.values_list('name',flat=True)
    groupexists= usergroupList.filter(name='Admin').exists()
    animation_list=MyAnimations.objects.filter(status="Approved")
    context={
        'animation_list':animation_list,
        'groupexists':groupexists,
    }
    return render(request,'myAnimations/allindex.html',context)



@login_required
# @allowed_users(allowed_roles=['Customer'])
@allowed_users(allowed_roles=['Admin'])
def post_approval_list(request):
    usergroupList= request.user.groups.values_list('name',flat=True)
    groupexists= usergroupList.filter(name='Admin').exists()
    animation_list=MyAnimations.objects.filter(status="Pending")
    context={
        'animation_list':animation_list,
        'groupexists':groupexists,
    }
    return render(request,'myAnimations/allindex.html',context)

@allowed_users(allowed_roles=['Admin'])
def post_approved_list(request):
    usergroupList= request.user.groups.values_list('name',flat=True)
    groupexists= usergroupList.filter(name='Admin').exists()
    animation_list=MyAnimations.objects.filter(status="Approved")
    context={
        'animation_list':animation_list,
        'groupexists':groupexists,
    }
    return render(request,'myAnimations/allindex.html',context)

@allowed_users(allowed_roles=['Admin'])
def post_rejected_list(request):
    animation_list=MyAnimations.objects.filter(status="Rejected")
    usergroupList= request.user.groups.values_list('name',flat=True)
    groupexists= usergroupList.filter(name='Admin').exists()
   
    context={
        'animation_list':animation_list,
        'groupexists':groupexists,
    }
    return render(request,'myAnimations/allindex.html',context)    
@allowed_users(allowed_roles=['Admin'])
def approve_post(request,id):
    item=MyAnimations.objects.get(id=id)
    item.status = 'Approved'
    item.save()
    context={
        'item':item,
    }
    
    return redirect('post_approval_list')

@allowed_users(allowed_roles=['Admin'])
def reject_post(request,id):
    item=MyAnimations.objects.get(id=id)
    item.status = 'Rejected'
    print(item)
    item.save()
    context={
        'item':item,
    }
    
    return redirect('post_approval_list')



