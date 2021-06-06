from menu import Menu, MenuItem
from django.utils.translation import gettext_lazy as _
from django.utils.text import capfirst
# from django.core.urlresolvers import reverse

def community_children(request):
    children = []
    children.append (MenuItem(
         capfirst(_("the CommonS project")),
         url='/info/about/',
        ))
    children.append (MenuItem(
         capfirst(_("press releases")),
         url='/press_releases/',
        ))
    children.append (MenuItem(
         capfirst(_("blog")),
         url='/weblog/',
        ))
    children.append (MenuItem(
         capfirst(_("the platform")),
         url='/info/platform/',
         ))
    return children

def projects_children(request):
    children = []
    children.append (MenuItem(
         capfirst(_("all communities")),
         url='/cops/',
        ))
    children.append (MenuItem(
         capfirst(_("browse mentors")),
         url='/browse_mentors/',
    ))
    children.append (MenuItem(
         capfirst(_("projects")),
         url='/projects/search',
        ))
    """
    children.append (MenuItem(
         capfirst(_("top contributors")),
         url='/resources/contributors/',
        ))
    """
    children.append (MenuItem(
         capfirst(_("forums")),
         url='/forum/',
        ))
    children.append (MenuItem(
         capfirst(_("browse people")),
         url='/browse_people/',
        ))
    children.append (MenuItem(
         capfirst(_("search people")),
         url='/people/search/',
        ))
    return children

def search_children(request):
    user = request.user
    children = []
    children.append (MenuItem(
         capfirst(_("all resources")),
         # url='/repos/',
         url='/browse/',
        ))
    children.append (MenuItem(
         capfirst(_("learning paths")),
         url='/lps/search/',
        ))
    children.append (MenuItem(
         capfirst(_("open resources")),
         url='/oers/search/',
        ))
    children.append (MenuItem(
         capfirst(_("source repositories")),
         url='/repos/search/',
        ))
    return children

def my_children(request):
    children = []
    children.append (MenuItem(
         capfirst(_("my projects")),
         url='/my_projects/',
        ))
    children.append (MenuItem(
         capfirst(_("my contents")),
         url='/my_contents/',
        ))
    children.append (MenuItem(
         capfirst(_("my activity")),
         url='/my_activity/',
        ))
    return children

def help_children(request):
    children = []
    children.append (MenuItem(
         capfirst(_("tutorials")),
         url='/help/tutorials/',
        ))
    children.append (MenuItem(
         capfirst(_("registration and authentication")),
         url='/help/register/',
        ))
    children.append (MenuItem(
         capfirst(_("user profile and user roles")),
         url='/help/profile/',
        ))
    children.append (MenuItem(
         capfirst(_("site navigation")),
         url='/help/navigation/',
        ))
    children.append (MenuItem(
         capfirst(_("communities and projects")),
         url='/help/community/',
        ))
    children.append (MenuItem(
         capfirst(_("searching the catalogued resources")),
         url='/help/search/',
        ))
    children.append (MenuItem(
         capfirst(_("open resources")),
         url='/help/oer/',
        ))
    children.append (MenuItem(
         capfirst(_("learning paths")),
         url='/help/lp/',
        ))
    children.append (MenuItem(
         capfirst(_("mentoring")),
         url='/help/mentoring/',
        ))
    children.append (MenuItem(
         capfirst(_("analytics")),
         url='/help/analytics/',
        ))
    children.append (MenuItem(
         capfirst(_("internationalization")),
         url='/info/i18n/',
        ))
    children.append (MenuItem(
         capfirst(_("translation")),
         url='/info/translation/',
        ))
    children.append (MenuItem(
         capfirst(_("content evaluation")),
         url='/help/evaluation/',
        ))
    children.append (MenuItem(
         capfirst(_("editorial tools")),
         url='/help/editorial/',
        ))
    return children

def admin_children(request):
    children = []
    user = request.user
    # if user.is_superuser or (user.is_authenticated() and user.is_community_manager()):
    if user.is_superuser or (user.is_authenticated and user.is_manager(1)):
        children.append (MenuItem(
             capfirst(_("activity stream")),
             url='/analytics/activity_stream/',
            ))
        children.append (MenuItem(
             capfirst(_("forums")),
             url='/analytics/forums/',
            ))
        children.append (MenuItem(
             capfirst(_("messages")),
             url='/analytics/messages/',
            ))
    return children


Menu.items = {}
Menu.sorted = {}

# Add a few items to our main menu
Menu.add_item("main", MenuItem(capfirst(_("about")),
                               url='/p',
                               weight=30,
                               check=True,
                               children=community_children,
                               separator=True))
Menu.add_item("main", MenuItem(capfirst(_("communities")),
                               url='/p',
                               weight=30,
                               check=True,
                               children=projects_children,
                               separator=True))     
Menu.add_item("main", MenuItem(capfirst(_("library")),
                               url='/p',
                               weight=30,
                               check=True,
                               children=search_children,
                               separator=True))
Menu.add_item("main", MenuItem(capfirst(_("my spaces")),
                               url='/p',
                               weight=30,
                               check=lambda request: request.user.is_authenticated and request.user.is_full_member(),
                               children=my_children,
                               separator=True))
Menu.add_item("main", MenuItem(capfirst(_("help")),
                               url='/p',
                               weight=30,
                               check=True,
                               children=help_children,
                               separator=True))
