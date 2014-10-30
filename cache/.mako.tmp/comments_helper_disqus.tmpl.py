# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1414693844.91641
_enable_loop = True
_template_filename = u'/Users/talos/.virtualenvs/nikola/lib/python2.7/site-packages/nikola/data/themes/base/templates/comments_helper_disqus.tmpl'
_template_uri = u'comments_helper_disqus.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_form', 'comment_link', 'comment_link_script']



import json
translations = {
    'es': 'es_ES',
}


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if comment_system_id:
            __M_writer(u'        <div id="disqus_thread"></div>\n        <script>\n        var disqus_shortname ="')
            __M_writer(unicode(comment_system_id))
            __M_writer(u'",\n')
            if url:
                __M_writer(u'            disqus_url="')
                __M_writer(unicode(url))
                __M_writer(u'",\n')
            __M_writer(u'        disqus_title=')
            __M_writer(unicode(json.dumps(title)))
            __M_writer(u',\n        disqus_identifier="')
            __M_writer(unicode(identifier))
            __M_writer(u'",\n        disqus_config = function () {\n            this.language = "')
            __M_writer(unicode(translations.get(lang, lang)))
            __M_writer(u'";\n        };\n        (function() {\n            var dsq = document.createElement(\'script\'); dsq.async = true;\n            dsq.src = \'//\' + disqus_shortname + \'.disqus.com/embed.js\';\n            (document.getElementsByTagName(\'head\')[0] || document.getElementsByTagName(\'body\')[0]).appendChild(dsq);\n        })();\n    </script>\n    <noscript>Please enable JavaScript to view the <a href="//disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>\n    <a href="//disqus.com" class="dsq-brlink" rel="nofollow">Comments powered by <span class="logo-disqus">Disqus</span></a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if comment_system_id:
            __M_writer(u'    <a href="')
            __M_writer(unicode(link))
            __M_writer(u'#disqus_thread" data-disqus-identifier="')
            __M_writer(unicode(identifier))
            __M_writer(u'">Comments</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if comment_system_id:
            __M_writer(u'       <script>var disqus_shortname="')
            __M_writer(unicode(comment_system_id))
            __M_writer(u'";(function(){var a=document.createElement("script");a.async=true;a.src="//"+disqus_shortname+".disqus.com/count.js";(document.getElementsByTagName("head")[0]||document.getElementsByTagName("body")[0]).appendChild(a)}());</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"15": 2, "22": 0, "27": 7, "28": 31, "29": 37, "30": 44, "36": 9, "42": 9, "43": 10, "44": 11, "45": 13, "46": 13, "47": 14, "48": 15, "49": 15, "50": 15, "51": 17, "52": 17, "53": 17, "54": 18, "55": 18, "56": 20, "57": 20, "63": 33, "68": 33, "69": 34, "70": 35, "71": 35, "72": 35, "73": 35, "74": 35, "80": 40, "85": 40, "86": 41, "87": 42, "88": 42, "89": 42, "95": 89}, "uri": "comments_helper_disqus.tmpl", "filename": "/Users/talos/.virtualenvs/nikola/lib/python2.7/site-packages/nikola/data/themes/base/templates/comments_helper_disqus.tmpl"}
__M_END_METADATA
"""
