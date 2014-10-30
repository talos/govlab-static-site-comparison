# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1414693845.033124
_enable_loop = True
_template_filename = u'/Users/talos/.virtualenvs/nikola/lib/python2.7/site-packages/nikola/data/themes/base/templates/post_helper.tmpl'
_template_uri = u'post_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_tags', 'html_pager', 'twitter_card_information', 'meta_translations', 'mathjax_script', 'open_graph_metadata']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_tags(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if post.tags:
            __M_writer(u'        <ul itemprop="keywords" class="tags">\n')
            for tag in post.tags:
                __M_writer(u'           <li><a class="tag p-category" href="')
                __M_writer(unicode(_link('tag', tag)))
                __M_writer(u'" rel="tag">')
                __M_writer(unicode(tag))
                __M_writer(u'</a></li>\n')
            __M_writer(u'        </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_pager(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if post.prev_post or post.next_post:
            __M_writer(u'        <ul class="pager">\n')
            if post.prev_post:
                __M_writer(u'            <li class="previous">\n                <a href="')
                __M_writer(unicode(post.prev_post.permalink()))
                __M_writer(u'" rel="prev" title="')
                __M_writer(unicode(post.prev_post.title()))
                __M_writer(u'">')
                __M_writer(unicode(messages("Previous post")))
                __M_writer(u'</a>\n            </li>\n')
            if post.next_post:
                __M_writer(u'            <li class="next">\n                <a href="')
                __M_writer(unicode(post.next_post.permalink()))
                __M_writer(u'" rel="next" title="')
                __M_writer(unicode(post.next_post.title()))
                __M_writer(u'">')
                __M_writer(unicode(messages("Next post")))
                __M_writer(u'</a>\n            </li>\n')
            __M_writer(u'        </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_twitter_card_information(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        twitter_card = context.get('twitter_card', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if twitter_card and twitter_card['use_twitter_cards']:
            __M_writer(u'    <meta name="twitter:card" content="')
            __M_writer(filters.html_escape(unicode(twitter_card.get('card', 'summary'))))
            __M_writer(u'">\n')
            if 'site:id' in twitter_card:
                __M_writer(u'    <meta name="twitter:site:id" content="')
                __M_writer(unicode(twitter_card['site:id']))
                __M_writer(u'">\n')
            elif 'site' in twitter_card:
                __M_writer(u'    <meta name="twitter:site" content="')
                __M_writer(unicode(twitter_card['site']))
                __M_writer(u'">\n')
            if 'creator:id' in twitter_card:
                __M_writer(u'    <meta name="twitter:creator:id" content="')
                __M_writer(unicode(twitter_card['creator:id']))
                __M_writer(u'">\n')
            elif 'creator' in twitter_card:
                __M_writer(u'    <meta name="twitter:creator" content="')
                __M_writer(unicode(twitter_card['creator']))
                __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if len(translations) > 1:
            for langname in translations.keys():
                if langname != lang and post.is_translation_available(langname):
                    __M_writer(u'                <link rel="alternate" hreflang="')
                    __M_writer(unicode(langname))
                    __M_writer(u'" href="')
                    __M_writer(unicode(post.permalink(langname)))
                    __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mathjax_script(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n')
        if post.is_mathjax:
            __M_writer(u'        <script type="text/x-mathjax-config">\n        MathJax.Hub.Config({tex2jax: {inlineMath: [[\'$latex \',\'$\'], [\'\\\\(\',\'\\\\)\']]}});</script>\n        <script src="/assets/js/mathjax.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_open_graph_metadata(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        striphtml = context.get('striphtml', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if use_open_graph:
            __M_writer(u'    <meta name="og:title" content="')
            __M_writer(filters.html_escape(unicode(post.title()[:70])))
            __M_writer(u'">\n    <meta name="og:url" content="')
            __M_writer(unicode(abs_link(permalink)))
            __M_writer(u'">\n')
            if post.description():
                __M_writer(u'    <meta name="og:description" content="')
                __M_writer(filters.html_escape(unicode(post.description()[:200])))
                __M_writer(u'">\n')
            else:
                __M_writer(u'    <meta name="og:description" content="')
                __M_writer(filters.html_escape(unicode(post.text(strip_html=True)[:200])))
                __M_writer(u'">\n')
            __M_writer(u'    <meta name="og:site_name" content="')
            __M_writer(striphtml(unicode(blog_title)))
            __M_writer(u'">\n    <meta name="og:type" content="article">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"15": 0, "20": 2, "21": 11, "22": 21, "23": 38, "24": 52, "25": 68, "26": 76, "32": 13, "37": 13, "38": 14, "39": 15, "40": 16, "41": 17, "42": 17, "43": 17, "44": 17, "45": 17, "46": 19, "52": 23, "57": 23, "58": 24, "59": 25, "60": 26, "61": 27, "62": 28, "63": 28, "64": 28, "65": 28, "66": 28, "67": 28, "68": 31, "69": 32, "70": 33, "71": 33, "72": 33, "73": 33, "74": 33, "75": 33, "76": 36, "82": 54, "87": 54, "88": 55, "89": 56, "90": 56, "91": 56, "92": 57, "93": 58, "94": 58, "95": 58, "96": 59, "97": 60, "98": 60, "99": 60, "100": 62, "101": 63, "102": 63, "103": 63, "104": 64, "105": 65, "106": 65, "107": 65, "113": 3, "120": 3, "121": 4, "122": 5, "123": 6, "124": 7, "125": 7, "126": 7, "127": 7, "128": 7, "134": 70, "138": 70, "139": 71, "140": 72, "146": 40, "155": 40, "156": 41, "157": 42, "158": 42, "159": 42, "160": 43, "161": 43, "162": 44, "163": 45, "164": 45, "165": 45, "166": 46, "167": 47, "168": 47, "169": 47, "170": 49, "171": 49, "172": 49, "178": 172}, "uri": "post_helper.tmpl", "filename": "/Users/talos/.virtualenvs/nikola/lib/python2.7/site-packages/nikola/data/themes/base/templates/post_helper.tmpl"}
__M_END_METADATA
"""
