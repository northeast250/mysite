import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                    'mysite.settings')
import django
django.setup()
from rango.models import Category, Page
def populate():
    python_cat = add_cat('Python', views=128, likes=64)

    add_page(cat=python_cat,
             title="Official Python Tutorial",
             url="http://docs.python.org/2/tutorial/")

    add_page(cat=python_cat,
             title="How to Think like a Computer Scientist",
             url="http://www.greenteapress.com/thinkpython/")

    add_page(cat=python_cat,
             title="Learn Python in 10 Minutes",
             url="http://www.korokithakis.net/tutorials/python/")

    django_cat = add_cat("Django", views=64, likes=32)

    add_page(cat=django_cat,
             title="Official Django Tutorial",
             url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    add_page(cat=django_cat,
             title="Django Rocks",
             url="http://www.djangorocks.com/")

    add_page(cat=django_cat,
             title="How to Tango with Django",
             url="http://www.tangowithdjango.com/")

    frame_cat = add_cat("Other Frameworks", views=32, likes=16)

    add_page(cat=frame_cat,
             title="Bottle",
             url="http://bottlepy.org/docs/dev/")

    add_page(cat=frame_cat,
             title="Flask",
             url="http://flask.pocoo.org")

    #首先创建一些字典，列出想添加到各分类的网页
#然后创建一个嵌套字典，设置各分类
#这么做看起来不易理解，但是便于迭代，方便为模型添加数据
    # python_pages = [
    #     {"title": "Official Python Tutorial",
    #      "url": "http://docs.python.org/2/tutoriall"},
    #     {"title": "How to Think like a Computer Scientist", "url": "http://www.g reenteapress.com/thinkpython/"},
    #     {"title": "Learn Python in 10 Minutes",
    #      "url":"http://www.korokithakis.net/tutorialspython/"}]
    #
    #
    # django_pages=[
    # {"title":"official Django Tutorial",
    # "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
    #     {"title":"Django Rocks",
    # "url":"http://www.djangorocks.com/"},
    # {"title":"How to Tango with Django",
    # "url":"http://www.tangowithdjango.com/"}]
    #
    # other_pages = [
    #     {"title":"Bottle",
    #     "url":"http://bottlepy.org/docs/dev/"}, {"title":"Flask",
    #     "url":"http://flask.pocoo.org"}]
    # cats = {"Python":{"pages": python_pages},
    #     "Django": {"pages": django_pages},
    #     "Other Frameworks": {"pages": other_pages}}
    #
    # for cat, cat_data in cats.items():
    #     c= add_cat(cat)
    #     for p in cat_data["pages"]:
    #         add_page(c,p["title"],p["url"])


#打印添加的分类
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0}-{1}".format(str(c),str(p)))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name,views=views,likes=likes)[0]
    return c

# def add_page(cat, title, url, views=0):
#     p = Page.objects.get_or_create(category=cat, title=title)[0]
#     p.url=url
#     p.views=views
#     p.save()
#     return p
#
# def add_cat(name):
#     c= Category.objects.get_or_create(name=name)[0]
#     c.save()
#     return c


# Start execution here!
if __name__ == '__main__':
    print ("Starting Rango population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
    from rango.models import Category, Page
    populate()





