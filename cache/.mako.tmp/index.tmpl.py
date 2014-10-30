# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1414693844.852998
_enable_loop = True
_template_filename = u'/Users/talos/.virtualenvs/nikola/lib/python2.7/site-packages/nikola/data/themes/base/templates/index.tmpl'
_template_uri = u'index.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'comments', context._clean_inheritance_tokens(), templateuri=u'comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'comments')] = ns

    ns = runtime.TemplateNamespace(u'helper', context._clean_inheritance_tokens(), templateuri=u'index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        date_format = context.get('date_format', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        messages = context.get('messages', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        date_format = context.get('date_format', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        messages = context.get('messages', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<div class="postindex">\n')
        for post in posts:
            __M_writer(u'    <article class="h-entry post-')
            __M_writer(unicode(post.meta('type')))
            __M_writer(u'">\n    <header>\n        <h1 class="p-name entry-title"><a href="')
            __M_writer(unicode(post.permalink()))
            __M_writer(u'" class="u-url">')
            __M_writer(unicode(post.title()))
            __M_writer(u'</h1></a>\n        <div class="metadata">\n            <p class="byline author vcard"><span class="byline-name fn">')
            __M_writer(unicode(post.author()))
            __M_writer(u'</span></p>\n            <p class="dateline"><a href="')
            __M_writer(unicode(post.permalink()))
            __M_writer(u'" rel="bookmark"><time class="published dt-published" datetime="')
            __M_writer(unicode(post.date.isoformat()))
            __M_writer(u'" itemprop="datePublished" title="')
            __M_writer(unicode(messages("Publication date")))
            __M_writer(u'">')
            __M_writer(unicode(post.formatted_date(date_format)))
            __M_writer(u'</time></a></p>\n')
            if not post.meta('nocomments') and site_has_comments:
                __M_writer(u'                <p class="commentline">')
                __M_writer(unicode(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer(u'\n')
            __M_writer(u'        </div>\n    </header>\n')
            if index_teasers:
                __M_writer(u'    <div class="p-summary entry-summary">\n    ')
                __M_writer(unicode(post.text(teaser_only=True)))
                __M_writer(u'\n')
            else:
                __M_writer(u'    <div class="e-content entry-content">\n    ')
                __M_writer(unicode(post.text(teaser_only=False)))
                __M_writer(u'\n')
            __M_writer(u'    </div>\n    </article>\n')
        __M_writer(u'</div>\n')
        __M_writer(unicode(helper.html_pager()))
        __M_writer(u'\n')
        __M_writer(unicode(comments.comment_link_script()))
        __M_writer(u'\n')
        __M_writer(unicode(helper.mathjax_script(posts)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"22": 3, "25": 2, "31": 0, "45": 2, "46": 3, "47": 4, "52": 34, "58": 6, "71": 6, "72": 8, "73": 9, "74": 9, "75": 9, "76": 11, "77": 11, "78": 11, "79": 11, "80": 13, "81": 13, "82": 14, "83": 14, "84": 14, "85": 14, "86": 14, "87": 14, "88": 14, "89": 14, "90": 15, "91": 16, "92": 16, "93": 16, "94": 18, "95": 20, "96": 21, "97": 22, "98": 22, "99": 23, "100": 24, "101": 25, "102": 25, "103": 27, "104": 30, "105": 31, "106": 31, "107": 32, "108": 32, "109": 33, "110": 33, "116": 110}, "uri": "index.tmpl", "filename": "/Users/talos/.virtualenvs/nikola/lib/python2.7/site-packages/nikola/data/themes/base/templates/index.tmpl"}
__M_END_METADATA
"""
