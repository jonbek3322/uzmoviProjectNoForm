from django.shortcuts import redirect, render
from django.http.response import HttpResponse, Http404
from movie.models import Movie


def movies_list(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movie_list.html', context)


def movie_detail(request, movie_id):
    if request.method == 'POST':
       redirect('')

    try:
        movie = Movie.objects.get(id=movie_id) # get(title='')
    except Exception as e:
        print(e)
        raise Http404('Bunday sahifa topilmadi')

    context = {
        'movie': movie,
    }
    return render(request, 'movie_detail.html', context)


def movie_edit(request, movie_id):

    try:
        movie = Movie.objects.get(id=movie_id) # get(title='')

        # print(Movie.objects.post(id=movie_id))
    except Exception as e:
        print(e)
        raise Http404('Bunday sahifa topilmadi')

    context = {
        'movie': movie,
                    }
    return render(request, 'movie_edit.html', context)

    # errors = {}
    # data = {}
    # context = {}
    # if request.method == 'GET':
    #     context = {
    #     'movie': movie,
    #                 }
    #     return render(request, 'movie_edit.html', context)
    # elif request.method == 'POST': # data = reuqest.POST : dict
    #     print(request.POST) # <QueryDict: {'title': ['asdasd'], 'released_year': ['234234'], 'language': ['english'], 'duration': [''], 'source_link': [''], 'type': ['SERIES'], 'csrfmiddlewaretoken': ['LJKe3tJW3HrWrJlf8FPrcC0P9BL5j8jujtxoQmD1McLn8guWniqx4SGq7KlBMV4F'], 'banner': [''], 'slug': ['fantastika']}>
    #     title = request.POST.get('title') # 'asdasd'
    #         # return render
    #     released_year = request.POST.get('released_year')
    #     lang = request.POST['language']
    #     duration = request.POST['duration']
    #     sourse_link = request.POST['source_link']
    #     type = request.POST['type']
    #     banner = request.POST['banner']
    #     slug = request.POST.get('slug')
        
    #     new_movie = Movie(title=title, banner=banner, language=lang, duration=duration, sourse_link=sourse_link, type=type, slug=slug)
    #     if not title:
    #         errors['title'] = 'Please enter a Nomi!'
    #     if not sourse_link:
    #         errors['source_link'] = 'Please enter a Link'
    #     if type not in  ['MOVIE', 'TRAILER', 'SHOW', 'SERIES']:
    #         errors['type'] = '''You entered the wrong format type
    #                             Please enter the type correctly'''
    #     if not slug:
    #         errors['slug'] = 'Please enter a slug'
    #     # slug = 'asdkjaskdasd'
    #     # new_movie.slug = slug
    #     if released_year:
    #         new_movie.released_year = released_year
        
    #     if len(errors) == 0:
    #         new_movie.save()    
    #         return redirect("/''/")
    #     else:
    #         data = {
    #         'title': title,
    #         'released_year': released_year,
    #         'language': lang,
    #         'duration': duration,
    #         'sourse_link': sourse_link,
    #         'type': type,
    #         'banner': banner,
    #         'slug': slug
    #     }
    #     # new_movie = Movie.objects.create(
    #     #     title=title, released_year=released_year, language=lang,
    #     #     duration=duration, source_link=source_link, type=type
    #     # )
    #     context['errors'] = errors,
    #     context['data']=data
    # return render(request, 'movie_create.html', context)
        
    # try:
    #     movie = Movie.objects.get(id=movie_id) # get(title='')

    #     # print(Movie.objects.post(id=movie_id))
    # except Exception as e:
    #     print(e)
    #     raise Http404('Bunday sahifa topilmadi')

    # context = {
    #     'movie': movie,
    # }
    # return render(request, 'movie_edit.html', context)


def movie_create(request):
    print(f"============{request.method}============")
    # request.GET
    errors = {}
    data = {}
    context = {}
    if request.method == 'POST': # data = reuqest.POST : dict
        print(request.POST) # <QueryDict: {'title': ['asdasd'], 'released_year': ['234234'], 'language': ['english'], 'duration': [''], 'source_link': [''], 'type': ['SERIES'], 'csrfmiddlewaretoken': ['LJKe3tJW3HrWrJlf8FPrcC0P9BL5j8jujtxoQmD1McLn8guWniqx4SGq7KlBMV4F'], 'banner': [''], 'slug': ['fantastika']}>
        title = request.POST['title'] # 'asdasd'
            # return render
        released_year = request.POST['released_year']
        lang = request.POST['language']
        duration = request.POST['duration']
        sourse_link = request.POST['source_link']
        type = request.POST['type']
        banner = request.POST['banner']
        slug = request.POST.get('slug')
        
        new_movie = Movie(title=title, banner=banner, language=lang, duration=duration, sourse_link=sourse_link, type=type, slug=slug)
        if not title:
            errors['title'] = 'Please enter a Nomi!'
        if not sourse_link:
            errors['source_link'] = 'Please enter a Link'
        if type not in  ['MOVIE', 'TRAILER', 'SHOW', 'SERIES']:
            errors['type'] = '''You entered the wrong format type
                                Please enter the type correctly'''
        if not slug:
            errors['slug'] = 'Please enter a slug'
        # slug = 'asdkjaskdasd'
        # new_movie.slug = slug
        if released_year:
            new_movie.released_year = released_year
        
        if len(errors) == 0:
            new_movie.save()    
            return redirect("/''/")
        else:
            data = {
            'title': title,
            'released_year': released_year,
            'language': lang,
            'duration': duration,
            'sourse_link': sourse_link,
            'type': type,
            'banner': banner,
            'slug': slug
        }
        # new_movie = Movie.objects.create(
        #     title=title, released_year=released_year, language=lang,
        #     duration=duration, source_link=source_link, type=type
        # )
        context['errors'] = errors,
        context['data']=data
    return render(request, 'movie_create.html', context)