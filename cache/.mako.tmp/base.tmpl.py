# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1414693844.737832
_enable_loop = True
_template_filename = u'/Users/talos/.virtualenvs/nikola/lib/python2.7/site-packages/nikola/data/themes/bootstrap3/templates/base.tmpl'
_template_uri = u'base.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'sourcelink', u'extra_js', u'belowtitle']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'notes', context._clean_inheritance_tokens(), templateuri=u'annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'notes')] = ns

    ns = runtime.TemplateNamespace(u'base', context._clean_inheritance_tokens(), templateuri=u'base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        show_sourcelink = _import_ns.get('show_sourcelink', context.get('show_sourcelink', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        annotations = _import_ns.get('annotations', context.get('annotations', UNDEFINED))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        def belowtitle():
            return render_belowtitle(context._locals(__M_locals))
        notes = _mako_get_namespace(context, 'notes')
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(unicode(set_locale(lang)))
        __M_writer(u'\n')
        __M_writer(unicode(base.html_headstart()))
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer(u'\n')
        __M_writer(unicode(template_hooks['extra_head']()))
        __M_writer(u'\n</head>\n<body>\n<a href="#content" class="sr-only sr-only-focusable">')
        __M_writer(unicode(messages("Skip to main content")))
        __M_writer(u'</a>\n\n<!-- Menubar -->\n\n<nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">\n    <div class="container"><!-- This keeps the margins nice -->\n        <div class="navbar-header">\n            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">\n            <span class="sr-only">Toggle navigation</span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            </button>\n            <a class="navbar-brand" href="')
        __M_writer(unicode(abs_link('/')))
        __M_writer(u'">\n')
        if logo_url:
            __M_writer(u'                <img src="')
            __M_writer(unicode(logo_url))
            __M_writer(u'" alt="')
            __M_writer(unicode(blog_title))
            __M_writer(u'" id="logo">\n')
        __M_writer(u'\n')
        if show_blog_title:
            __M_writer(u'                <span id="blog-title">')
            __M_writer(unicode(blog_title))
            __M_writer(u'</span>\n')
        __M_writer(u'            </a>\n        </div><!-- /.navbar-header -->\n        <div class="collapse navbar-collapse navbar-ex1-collapse">\n            <ul class="nav navbar-nav">\n                ')
        __M_writer(unicode(base.html_navigation_links()))
        __M_writer(u'\n                ')
        __M_writer(unicode(template_hooks['menu']()))
        __M_writer(u'\n            </ul>\n')
        if search_form:
            __M_writer(u'                ')
            __M_writer(unicode(search_form))
            __M_writer(u'\n')
        __M_writer(u'\n            <ul class="nav navbar-nav navbar-right">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'belowtitle'):
            context['self'].belowtitle(**pageargs)
        

        __M_writer(u'\n')
        if show_sourcelink:
            __M_writer(u'                    ')
            if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
                context['self'].sourcelink(**pageargs)
            

            __M_writer(u'\n')
        __M_writer(u'                ')
        __M_writer(unicode(template_hooks['menu_alt']()))
        __M_writer(u'\n            </ul>\n        </div><!-- /.navbar-collapse -->\n    </div><!-- /.container -->\n</nav>\n\n<!-- End of Menubar -->\n\n<div class="container" id="content">\n    <div class="body-content">\n        <!--Body content-->\n        <div class="row">\n            ')
        __M_writer(unicode(template_hooks['page_header']()))
        __M_writer(u'\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n        </div>\n        <!--End of body content-->\n\n        <footer>\n            ')
        __M_writer(unicode(content_footer))
        __M_writer(u'\n            ')
        __M_writer(unicode(template_hooks['page_footer']()))
        __M_writer(u'\n        </footer>\n    </div>\n</div>\n\n')
        __M_writer(unicode(base.late_load_js()))
        __M_writer(u'\n    <script>jQuery("a.image-reference").colorbox({rel:"gal",maxWidth:"100%",maxHeight:"100%",scalePhotos:true});</script>\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer(u'\n')
        if annotations and post and not post.meta('noannotations'):
            __M_writer(u'        ')
            __M_writer(unicode(notes.code()))
            __M_writer(u'\n')
        elif not annotations and post and post.meta('annotations'):
            __M_writer(u'        ')
            __M_writer(unicode(notes.code()))
            __M_writer(u'\n')
        __M_writer(unicode(body_end))
        __M_writer(u'\n')
        __M_writer(unicode(template_hooks['body_end']()))
        __M_writer(u'\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_belowtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def belowtitle():
            return render_belowtitle(context)
        base = _mako_get_namespace(context, 'base')
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        if len(translations) > 1:
            __M_writer(u'                    <li>')
            __M_writer(unicode(base.html_translations()))
            __M_writer(u'</li>\n')
        __M_writer(u'                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 77, "129": 77, "224": 47, "226": 49, "134": 79, "135": 80, "136": 81, "137": 81, "138": 81, "139": 82, "140": 83, "141": 83, "142": 83, "143": 85, "144": 85, "145": 86, "146": 86, "195": 79, "22": 3, "152": 66, "25": 2, "28": 0, "166": 6, "223": 47, "175": 6, "181": 51, "221": 45, "64": 2, "65": 3, "66": 4, "67": 4, "68": 5, "69": 5, "225": 47, "74": 8, "75": 9, "76": 9, "77": 12, "78": 12, "79": 25, "80": 25, "81": 26, "82": 27, "83": 27, "84": 27, "85": 27, "86": 27, "87": 29, "88": 30, "89": 31, "90": 31, "91": 31, "92": 33, "93": 37, "94": 37, "95": 38, "96": 38, "97": 40, "98": 41, "99": 41, "100": 41, "101": 43, "209": 45, "232": 226, "106": 49, "107": 50, "108": 51, "222": 46, "113": 51, "114": 53, "115": 53, "116": 53, "117": 65, "118": 65, "123": 66, "124": 71, "125": 71, "126": 72, "127": 72}, "uri": "base.tmpl", "filename": "/Users/talos/.virtualenvs/nikola/lib/python2.7/site-packages/nikola/data/themes/bootstrap3/templates/base.tmpl"}
__M_END_METADATA
"""
